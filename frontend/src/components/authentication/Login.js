import React from 'react';
import "../../style/auth.css";
import {staticURL} from "../../index";
import {NavLink} from "react-router-dom";

const Login = () => {
    return (
        <>
            <div className="limiter">
                <div className="container-login100">
                    <div className="wrap-login100">

                        <div className="login100-pic js-tilt">
                            <img src={staticURL + 'images/img-1.png'} alt="IMG"/>
                        </div>

                        <form className="login100-form validate-form">
                            <span className="login100-form-title"> Login  </span>

                            <div className="wrap-input100 validate-input" data-validate="Valid email is required: ex@abc.xyz">
                                <input className="input100" type="text" name="email" placeholder="Email"/>
                                <span className="focus-input100"/>
                            </div>

                            <div className="wrap-input100 validate-input" data-validate="Password is required">
                                <input className="input100" type="password" name="pass" placeholder="Password"/>
                                <span className="focus-input100"/>
                            </div>

                            <div className="container-login100-form-btn">
                                <button type="submit" className="login100-form-btn"> Login</button>
                            </div>

                            <div className="text-center p-t-12 mt-5">
                                <span className="txt1"> Forgot </span>
                                <NavLink className="txt2" to="#"> Password? </NavLink>
                            </div>

                        </form>
                    </div>
                </div>
            </div>
        </>
    );
};

export default Login;