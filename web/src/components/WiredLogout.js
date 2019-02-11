import PropTypes from 'prop-types';
import React from 'react';

import Logout from './Logout';

const API = 'http://localhost:4000/api';

const FETCH_CONFIG = {
  mode: 'cors',
  cache: 'no-cache',
  headers: {
    'Content-Type': 'application/json'
  }
};

const logout = (e, success, failure) => {
  fetch(API + '/logout', Object.assign(FETCH_CONFIG, {
    method: 'POST',
    headers: Object.assign(FETCH_CONFIG['headers'], {
      'X-Token': sessionStorage.getItem('token')
    })
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

const WiredLogout = ({
  // handlers
  handleLogoutSuccess,
  handleLogoutFailure,
  // styles
  styles
}) => (
  <Logout
    handleLogout={(e) => logout(e, handleLogoutSuccess, handleLogoutFailure)}
    />
);

WiredLogout.propTypes = {
  // handlers
  handleLogoutSuccess: PropTypes.func.isRequired,
  handleLogoutFailure: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.object
};

WiredLogout.defaultProps = {
  styles: {}
};

export default WiredLogout;
