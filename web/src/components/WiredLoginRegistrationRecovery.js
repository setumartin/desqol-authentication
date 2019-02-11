import PropTypes from 'prop-types';
import React from 'react';

import LoginRegistrationRecovery from './LoginRegistrationRecovery';

const API = 'http://localhost:4000/api';

const FETCH_CONFIG = {
  mode: 'cors',
  cache: 'no-cache',
  headers: {
    'Content-Type': 'application/json'
  }
};

const register = (e, success, failure) => {
  const body = {
    email: e['email'],
    displayName: e['displayName'],
    password: e['password']
  };
  fetch(API + '/registration', Object.assign(FETCH_CONFIG, {
    method: 'POST',
    body: JSON.stringify(body),
  }))
  .then(response => {
    if (response.status === 200) {
      response.json().then(success);
    } else {
      response.json().then(failure);
    }
  })
  .catch(error => failure(error));
};

const login = (e, success, failure) => {
  const body = {
    email: e['email'],
    password: e['password']
  };
  fetch(API + '/login', Object.assign(FETCH_CONFIG, {
    method: 'POST',
    body: JSON.stringify(body),
  }))
  .then(response => {
    if (response.status === 200) {
      response.json().then(success);
    } else {
      response.json().then(failure);
    }
  })
  .catch(error => failure(error));
};

const recover = (e, success, failure) => {
  const body = {
    email: e['email']
  };
  fetch(API + '/password/reset', Object.assign(FETCH_CONFIG, {
    method: 'POST',
    body: JSON.stringify(body),
  }))
  .then(response => {
    if (response.status === 200) {
      response.json().then(success);
    } else {
      response.json().then(failure);
    }
  })
  .catch(error => failure(error));
};

const WiredLoginRegistrationRecovery = ({
  // handlers
  handleRegisterSuccess,
  handleRegisterFailure,
  handleLoginSuccess,
  handleLoginFailure,
  handleRecoverSuccess,
  handleRecoverFailure,
  // styles
  styles
}) => (
  <LoginRegistrationRecovery
    handleRegister={(e) => register(e, handleRegisterSuccess, handleRegisterFailure)}
    handleLogin={(e) => login(e, handleLoginSuccess, handleLoginFailure)}
    handleRecover={(e) => recover(e, handleRecoverSuccess, handleRecoverFailure)}
    />
);

WiredLoginRegistrationRecovery.propTypes = {
  // handlers
  handleRegisterSuccess: PropTypes.func.isRequired,
  handleRegisterFailure: PropTypes.func.isRequired,
  handleLoginSuccess: PropTypes.func.isRequired,
  handleLoginFailure: PropTypes.func.isRequired,
  handleRecoverSuccess: PropTypes.func.isRequired,
  handleRecoverFailure: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.object
};

WiredLoginRegistrationRecovery.defaultProps = {
  styles: {}
};

export default WiredLoginRegistrationRecovery;
