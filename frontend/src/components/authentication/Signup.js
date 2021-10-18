import React from 'react';
import "../../style/auth.css";
import {NavLink} from "react-router-dom";
import {staticURL} from "../../index";

const Signup = () => {
    return (
        <>
            <section>
                <div className="container d-flex justify-content-center">
                    <div className="login-form">
                        <div className="card-wrapper mt-5">

                            <div className="brand text-center p-3">
                                <img src={staticURL + 'images/favicon.svg'} alt="login page" height="70"/>
                            </div>

                            <div className="card fat login-form">
                                <div className="card-body">
                                    <form>

                                        <div className="form-group mb-3">
                                            <label htmlFor="name">Name</label>
                                            <input type="text" className="form-control" name="name" required autoFocus/>
                                            <div className="invalid-feedback">
                                                What's your name?
                                            </div>
                                        </div>

                                        <div className="form-group mb-3">
                                            <label htmlFor="email">Email</label>
                                            <input type="email" className="form-control" name="email" required/>
                                            <div className="invalid-feedback">
                                                Your email is invalid
                                            </div>
                                        </div>

                                        <div className="form-group mb-3">
                                            <label htmlFor="password">Password</label>
                                            <input type="password" className="form-control" name="password" required/>
                                            <div className="invalid-feedback">
                                                Password is required
                                            </div>
                                        </div>

                                        <div className="form-group my-2">
                                            <button type="submit" className="btn btn-primary btn-block w-100 my-2">
                                                Register
                                            </button>
                                        </div>
                                        <div className="mt-4 text-center">
                                            Already have an account? <NavLink to="/login">Login</NavLink>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </>
    );
};

export default Signup;