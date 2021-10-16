import React from 'react';
import {NavLink} from "react-router-dom";

const Header = () => {
    return (
        <>
            <nav className="navbar navbar-light bg-light">
                <div className="container-fluid">
                    <NavLink className="navbar-brand" to="/">SCHOOL MANAGEMENT</NavLink>

                    <button className="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar"
                            aria-controls="offcanvasNavbar">
                        <span className="navbar-toggler-icon"/>
                    </button>

                    <div className="offcanvas offcanvas-end" tabIndex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">

                        <div className="offcanvas-header">
                            <h5 className="offcanvas-title" id="offcanvasNavbarLabel">School Management System</h5>
                            <button type="button" className="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"/>
                        </div>

                        <div className="offcanvas-body">

                            <form className="d-flex">
                                <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
                                <button className="btn btn-outline-success" type="submit">Search</button>
                            </form>

                            <hr/>

                            <ul className="navbar-nav justify-content-end flex-grow-1 pe-3">
                                <li className="nav-item">
                                    <NavLink className="nav-link" aria-current="page" to="/">Home</NavLink>
                                </li>
                                <li className="nav-item">
                                    <NavLink className="nav-link" to="/signup">Sign Up</NavLink>
                                </li>
                                <li className="nav-item">
                                    <NavLink className="nav-link" to="/login">Login</NavLink>
                                </li>
                                <li className="nav-item">
                                    <NavLink className="nav-link" to="/about">About</NavLink>
                                </li>
                                <li className="nav-item">
                                    <NavLink className="nav-link" to="/contact-us">Contact Us</NavLink>
                                </li>
                                <li className="nav-item dropdown">
                                    <NavLink className="nav-link dropdown-toggle" to="" id="offcanvasNavbarDropdown" role="button"
                                             data-bs-toggle="dropdown" aria-expanded="false">
                                        More
                                    </NavLink>
                                    <ul className="dropdown-menu" aria-labelledby="offcanvasNavbarDropdown">
                                        <li><NavLink className="dropdown-item" to="/admin">Admin</NavLink></li>
                                        <li><NavLink className="dropdown-item" to="/help">Need Help</NavLink></li>
                                        <li><NavLink className="dropdown-item" to="/feedback">Feedback</NavLink></li>
                                    </ul>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </nav>
        </>
    );
};

export default Header;