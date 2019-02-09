import PropTypes from 'prop-types';
import React from 'react';

import Authentication from './Authentication';

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
    username: e['username'],
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
    username: e['username'],
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
    username: e['username']
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

const WiredAuthentication = ({
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
  <Authentication
    handleRegister={(e) => register(e, handleRegisterSuccess, handleRegisterFailure)}
    handleLogin={(e) => login(e, handleLoginSuccess, handleLoginFailure)}
    handleRecover={(e) => recover(e, handleRecoverSuccess, handleRecoverFailure)}
    />
);

WiredAuthentication.propTypes = {
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

WiredAuthentication.defaultProps = {
  // handlers
  handleRegisterSuccess: (e) => {
    console.log('Handle register success...');
    console.log(e);
  },
  handleRegisterFailure: (e) => {
    console.error('Handle register failure...');
    console.log(e);
  },
  handleLoginSuccess: (e) => {
    console.log('Handle login success...');
    console.log(e);
  },
  handleLoginFailure: (e) => {
    console.error('Handle login failure...');
    console.log(e);
  },
  handleRecoverSuccess: (e) => {
    console.log('Handle recover success...');
    console.log(e);
  },
  handleRecoverFailure: (e) => {
    console.error('Handle recover failure...');
    console.log(e);
  },
  // styles
  styles: {}
};

export default WiredAuthentication;
