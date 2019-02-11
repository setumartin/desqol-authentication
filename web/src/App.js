import React, { Component, Fragment } from 'react';
import './App.css';

import WiredLoginRegistrationRecovery from './components/WiredLoginRegistrationRecovery';
import WiredLogout from './components/WiredLogout';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {lastMessage: ''};

    this.handleRegisterSuccess = this.handleRegisterSuccess.bind(this);
    this.handleRegisterFailure = this.handleRegisterFailure.bind(this);
    this.handleLoginSuccess = this.handleLoginSuccess.bind(this);
    this.handleLoginFailure = this.handleLoginFailure.bind(this);
    this.handleRecoverSuccess = this.handleRecoverSuccess.bind(this);
    this.handleRecoverFailure = this.handleRecoverFailure.bind(this);
    this.handleLogoutSuccess = this.handleLogoutSuccess.bind(this);
    this.handleLogoutFailure = this.handleLogoutFailure.bind(this);
  }

  handleRegisterSuccess(e) {
    this.setState({
      lastMessage: 'Registration was successful!'
    });
    console.log(e);
  }

  handleRegisterFailure(e) {
    this.setState({
      lastMessage: 'Registration failed: ' + e['message']
    });
    console.log(e);
  }

  handleLoginSuccess(e) {
    this.setState({
      lastMessage: 'Login was successful!'
    });
    console.log(e);
  }

  handleLoginFailure(e) {
    this.setState({
      lastMessage: 'Login failed: ' + e['message']
    });
    console.log(e);
  }

  handleRecoverSuccess(e) {
    this.setState({
      lastMessage: 'Recovery was successful!'
    });
    console.log(e);
  }

  handleRecoverFailure(e) {
    this.setState({
      lastMessage: 'Recovery failed: ' + e['message']
    });
    console.log(e);
  }
  
  handleLogoutSuccess(e) {
    this.setState({
      lastMessage: 'Logout was successful!'
    });
    console.log(e);
  }

  handleLogoutFailure(e) {
    this.setState({
      lastMessage: 'Logout failed: ' + e['message']
    });
    console.log(e);
  }

  render() {
    return (
      <Fragment>
        <div>{this.state.lastMessage}</div>
        <WiredLoginRegistrationRecovery
          handleRegisterSuccess={this.handleRegisterSuccess}
          handleRegisterFailure={this.handleRegisterFailure}
          handleLoginSuccess={this.handleLoginSuccess}
          handleLoginFailure={this.handleLoginFailure}
          handleRecoverSuccess={this.handleRecoverSuccess}
          handleRecoverFailure={this.handleRecoverFailure}
        />
        <hr />
        <WiredLogout
          handleLogoutSuccess={this.handleLogoutSuccess}
          handleLogoutFailure={this.handleLogoutFailure}
        />
      </Fragment>
    );
  }
}

export default App;
