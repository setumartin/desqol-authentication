import React, { Component, Fragment } from 'react';
import './App.css';

import Signup from './components/Signup';
import Login from './components/Login';

class App extends Component {
  render() {
    return (
      <Fragment>
        <Signup />
        <hr />
        <Login />
      </Fragment>
    );
  }
}

export default App;
