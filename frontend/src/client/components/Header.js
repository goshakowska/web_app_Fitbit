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


function Header() {
  const {userId} = clientToken();

  return (
    <div>
      <Nav pills className='header-style'>
        <NavbarBrand>
                <img src="./logofitbit.png" alt="Logo"></img>
        </NavbarBrand>
        <NavItem className='button-style-header'>
          <NavLink
            href="./silownie" className='text-style'>
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

  {userId() ? <SideBarClient /> : (<NavItem className='button-style-login-header'>
                                      <NavLink href="./login" className='text-style'>
                                        ZALOGUJ
                                      </NavLink>
                                      </NavItem>)
    };
      </Nav>
    </div>
  );
}

export default Header;