import React from "react";
import './client/styles/styles.css';
import {BrowserRouter, Routes, Route, Form } from 'react-router-dom';

import {FormProvider} from "./client/context/RegistrationContext";

import StartPage from "./client/components/StartPage"
import Header from "./client/components/Header";
import FitnessClubs from "./client/components/FitnessClubs";
import LoginForm from "./client/components/LoginForm";
import Registration from "./client/views/Registration";


function App() {
  return(
      <div className="App">
            <BrowserRouter>
            <FormProvider>
              <Header />

              <Routes>
              <Route exact path="/" element={<StartPage />} />
              <Route exact path='/silownie' element={<FitnessClubs />} />
              <Route exact path='/login' element={<LoginForm />} />
              <Route exact path='/rejestracja' element={<Registration />} />
              </Routes>

              </FormProvider>
            </BrowserRouter>
      </div>
);


}
export default App;
