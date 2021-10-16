import React from 'react';
import {staticURL} from '../../index';

const NotFound = () => {
    return (
        <div className="content-center">
            <div className="d-flex justify-content-center align-items-center">
                <img src={staticURL + 'images/NotFound.svg'} className="img-responsive" alt="not-found" width="50%"/>
            </div>
            <h1 className="d-flex justify-content-center align-items-center mt-5">Not Found</h1>
        </div>
    );
};

export default NotFound;