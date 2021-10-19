import {createStore, combineReducers} from 'redux';
import isAuthReducer from "./auth/authReducer";

const store = createStore(combineReducers({
        auth: isAuthReducer
    }),
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
)

export default store;