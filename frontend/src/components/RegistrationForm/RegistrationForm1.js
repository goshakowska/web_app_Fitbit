import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';


function RegistrationForm1() {
    const navigate = useNavigate();
    const [cliLogin, setcliLogin] = useState(null);
    const [formData, setFormData] = useState({
      name: '',
      surname: '',
      login: '',
      password: '',
      email: '',
      dayOfBrith: '',
      monthOfBrith: '',
      yearOfBrith: '',
      sex: '',
      phone: ''
    });



    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
          ...prevData,
          [name]: value
        }));
      };


      const handleSubmit = async (event) => {
        event.preventDefault();
        try {
          const response = await fetch('http://localhost:8000/registration/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ login: formData.login,
                                    password_hash: formData.password,
                                    email: formData.email,
                                    phone_number: formData.phone,
                                    name: formData.name,
                                    surname: formData.surname,
                                    gender: formData.sex,
                                    height: 155,
                                    birth_year: '2002-10-05',
                                    advancement: 'zaawansowany',
                                    target_weight: 55,
                                    training_frequency: 1,
                                    training_time: 60,
                                    training_goal_id: 1,
                                    gym_id: 1 }),
          });

          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          alert('Zostałeś pomyślnie zarejestrowany.')

          // const data = await response.json();
          // setFormData(formData.name, formData.surname, formData.login, formData.password, formData.email);
        } catch (error) {
          console.error('Error:', error);
        }
      };

      const handleDBcon = async () => {
        try {
          const response = await fetch('http://localhost:8000/client_login/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id: 1 }),
          });

          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }

          const data = await response.json();
          setcliLogin(data.login);
          alert('Z bazy pobrano login: '+ cliLogin)
        } catch (error) {
          console.error('Error:', error);
        }
      };

      const headingStyle = {
        fontFamily: 'Times New Roman, Times, serif',
        fontSize: '50px',
        color: '#D9D9D9'
      };

      const paragraphStyle = {
        fontFamily: 'Times New Roman, Times, serif',
        fontSize: '18px',
        color: '#D9D9D9'
      };

      const inputStyle = {
        color: 'black'
      };

    return(
        <div className="wrapper">
        <h1 style={headingStyle}>Zarejestruj się</h1>
        <h1 style={paragraphStyle}>Gwiazdką * oznaczono pola obowiązkowe</h1>
        <form onSubmit={handleSubmit}>

        <fieldset>
         <label>
           <p style={paragraphStyle}>Imię*</p>
           <input
           style = {inputStyle}
           type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
        />
         </label>
       </fieldset>

       <fieldset>
         <label>
           <p style={paragraphStyle}>Nazwisko*</p>
           <input
           style = {inputStyle}
           type="text"
            id="surname"
            name="surname"
            value={formData.surname}
            onChange={handleChange}
            required
        />
         </label>
       </fieldset>


       <fieldset>
         <label>
           <p style={paragraphStyle}>E-mail*</p>
           <input
           style = {inputStyle}
           type="text"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
        />
         </label>
       </fieldset>


       <fieldset>
         <label>
           <p style={paragraphStyle}>Login*</p>
           <input
           style = {inputStyle}
           type="text"
            id="login"
            name="login"
            value={formData.login}
            onChange={handleChange}
            required
        />
         </label>
       </fieldset>

       <fieldset>
         <label>
           <p style={paragraphStyle}>Hasło*</p>
           <input
           style = {inputStyle}
           type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
        />
         </label>
       </fieldset>

       <fieldset>
         <label>
           <p style={paragraphStyle}>Nr telefonu</p>
           <input
           style = {inputStyle}
           type="tel"
            id="phone"
            name="phone"
            value={formData.phone}
            onChange={handleChange}
        />
         </label>
       </fieldset>

       <fieldset>
         <label>
           <p style={paragraphStyle}>Płeć*</p>
           <select style = {inputStyle} name="sex" onChange={handleChange}>
               <option value="">--Ustaw swoją płeć--</option>
               <option value="K">Kobieta</option>
               <option value="M">Mężczyzna</option>
           </select>
         </label>
         </fieldset>


       <button type='submit' onClick={handleSubmit} className="mt-4 px-4 py-2 bg-orange-500 text-black rounded hover:bg-orange-600">Zarejestruj</button>

        </form>

      <div>
        <button type='submit' onClick={handleDBcon} className="mt-4 px-4 py-2 bg-orange-500 text-black rounded hover:bg-orange-600">Przetestuj połączenie z bazą</button>
      </div>

      </div>
    );
  }

  export default RegistrationForm1