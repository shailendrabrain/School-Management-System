import React from 'react';
import "../../style/home.css";
import {staticURL} from "../../index";
import Footer from "../layout/Footer";

const Home = () => {
    return (
        <>
            <header id="header" className="header">
                <div className="container">
                    <div className="row">
                        <div className="col-lg-6">
                            <div className="text-container">
                                <h1 className="h1-large">
                                    The #1 School Management System
                                </h1>
                                <p className="p-large">
                                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut dignissim, neque ut vanic barem
                                    ultrices sollicitudin
                                </p>
                                <a className="btn-solid-lg" href="sign-up.html">Sign up for free</a>
                            </div>
                        </div>

                        <div className="col-lg-6">
                            <div className="image-container">
                                <img className="img-fluid" src={staticURL + 'svg/header-illustration.svg'} alt="alternative"/>
                            </div>
                        </div>
                    </div>
                </div>
            </header>

            <Footer/>
        </>
    );
};

export default Home;