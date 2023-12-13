import React from 'react';
import './Sidebar.css';

const Sidebar = () => {
    return (
        <div className="sidebar">
            <img className="profile-picture" src="./user.png" alt="Profile Picture" />
            <button className="sidebar-button">plan tygodniowy</button>
            <button className="sidebar-button">wyświetl swój profil</button>
            <button className="sidebar-button">monitoruj swoją wypłatę</button>
        </div>
    );
};

export default Sidebar;