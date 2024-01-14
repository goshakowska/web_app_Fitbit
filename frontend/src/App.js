import React from "react";
import './client/styles/styles.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';

import {FormProvider} from "./client/context/RegistrationContext";
import { WeekSwitcherProvider } from "./client/context/WeekSwitcherContext";

import StartPage from "./client/components/StartPage"
import Header from "./client/components/Header";
import FitnessClubs from "./client/components/FitnessClubs";
import LoginForm from "./client/components/LoginForm";
import TicketsShop from "./client/components/TicketsShop";
import Trainings from "./client/components/Trainings";
import TrainingDetails from "./client/components/TrainingDetails";
import ClientTickets from "./client/components/ClientTickets";
import ClientTicketDetails from "./client/components/ClientTicketDetails";
import Profile from "./client/components/Profile";
import FitnessClubDetails from "./client/components/FitnessClubDetails";

import Registration from "./client/views/Registration";
import ClientClasses from "./client/views/ClientClasses";


// employee

import LoginEmployeeForm from "./employee/components/LoginEmployeeForm";
// manager
import FitnessClubStatistics from "./employee/manager/components/FitnessClubStatistics";

// portier
import SearchBar from "./employee/portier/components/SearchBar";
import ClientInfo from "./employee/portier/components/ClientInfo";

// trainer
import Scheduler from "./employee/trainer/components/Scheduler";
import TrainingCreator from "./employee/trainer/components/TrainingCreator";
import ClientTrainingInfo from "./employee/trainer/components/ClientTrainingInfo";
import GroupClassInfo from "./employee/trainer/components/GroupClassesInfo";

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
              <Route exact path='/szczegoly_silowni' element={<FitnessClubDetails />} />
              <Route exact path='/login' element={<LoginForm />} />
              <Route exact path='/rejestracja' element={<Registration />} />
              <Route exact path='/sklep_karnetow' element={<TicketsShop />} />
              <Route exact path='/kalendarz_klienta' element={<ClientClasses />} />
              <Route exact path='/statystyki' element={<Trainings />} />
              <Route exact path='/szczegoly_treningu' element={<TrainingDetails />} />
              <Route exact path='/karnety_klienta' element={<ClientTickets />} />
              <Route exact path='/szczegoly_karnetu' element={<ClientTicketDetails />} />
              <Route exact path='/profil' element={<Profile />} />
              {/* employee */}
              <Route exact path='/login_pracowników' element={<LoginEmployeeForm />} />
              {/* manager */}
              <Route exact path='/menadżer/' element={<FitnessClubStatistics />} />
              {/* portier */}
              <Route exact path='/portier/' element={<SearchBar />} />
              <Route exact path='/portier/clientinfo' element={<ClientInfo />} />
              {/* trainer */}
              <Route exact path='/trener/' element={<Scheduler />} />
              <Route exact path='/trener/planer' element={<TrainingCreator />} />
              <Route exact path='/trener/client_info' element={<ClientTrainingInfo />} />
              <Route exact path='/trener/group_class_info' element={<GroupClassInfo />}/>
              </Routes>

              </WeekSwitcherProvider>
              </FormProvider>
            </BrowserRouter>
      </div>
);


}
export default App;
