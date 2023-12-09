import React from 'react';
import {
  Navbar,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
  UncontrolledDropdown,
  DropdownToggle,
  DropdownMenu,
  DropdownItem,
  NavbarText,
  Row,
  Col,
} from 'reactstrap';
import "../styles.css"

function Header() {
  return (
    <div>
    <Nav pills className='header-style'>
    <NavbarBrand>
    <img src="./logofitbit.png" alt="Logo"></img>
    </NavbarBrand>
  <NavItem className='button-style1'>
    <NavLink
      href="./silownie" className='text-style'
    >
      NASZE SIŁOWNIE
    </NavLink>
  </NavItem>
  <NavItem className='button-style1'>
    <NavLink href="./sklep_karnetow" className='text-style'>
      KARNETY
    </NavLink>
  </NavItem>
  <NavItem className='button-style1'>
    <NavLink href="./kontakt" className='text-style'>
      KONTAKT
    </NavLink>
  </NavItem>
</Nav>
    </div>
  );
}

export default Header;
