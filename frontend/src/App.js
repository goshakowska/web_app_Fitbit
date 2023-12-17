import React from "react";
import './client/styles/styles.css';
import {BrowserRouter, Routes, Route, Form } from 'react-router-dom';

import {FormProvider} from "./client/context/RegistrationContext";
import { WeekSwitcherProvider } from "./client/context/WeekSwitcherContext";

import StartPage from "./client/components/StartPage"
import Header from "./client/components/Header";
import FitnessClubs from "./client/components/FitnessClubs";
import LoginForm from "./client/components/LoginForm";
import Tickets from "./client/components/Tickets";
import Trainings from "./client/components/Trainings";
import TrainingDetails from "./client/components/TrainingDetails";

import Registration from "./client/views/Registration";
import ClientClasses from "./client/views/ClientClasses";


function App() {
  return(
      <div className="App">
            <BrowserRouter>
            <FormProvider>
            <WeekSwitcherProvider>
              <Header />

              <Routes>
              <Route exact path="/" element={<StartPage />} />
              <Route exact path='/silownie' element={<FitnessClubs />} />
              <Route exact path='/login' element={<LoginForm />} />
              <Route exact path='/rejestracja' element={<Registration />} />
              <Route exact path='/sklep_karnetow' element={<Tickets />} />
              <Route exact path='/kalendarz_klienta' element={<ClientClasses />} />
              <Route exact path='/statystyki' element={<Trainings />} />
              <Route exact path='/szczegoly' element={<TrainingDetails />} />
              </Routes>

              </WeekSwitcherProvider>
              </FormProvider>
            </BrowserRouter>
      </div>
);


}
export default App;
