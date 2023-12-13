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
import clientToken from '../ClientToken';


function SideBarClient() {
  const [isOpen, setIsOpen] = useState(false);
  const toggle = () => setIsOpen(!isOpen);
  const {userName, logout} = clientToken();

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
                Twoje zajęcia
                </NavLink>
            </NavItem>
            <NavItem className='sidebar-pos-style'>
              <NavLink className='text-style-sidebar' href="/statystyki">
                Statystyki
              </NavLink>
            </NavItem>
            <NavItem className='sidebar-pos-style'>
              <NavLink className='text-style-sidebar' href="/koszyk">
                Koszyk
              </NavLink>
            </NavItem>
            <NavItem className='sidebar-pos-style'>
              <NavLink className='text-style-sidebar' href="/karnety_klienta">
                Twoje karnety
              </NavLink>
            </NavItem>
            <NavItem className='sidebar-pos-style'>
              <NavLink className='text-style-sidebar' href="/sklep_zajec">
                Kup zajęcia
              </NavLink>
            </NavItem>
            <NavItem className='sidebar-pos-style'>
              <NavLink className='text-style-sidebar' href="/profil">
                Profil klienta
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

export default SideBarClient;