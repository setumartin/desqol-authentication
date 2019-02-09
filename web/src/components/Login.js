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
  }
};

const Login = ({
  // fields
  username,
  password,
  // handlers
  handleChange,
  handleLogin,
  handleShowRecovery,
  handleShowRegistration,
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
        placeholder="Username"
        onChange={e => handleChange(e.target.name, e.target.value)}
        value={username}
        />
        <input
          style={Object.assign({}, localStyles.input, styles.input)}
          type="password"
          id="password"
          name="password"
          placeholder="Password"
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
            handleShowRecovery('isRecoveringPassword', true);
          }}
          >
          Recover Lost Password
        </button>
      </div>
      <button
        id="signup-button"
        type="button"
        style={Object.assign({}, localStyles.button, styles.button)}
        onClick={() => {
          handleShowRegistration('isLogin', false);
        }}
        >
        Go to Registration Instead
      </button>
      <input
        id="submit-login"
        name="submit-login"
        value="Login"
        type="submit"
        style={Object.assign({}, localStyles.button, styles.button)}
        onClick={handleLogin}
        />
    </div>
  </section>
);

Login.propTypes = {
  // fields
  username: PropTypes.string,
  password: PropTypes.string,
  // handlers
  handleChange: PropTypes.func.isRequired,
  handleLogin: PropTypes.func.isRequired,
  handleShowRecovery: PropTypes.func.isRequired,
  handleShowRegistration: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.object.isRequired
};

Login.defaultProps = {
  // handlers
  handleChange: (e) => {
    console.log('Handle change...');
  },
  handleLogin: (e) => {
    console.log('Handle login...');
  },
  handleShowRecovery: (e) => {
    console.log('Handle show recovery...');
  },
  handleShowRegistration: (e) => {
    console.log('Handle show registration...');
  },
  // styles
  styles: {}
};

export default Login;
