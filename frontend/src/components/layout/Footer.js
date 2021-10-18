import React from 'react';
import {NavLink} from "react-router-dom";

const Footer = () => {
    return (
        <>
            <div className="footer">
                <div className="container">
                    <div className="row">
                        <div className="col-lg-12">
                            <div className="footer-col first">
                                <h6>About School Management System</h6>
                                <p className="p-small">
                                    An ERP System for schools
                                </p>
                            </div>

                            <div className="footer-col second">
                                <h6>Links</h6>
                                <ul className="list-unstyled li-space-lg p-small">
                                    <li>
                                        <NavLink to="terms.html">Terms & Conditions</NavLink>
                                    </li>
                                    <li>
                                        <NavLink to="privacy.html">Privacy Policy</NavLink>
                                    </li>
                                    <li>
                                        <NavLink to="#header">Home</NavLink>
                                    </li>
                                    <li>
                                        <NavLink to="#features">Features</NavLink>
                                    </li>
                                </ul>
                            </div>

                            <div className="footer-col third">
                            <span className="fa-stack">
                                <NavLink to="#your-link">
                                    <i className="fas fa-circle fa-stack-2x"/>
                                    <i className="fab fa-facebook-f fa-stack-1x"/>
                                </NavLink>
                            </span>
                                <span className="fa-stack">
                                <NavLink to="#your-link">
                                    <i className="fas fa-circle fa-stack-2x"/>
                                    <i className="fab fa-twitter fa-stack-1x"/>
                                </NavLink>
                            </span>
                                <span className="fa-stack">
                                <NavLink to="#your-link">
                                    <i className="fas fa-circle fa-stack-2x"/>
                                    <i className="fab fa-pinterest-p fa-stack-1x"/>
                                </NavLink>
                            </span>
                                <span className="fa-stack">
                                <NavLink to="#your-link">
                                    <i className="fas fa-circle fa-stack-2x"/>
                                    <i className="fab fa-instagram fa-stack-1x"/>
                                </NavLink>
                            </span>
                                <p className="p-small">Contact Us
                                    <br/>
                                    <NavLink to="mailto:contact@site.com"><strong>contact@site.com</strong></NavLink>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <button onClick="topFunction()" id="myBtn">
                <img src="images/up-arrow.png" alt="alternative"/>
            </button>
        </>
    );
};

export default Footer;