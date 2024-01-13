import React, { useState } from 'react';
import { Button, Modal, Input, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
import buyCart from '../functions/buyCart';
import { useLocation } from "react-router-dom";
import clientToken from '../ClientToken';
import CartToken from '../CartToken';

function Reservation() {
    const {userId} = clientToken();
    const {getCart} = CartToken();
    const location = useLocation();
    const reservationList = location.state.reservationList;


    const handleBuyCart = async (event, client_id, reserved_gym_classes, gym_tickets) => {
        const details = await buyCart(event, client_id, reserved_gym_classes, gym_tickets);}

  return (
    <div>
        <td> <Button type="button" className="cartStyle" onClick={(e) => {console.log(getCart()[0]);handleBuyCart(e, userId(), reservationList, getCart()[0])}}
                        >Kup koszyk</Button> </td>
    </div>
  );
}


export default Reservation