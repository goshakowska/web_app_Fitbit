import React, {createContext, useState} from "react";

const FormContext = createContext({})

export const FormProvider = ({ children }) => {
  // create context for multi-page user registration
    const title = {
        0: 'User Data',
        1: 'Personal Info',
        2: 'Preferences'
    }

    const [page, setPage] = useState(0)

    const [formData, setFormData] = useState({
        name: null,
        surname: null,
        login: null,
        password: null,
        repeatedPassword: null,
        email: null,
        dateOfBirth: null,
        sex: null,
        phone: null,
        current_weight: null,
        target_weight: null,
        advancement: null,
        height: null,
        training_frequency: null,
        training_goal_id: null,
        training_time: null,
        validate: {
          loginState: "",
          emailState:"",
          passwordState: "",
          repeatedPasswordState: "",
          phoneState: "",
          nameState: "",
          surnameState: "",
        },
      });

      const handleChange = (e) => {
        console.log(formData)
        const { name, value } = e.target;
        setFormData((prevData) => ({
          ...prevData,
          [name]: value
        }));
      };

      // changing pages
      const handlePrev = () => setPage(prev => prev - 1);
      const handleNext = () => setPage(prev => prev + 1);



    return(
        <FormContext.Provider value={{title, page, setPage, formData, setFormData, handleChange, handlePrev, handleNext}}>
            {children}
        </FormContext.Provider>
    )
}

export default FormContext;