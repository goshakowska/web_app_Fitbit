import React, {createContext, useState} from "react";

const FormContext = createContext({})

export const FormProvider = ({ children }) => {

    const title = {
        0: 'User Data',
        1: 'Personal Info',
        2: 'Preferences'
    }

    const [page, setPage] = useState(0)

    const [formData, setFormData] = useState({
        name: '',
        surname: '',
        login: '',
        password: '',
        email: '',
        dateOfBrith: '',
        sex: '',
        phone: '',
        current_weight: '',
        target_weight: '',
        advancement: '',
        height: '',
        training_frequency: '',
        training_goal_id: '',
        training_time: '',
      });

      const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
          ...prevData,
          [name]: value
        }));
      };

      const handlePrev = () => setPage(prev => prev - 1);
      const handleNext = () => setPage(prev => prev + 1);

    return(
        <FormContext.Provider value={{title, page, setPage, formData, setFormData, handleChange, handlePrev, handleNext}}>
            {children}
        </FormContext.Provider>
    )
}

export default FormContext;