import React, { Component, Fragment } from 'react';
import './App.css';

import Signup from './components/Signup';
import Login from './components/Login';
import RecoverPassword from './components/RecoverPassword';

class App extends Component {
  render() {
    return (
      <Fragment>
        <Signup />
        <hr />
        <Login />
        <hr />
        <RecoverPassword />
      </Fragment>
    );
  }
}

export default App;
