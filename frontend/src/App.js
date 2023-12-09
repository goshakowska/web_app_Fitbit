import React from "react";
import './styles.css';
import {BrowserRouter, Routes, Route } from 'react-router-dom';
import StartPage from "./components/StartPage"
import Header from "./components/Header";
import FitnessClubs from "./components/FitnessClubs";
import RegistrationForm1 from "./components/RegistrationForm/RegistrationForm1";

function App() {
  return(
      <div className="App">
            <BrowserRouter>
              <Header />

              <Routes>
              <Route exact path="/" element={<StartPage />} />
              <Route exact path='/silownie' element={<FitnessClubs />} />
              <Route exact path='/rejestracja' element={<RegistrationForm1 />} />
              </Routes>

            </BrowserRouter>
      </div>
);


}
export default App;
