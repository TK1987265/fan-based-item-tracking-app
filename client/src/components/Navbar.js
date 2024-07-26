import React from 'react';
import { Link } from 'react-router-dom';


const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-link">Home</Link>
        <Link to="/locations" className="navbar-link">Locations</Link>
        <Link to="/items" className="navbar-link">Items</Link>
        <Link to="/location-items" className="navbar-link">Location Items</Link>
      </div>
    </nav>
  );
};

export default Navbar;
