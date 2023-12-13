import React from "react";
import './client/styles/styles.css';
import {BrowserRouter, Routes, Route } from 'react-router-dom';
import StartPage from "./client/components/StartPage"
import Header from "./client/components/Header";
import FitnessClubs from "./client/components/FitnessClubs";
import LoginForm from "./client/components/LoginForm";
import RegistrationForm1 from "./client/components/RegistrationForm/RegistrationForm1";


function App() {
  return(
      <div className="App">
            <BrowserRouter>
              <Header />

              <Routes>
              <Route exact path="/" element={<StartPage />} />
              <Route exact path='/silownie' element={<FitnessClubs />} />
              <Route exact path='/login' element={<LoginForm />} />
              <Route exact path='/rejestracja' element={<RegistrationForm1 />} />
              </Routes>

            </BrowserRouter>
      </div>
);


}
export default App;
