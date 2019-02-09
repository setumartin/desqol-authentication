import PropTypes from 'prop-types';
import React from 'react';

const localStyles = {
  wrapper: {
  },
  button: {
  }
};

const Logout = ({
  // fields
  username,
  password,
  // handlers
  handleLogout,
  // styles
  styles
}) => (
<div style={Object.assign({}, localStyles.wrapper, styles.wrapper)}>
  <button
    id="logout-button"
    type="button"
    style={Object.assign({}, localStyles.button, styles.button)}
    onClick={(e) => {
      handleLogout(e);
    }}
    >
    Logout
  </button>
</div>
);

Logout.propTypes = {
  // handlers
  handleLogout: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.shape({
    wrapper: PropTypes.object,
    button: PropTypes.object
  })
};

Logout.defaultProps = {
  // handlers
  handleLogout: (e) => {
    console.log('Handle logout...');
  },
  // styles
  styles: {}
};

export default Logout;
