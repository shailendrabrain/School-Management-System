import React from 'react';
import "../../style/auth.css";
import {staticURL} from "../../index";
import {NavLink} from "react-router-dom";

const Login = () => {
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
                                            <label htmlFor="email">Email</label>
                                            <input type="email" className="form-control" autoFocus name="email" required/>
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
                                            <button type="submit" className="btn btn-success btn-block w-100 my-2">
                                                Login
                                            </button>
                                        </div>
                                        <div className="mt-4 text-center">
                                            Already have an account? <NavLink to="/signup">Sign up</NavLink>
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

export default Login;