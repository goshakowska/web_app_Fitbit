import React from "react";
import './styles.css';
import {BrowserRouter, Routes, Route } from 'react-router-dom';
// import RegistrationForm1 from "./components/RegistrationForm/RegistrationForm1";
import StartPage from "./components/StartPage"
import Header from "./components/Header";

function App() {
  return(
      <div className="App">
            <BrowserRouter>
              <Header />

              <Routes>
              <Route exact path="/" element={<StartPage />} />
              </Routes>

            </BrowserRouter>
      </div>
);


}
export default App;
