import React from 'react';
import Header from "./components/layout/Header";
import {Route, Switch} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import './style/style.css'
import Home from "./components/home/Home";
import Login from "./components/authentication/Login";
import NotFound from "./components/authentication/NotFound";


const App = () =>
    <>
        <Header/>
        <Switch>
            <Route exact path="/" component={Home}/>
            <Route path="/login" component={Login}/>
            <Route component={NotFound}/>
        </Switch>
    </>


export default App;
