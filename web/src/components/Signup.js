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
  recoverPassword: {
  },
  button: {
  },
};

const Signup = ({
  // labels, etc.
  usernameCustomLabel,
  passwordCustomLabel,
  passwordConfirmationCustomLabel,
  goToLoginCustomLabel,
  submitSignupCustomLabel,
  // fields
  username,
  password,
  passwordConfirmation,
  // handlers
  handleShowLogin,
  handleSignup,
  handleChange,
  // styles
  styles
}) => (
  <section style={Object.assign({}, localStyles.wrapper, styles.wrapper)}>
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
      <input
        style={Object.assign({}, localStyles.input, styles.input)}
        type="password"
        id="password"
        name="password"
        placeholder={passwordCustomLabel}
        onChange={e => handleChange(e.target.name, e.target.value)}
        value={password}
      />
      <input
        style={Object.assign({}, localStyles.input, styles.input)}
        type="password"
        id="passwordConfirmation"
        name="passwordConfirmation"
        placeholder={passwordConfirmationCustomLabel}
        onChange={e => handleChange(e.target.name, e.target.value)}
        value={passwordConfirmation}
      />
    </div>
    <div style={Object.assign({}, localStyles.buttonsWrapper, styles.buttonsWrapper)}>
      <button
        id="login-button"
        type="button"
        style={Object.assign({}, localStyles.button, styles.button)}
        onClick={() => {
          handleShowLogin('isLogin', true);
        }}
      >
        {goToLoginCustomLabel}
      </button>
      <input
        id="submit-signup"
        type="submit"
        value={submitSignupCustomLabel}
        style={Object.assign({}, localStyles.button, styles.button)}
        onClick={handleSignup}
      />
    </div>
  </section>
);

Signup.propTypes = {
  // labels
  usernameCustomLabel: PropTypes.string.isRequired,
  passwordCustomLabel: PropTypes.string.isRequired,
  passwordConfirmationCustomLabel: PropTypes.string.isRequired,
  goToLoginCustomLabel: PropTypes.string.isRequired,
  submitSignupCustomLabel: PropTypes.string.isRequired,
  // fields
  username: PropTypes.string,
  password: PropTypes.string,
  passwordConfirmation: PropTypes.string,
  // handlers
  handleShowLogin: PropTypes.func.isRequired,
  handleSignup: PropTypes.func.isRequired,
  handleChange: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.shape({
    wrapper: PropTypes.object,
    inputWrapper: PropTypes.object,
    buttonsWrapper: PropTypes.object,
    input: PropTypes.object,
    recoverPassword: PropTypes.object,
    button: PropTypes.object,
  }),

};

Signup.defaultProps = {
  // labels
  usernameCustomLabel: 'Username',
  passwordCustomLabel: 'Password',
  passwordConfirmationCustomLabel: 'Confirm Password',
  goToLoginCustomLabel: 'Go to Login Instead',
  submitSignupCustomLabel: 'Signup',
  // handlers
  handleShowLogin: (e) => {
    console.log('HANDLE SHOW LOGIN...');
  },
  handleSignup: (e) => {
    console.log('HANDLE SIGNUP...');
  },
  handleChange: (e) => {
    console.log('HANDLE CHANGE...');
  },
  // styles
  styles: {},
};

export default Signup;
