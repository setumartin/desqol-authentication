import PropTypes from 'prop-types';
import React from 'react';

const localStyles = {
  wrapper: {
  },
  buttonsWrapper: {
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
  <section style={Object.assign({}, localStyles.wrapper, styles.wrapper)}>
    <div style={Object.assign({}, localStyles.buttonsWrapper, styles.buttonsWrapper)}>
      <input
        id="submit-logout"
        type="submit"
        value="Logout"
        style={Object.assign({}, localStyles.button, styles.button)}
        onClick={handleLogout}
        />
    </div>
  </section>
);

Logout.propTypes = {
  // handlers
  handleLogout: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.object.isRequired
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
