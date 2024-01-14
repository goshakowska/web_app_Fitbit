import React, { useState, useEffect } from 'react';
import { Button, Input, InputGroup } from 'reactstrap';
import buyCart from '../functions/buyCart';
import { useLocation, useNavigate } from "react-router-dom";
import clientToken from '../ClientToken';
import CartToken from '../CartToken';
import secondsToHHMMSS from '../functions/secondsToHHMMSS';

function Reservation() {
    const {userId} = clientToken();
    const {getCart, emptyCart} = CartToken();
    const location = useLocation();
    const reservationList = location.state.reservationList;

    const [countdownTime, setCountdownTime] = useState(2000);
    const navigate = useNavigate();

    useEffect(() => {
      const odlicz = setInterval(() => {
        setCountdownTime(prevCzas => prevCzas - 1);
      }, 1000);
      if (countdownTime === 0) {
        clearInterval(odlicz);
        alert('Transakcja została anulowana')
        navigate('/koszyk');
      }
      return () => clearInterval(odlicz);
    }, [countdownTime]);


    const handleBuyCart = async (event, client_id, reserved_gym_classes, gym_tickets) => {
        await buyCart(event, client_id, reserved_gym_classes, gym_tickets);
        emptyCart();
        alert('Potwierdzenie zakupu.')
        navigate('/koszyk');
    }

  return (
    <div className='layout2'>
      <div className='textLogin2'>Potwierdzenie zakupu</div>
      <div className=' layout labelsStyle'>Czas na zrealizowanie płatności: </div>
        <div className='sumStyle layout text-style marginBottom'> {secondsToHHMMSS(countdownTime)}</div>
        <div>
          <div className='textStyleBiggerWhite'>Wykonaj przelew</div>
        <InputGroup className="inputGroup">
        <Input className='centeredTextInput' placeholder='Wprowadź numer konta bankowego'></Input>
        </InputGroup>
        <InputGroup className="inputGroup">
        <Input className='centeredTextInput' placeholder='Imię'></Input>
        </InputGroup>
        <InputGroup className="inputGroup">
        <Input className='centeredTextInput' placeholder='Nazwisko'></Input>
        </InputGroup>
        <InputGroup className="inputGroup">
        <Input className='centeredTextInput' placeholder='E-mail'></Input>
        </InputGroup></div>
        <Button type="button" className="cartStyle text-style" onClick={(e) => {console.log(getCart()[0]);handleBuyCart(e, userId(), reservationList, getCart()[0])}}
                        >Potwierdź</Button>
    </div>
  );
}


export default Reservation