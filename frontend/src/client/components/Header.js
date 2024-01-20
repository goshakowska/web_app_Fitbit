import React from 'react';
import {
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';
import "../styles/styles.css"
import SideBarClient from './SideBarClient.js';
import clientToken from '../ClientToken.js';
import employeeToken from '../../employee/EmployeeToken.js';
import SideBarPortier from '../../employee/portier/components/SideBarPortier.js';
import SideBarManager from '../../employee/manager/components/SideBarManager.js';
import SideBarTrainer from '../../employee/trainer/components/SideBarTrainer.js';

function Header() {
  // shows header 
  const {userId } = clientToken();
  const {userId: empUserId , userType } = employeeToken();

  console.log(empUserId(),userType())

  return (
    <div>
      <Nav pills className='header-style'>
        <NavbarBrand>
          <img src="./logofitbit.png" alt="Logo"></img>
        </NavbarBrand>
        <NavItem className='button-style-header'>
          <NavLink href="./silownie" className='text-style'>
            NASZE SIŁOWNIE
          </NavLink>
        </NavItem>
        <NavItem className='button-style-header'>
          <NavLink href="./sklep_karnetow" className='text-style'>
            KARNETY
          </NavLink>
        </NavItem>
        <NavItem className='button-style-header'>
          <NavLink href="./cennik" className='text-style'>
            CENNIK
          </NavLink>
        </NavItem>

        {(empUserId() && userType()==='trener') && <SideBarTrainer />}
        {(empUserId() && userType()==='portier') && <SideBarPortier />}
        {(empUserId() && userType()==='menadżer') && <SideBarManager />}
        {(userId() && !userType()) && <SideBarClient />}

        {(!userId() && !empUserId()) && (
          <NavItem className='button-style-login-header'>
            <NavLink href="./login" className='text-style'>
              ZALOGUJ
            </NavLink>
          </NavItem>
        )}
      </Nav>
    </div>
  );
}

export default Header;