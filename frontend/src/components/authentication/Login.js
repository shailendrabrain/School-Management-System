import React from 'react';
import "../../style/auth.css";
import {staticURL} from "../../index";
import {useForm} from "react-hook-form";
import {NavLink} from "react-router-dom";

const Login = () => {

    const {register, handleSubmit, formState: {errors}} = useForm();
    const onSubmit = data => console.log(data);

    return (
        <>
            <div className="limiter">
                <div className="container-login100">
                    <div className="wrap-login100">

                        <div className="login100-pic js-tilt">
                            <img src={staticURL + 'images/img-1.png'} alt="IMG"/>
                        </div>

                        <form className="login100-form" onSubmit={handleSubmit(onSubmit)}>
                            <span className="login100-form-title"> Login  </span>

                            <div className="wrap-input100">
                                <input
                                    className="input100"
                                    type="text"
                                    placeholder="Email"
                                    {...register('email', {required: {value: true, message: "email is required"}})}
                                />
                                <span className="focus-input100 invalid-feedback"/>
                                <div className="text-danger w-100 text-center">{errors.email && errors.email.message}</div>
                            </div>

                            <div className="wrap-input100">
                                <input
                                    className="input100"
                                    type="password"
                                    placeholder="Password"
                                    {...register('password', {required: {value: true, message: "password is required"}})}
                                />
                                <span className="focus-input100"/>
                                <div className="text-danger w-100 text-center">{errors.password && errors.password.message}</div>
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