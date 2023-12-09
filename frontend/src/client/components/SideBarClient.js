import React, { useState } from 'react';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  NavbarText,
} from 'reactstrap';
import "../styles.css"

function SideBarClient() {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => setIsOpen(!isOpen);
  return (
    <div >
      <Navbar>
        <NavbarBrand href="/"></NavbarBrand>
        <NavbarToggler className= 'text-style' onClick={toggle} > <span>User</span> </NavbarToggler>
        <Collapse isOpen={isOpen} navbar>
          <Nav className='sidebar-style dark-green' navbar>
            <NavItem className='sidebar-pos-style'>
              <NavLink className='text-style-sidebar' href="/kalendarz_klienta">Twoje zajęcia</NavLink>
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
            <NavItem className='sidebar-last-pos-style'>
              <NavLink className='text-style-sidebar'>
                Wyloguj
              </NavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
}

export default SideBarClient;