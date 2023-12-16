import { useContext } from "react";
import RegistrationUserData from "./RegistrationUserData";
import RegistrationPersonalInfo from "./RegistrationPersonalInfo";
import RegistrationPreferences from "./RegistrationPreferences";
import FormContext from '../context/RegistrationContext';

function RegistrationFormInputs() {
    const {page} = useContext(FormContext)

    const display = {
        0: <RegistrationUserData />,
        1: <RegistrationPersonalInfo />,
        2: <RegistrationPreferences />
    }

    return (
        <div>
            {display[page]}
        </div>
    )

}

export default RegistrationFormInputs