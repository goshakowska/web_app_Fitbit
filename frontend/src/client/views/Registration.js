import { useContext } from "react";
import FormContext from "../context/RegistrationContext";
import RegistrationFormInputs from "../components/RegistrationFormInputs";

function Registration() {
    const {page, setPage, title, formData} = useContext(FormContext)

    return (
        <div>
        <form>
        <p className="textRegistration">Zarejestruj się</p>
        <p className='linkTexts'>Gwiazdką * oznaczono pola obowiązkowe</p>
            <RegistrationFormInputs />
        </form>
        </div>

    )
}

export default Registration