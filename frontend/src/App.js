import React from "react";
import './client/styles/styles.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';

import {FormProvider} from "./client/context/RegistrationContext";
import { WeekSwitcherProvider } from "./client/context/WeekSwitcherContext";

import Header from "./client/components/Header";

import GroupClassesShopView from "./client/views/GroupClassesShop";
import IndvClassesShopView from "./client/views/IndvClassesShop";
import ClassDetailsView from "./client/views/ClientClassDetails";
import ClassDetailsShopView from "./client/views/ClassDetailsShop";
import ClientTicketsView from "./client/views/ClientTickets";
import TrainingDetailsView from "./client/views/TrainingDetails";
import TrainingsView from "./client/views/Trainings";
import TicketsShopView from "./client/views/TicketsShop";
import FitnessClubsView from "./client/views/FitnessClubs";
import StartPageView from "./client/views/StartPage"
import LoginFormView from "./client/views/Login";
import ReservationView from "./client/views/Reservation";
import Registration from "./client/views/Registration";
import ClientClasses from "./client/views/ClientClasses";
import CartView from "./client/views/Cart";
import ClientTicketDetailsView from "./client/views/ClientTicketDetails";
import ProfileView from "./client/views/Profile";
import FitnessClubDetailsView from "./client/views/FitnessClubDetails";
import ClassTypesView from "./client/views/ClassTypes";
import PriceListView from "./client/views/PriceList";


// employee

import LoginEmployeeForm from "./employee/views/LoginEmployeeForm";
// manager
import FitnessClubStatistics from "./employee/manager/views/FitnessClubStatistics";

// portier
import SearchBar from "./employee/portier/views/SearchBar";
import ClientInfo from "./employee/portier/views/ClientInfo";

// trainer
import Scheduler from "./employee/trainer/views/Scheduler";
import TrainingCreator from "./employee/trainer/views/TrainingCreator";
import ClientTrainingInfo from "./employee/trainer/views/ClientTrainingInfo";
import GroupClassInfo from "./employee/trainer/views/GroupClassesInfo";

function App() {
  return(
      <div className="App">
            <BrowserRouter>
            <FormProvider>
            <WeekSwitcherProvider>
              <Header />

              <Routes>
              <Route exact path="/" element={<StartPageView />} />
              <Route exact path='/silownie' element={<FitnessClubsView />} />
              <Route exact path='/szczegoly_silowni' element={<FitnessClubDetailsView />} />
              <Route exact path='/login' element={<LoginFormView />} />
              <Route exact path='/rejestracja' element={<Registration />} />
              <Route exact path='/sklep_karnetow' element={<TicketsShopView />} />
              <Route exact path='/kalendarz_klienta' element={<ClientClasses />} />
              <Route exact path='/statystyki' element={<TrainingsView />} />
              <Route exact path='/szczegoly_treningu' element={<TrainingDetailsView />} />
              <Route exact path='/karnety_klienta' element={<ClientTicketsView />} />
              <Route exact path='/szczegoly_karnetu' element={<ClientTicketDetailsView />} />
              <Route exact path='/profil' element={<ProfileView />} />
              <Route exact path='/szczegoly_zajec' element={<ClassDetailsView />} />
              <Route exact path='/statystyki' element={<TrainingsView />} />
              <Route exact path='/szczegoly_treningu' element={<TrainingDetailsView />} />
              <Route exact path='/karnety_klienta' element={<ClientTicketsView />} />
              <Route exact path='/szczegoly_karnetu' element={<ClientTicketDetailsView />} />
              <Route exact path='/profil' element={<ProfileView />} />
              <Route exact path='/sklep_zajec' element={<ClassTypesView />} />
              <Route exact path='/grupowe_sklep' element={<GroupClassesShopView />} />
              <Route exact path='/indywidualne_sklep' element={<IndvClassesShopView />} />
              <Route exact path='/szczegoly_sklep' element={<ClassDetailsShopView />} />
              <Route exact path='/koszyk' element={<CartView />} />
              <Route exact path='/platnosc' element={<ReservationView />} />
              <Route exact path='/cennik' element={<PriceListView />} />
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
