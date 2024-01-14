export const CartToken = () => {

    const addTicket = (name, durability, type, discount, bDPrice, price, eOD, discountId, gTOI) => {
        let ticket = {
            name: name,
            durability: durability,
            type: type,
            discount: discount,
            beforeDiscountPrice: bDPrice,
            price: price,
            endOfDiscount: eOD,
            discountId: discountId,
            gymTicketOfferId: gTOI,
        }
        let storedCart = sessionStorage.getItem('ticketsCart') ?
        JSON.parse(sessionStorage.getItem('ticketsCart')) : [];
        storedCart.push(ticket)
        sessionStorage.setItem('ticketsCart', JSON.stringify(storedCart));
    }

    const addTraining = (name, price, hour, scheduleDate, weekScheduleId, freePlaces) => {
        let training = {
            name: name,
            price: price,
            hour: hour,
            schedule_date: scheduleDate,
            week_schedule_id: weekScheduleId,
            freePlaces: freePlaces,
        }
        let storedCart = sessionStorage.getItem('trainingsCart') ?
        JSON.parse(sessionStorage.getItem('trainingsCart')) : [];
        storedCart.push(training)
        sessionStorage.setItem('trainingsCart', JSON.stringify(storedCart));
    }

    const deleteTicket = (id) => {
        let storedCart = sessionStorage.getItem('ticketsCart') ?
        JSON.parse(sessionStorage.getItem('ticketsCart')) : [];
        storedCart.splice(id, 1);
        sessionStorage.setItem('ticketsCart', JSON.stringify(storedCart));
    }

    const deleteTraining = (id) => {
        let storedCart = sessionStorage.getItem('trainingsCart') ?
        JSON.parse(sessionStorage.getItem('trainingsCart')) : [];
        storedCart.splice(id, 1);
        sessionStorage.setItem('trainingsCart', JSON.stringify(storedCart));
    }

    const getCart = () => {
        let storedTrainingsCart = sessionStorage.getItem('trainingsCart') ?
        JSON.parse(sessionStorage.getItem('trainingsCart')) : [];
        let storedTicketsCart = sessionStorage.getItem('ticketsCart') ?
        JSON.parse(sessionStorage.getItem('ticketsCart')) : [];
        return [storedTicketsCart, storedTrainingsCart]
    }

    const emptyCart = () => {
        sessionStorage.removeItem('trainingsCart');
        sessionStorage.removeItem('ticketsCart');
    }

    return{addTraining, addTicket, deleteTicket, deleteTraining, getCart, emptyCart}
}

export default CartToken;