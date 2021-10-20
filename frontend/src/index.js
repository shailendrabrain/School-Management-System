import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from "react-redux";
import {BrowserRouter} from "react-router-dom";
import App from './App';
import * as serviceWorkerRegistration from './services/serviceWorkerRegistration';
import reportWebVitals from './services/reportWebVitals';
import axios from 'axios';
import store from "./redux/store";

export const staticURL = "http://localhost:8000/static/";

axios.defaults.baseURL = 'http://localhost:8000/';
axios.defaults.headers.post['Content-Type'] = 'application/json';


ReactDOM.render(
    <React.StrictMode>
        <BrowserRouter>
            <Provider store={store}>
                <App/>
            </Provider>
        </BrowserRouter>
    </React.StrictMode>,
    document.getElementById('root')
);

serviceWorkerRegistration.unregister();
reportWebVitals();

