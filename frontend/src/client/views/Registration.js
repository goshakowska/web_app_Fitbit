import RegistrationFormInputs from "../components/RegistrationFormInputs";

function Registration() {

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