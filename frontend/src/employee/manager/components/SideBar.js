import React, { useState } from 'react';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';
import "../styles/styles.css"
import employeeToken from '../../EmployeeToken';


function SideBarManager() {
  const [isOpen, setIsOpen] = useState(false);
  const toggle = () => setIsOpen(!isOpen);
  const {userName, logout} = employeeToken();

  const handleLogout = () => {
    logout();
  }

  return (
    <div >
      <Navbar>
        <NavbarBrand href="/"></NavbarBrand>
        <NavbarToggler className= 'user-circle-text-style' onClick={toggle} > <span>{userName()}</span> </NavbarToggler>
        <Collapse isOpen={isOpen} navbar>
          <Nav className='sidebar-style dark-green' navbar>
            <NavItem className='sidebar-pos-style'>
              <NavLink className='text-style-sidebar' href="/kalendarz_klienta">
                Wyświetl statystyki
                </NavLink>
            </NavItem>
            <NavItem className='sidebar-pos-style' onClick={handleLogout}>
            <NavLink className='text-style-sidebar' href="/" >
                Wyloguj się
              </NavLink>
              </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
}

export default SideBarManager;