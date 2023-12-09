import React from 'react';
import {
  NavbarBrand,
  Nav,
  NavbarText,
  NavItem,
  NavLink,
} from 'reactstrap';
import "../styles.css"
import SideBarClient from './SideBarClient.js';

function Header() {

  return (
    <div>
    <Nav pills className='header-style'>
    <NavbarBrand>
    <img src="./logofitbit.png" alt="Logo"></img>
    </NavbarBrand>
  <NavItem className='button-style-header'>
    <NavLink
      href="./silownie" className='text-style'
    >
      NASZE SIŁOWNIE
    </NavLink>
  </NavItem>
  <NavItem className='button-style-header'>
    <NavLink href="./sklep_karnetow" className='text-style'>
      KARNETY
    </NavLink>
  </NavItem>
  <NavItem className='button-style-header'>
    <NavLink href="./kontakt" className='text-style'>
      KONTAKT
    </NavLink>
  </NavItem>
    <SideBarClient />
</Nav>
    </div>
  );
}

export default Header;
