import PropTypes from 'prop-types';
import React from 'react';

const localStyles = {
  wrapper: {
  },
  inputWrapper: {
  },
  buttonsWrapper: {
  },
  input: {
  },
  button: {
  },
};

const RecoverPassword = ({
  // labels
  usernameCustomLabel,
  goToLoginCustomLabel,
  submitRecoverPasswordCustomLabel,
  // fields
  username,
  // handlers
  handleShowLogin,
  handleChange,
  handleRecoverPassword,
  // styles
  styles
}) => (
  <section
    style={Object.assign({}, localStyles.wrapper, styles.wrapper)}
  >
    <div style={Object.assign({}, localStyles.inputWrapper, styles.inputWrapper)}>
      <input
        style={Object.assign({}, localStyles.input, styles.input)}
        type="text"
        id="username"
        name="username"
        placeholder={usernameCustomLabel}
        onChange={e => handleChange(e.target.name, e.target.value)}
        value={username}
      />
    </div>
    <div style={Object.assign({}, localStyles.buttonsWrapper, styles.buttonsWrapper)}>
      <button
        id="login-button"
        type="button"
        style={Object.assign({}, localStyles.button, styles.button)}
        onClick={() => {
          handleShowLogin('isRecoveringPassword', false);
        }}
      >
        {goToLoginCustomLabel}
      </button>
      <input
        id="submit-recover-password"
        name="submit-recover-password"
        type="submit"
        value={submitRecoverPasswordCustomLabel}
        style={Object.assign({}, localStyles.button, styles.button)}
        onClick={handleRecoverPassword}
      />
    </div>
  </section>
);

RecoverPassword.propTypes = {
  // labels
  usernameCustomLabel: PropTypes.string.isRequired,
  goToLoginCustomLabel: PropTypes.string.isRequired,
  submitRecoverPasswordCustomLabel: PropTypes.string.isRequired,
  // fields
  username: PropTypes.string,
  // handlers
  handleShowLogin: PropTypes.func.isRequired,
  handleChange: PropTypes.func.isRequired,
  handleRecoverPassword: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.shape({
    wrapper: PropTypes.object,
    inputWrapper: PropTypes.object,
    buttonsWrapper: PropTypes.object,
    input: PropTypes.object,
    button: PropTypes.object,
  })
};

RecoverPassword.defaultProps = {
  // labels
  usernameCustomLabel: 'Username',
  goToLoginCustomLabel: 'Go to Login Instead',
  submitRecoverPasswordCustomLabel: 'Recover Password',
  // handlers
  handleShowLogin: (e) => {
    console.log('Handle show login...');
  },
  handleChange: (e) => {
    console.log('Handle change...');
  },
  handleRecoverPassword: (e) => {
    console.log('Handle recover password...');
  },
  // styles
  styles: {}
};

export default RecoverPassword;