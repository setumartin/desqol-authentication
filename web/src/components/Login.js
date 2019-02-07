import PropTypes from 'prop-types';
import React from 'react';

const localStyles = {
  wrapper: {
  },
  buttonsWrapper: {
  },
  input: {
  },
  recoverPasswordWrapper: {
  },
  recoverPassword: {
  },
  button: {
  },
};

const Login = ({
  // labels
  usernameCustomLabel,
  passwordCustomLabel,
  recoverPasswordCustomLabel,
  goToSignupCustomLabel,
  submitLoginCustomLabel,
  // fields
  username,
  password,
  // handlers
  handleShowSignup,
  handleShowRecover,
  handleLogin,
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
    </div>
    <div style={Object.assign({}, localStyles.buttonsWrapper, styles.buttonsWrapper)}>
      <div
        style={Object.assign({}, localStyles.recoverPasswordWrapper, styles.recoverPasswordWrapper)}
      >
        <button
          id="recorver-password"
          type="button"
          style={Object.assign({}, localStyles.recoverPassword, styles.recoverPasswordButton)}
          onClick={() => {
            handleShowRecover('isRecoveringPassword', true);
          }}
        >
          {recoverPasswordCustomLabel}
        </button>
      </div>
      <button
        id="signup-button"
        type="button"
        style={Object.assign({}, localStyles.button, styles.button)}
        onClick={() => {
          handleShowSignup('isLogin', false);
        }}
      >
        {goToSignupCustomLabel}
      </button>
      <input
        id="submit-login"
        name="submit-login"
        value={submitLoginCustomLabel}
        type="submit"
        style={Object.assign({}, localStyles.button, styles.button)}
        onClick={handleLogin}
      />
    </div>
  </section>
);

Login.propTypes = {
  // labels
  usernameCustomLabel: PropTypes.string.isRequired,
  passwordCustomLabel: PropTypes.string.isRequired,
  recoverPasswordCustomLabel: PropTypes.string.isRequired,
  goToSignupCustomLabel: PropTypes.string.isRequired,
  submitLoginCustomLabel: PropTypes.string.isRequired,
  // fields
  username: PropTypes.string,
  password: PropTypes.string,
  // handlers
  handleShowSignup: PropTypes.func.isRequired,
  handleShowRecover: PropTypes.func.isRequired,
  handleLogin: PropTypes.func.isRequired,
  handleChange: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.shape({
    wrapper: PropTypes.object,
    inputWrapper: PropTypes.object,
    buttonsWrapper: PropTypes.object,
    input: PropTypes.object,
    recoverPasswordWrapper: PropTypes.object,
    recoverPasswordButton: PropTypes.object,
    button: PropTypes.object,
  })
};

Login.defaultProps = {
  // labels
  usernameCustomLabel: 'Username',
  passwordCustomLabel: 'Password',
  recoverPasswordCustomLabel: 'Recover Password',
  goToSignupCustomLabel: 'Go to Signup Instead',
  submitLoginCustomLabel: 'Login',
  // handlers
  handleShowSignup: (e) => {
    console.log('Handle show signup...');
  },
  handleShowRecover: (e) => {
    console.log('Handle show recover...');
  },
  handleLogin: (e) => {
    console.log('Handle login...');
  },
  handleChange: (e) => {
    console.log('Handle change...');
  },
  // styles
  styles: {}
};

export default Login;
