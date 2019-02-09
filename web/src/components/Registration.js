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
  }
};

const Registration = ({
  // fields
  username,
  displayName,
  password,
  passwordConfirmation,
  // handlers
  handleChange,
  handleRegister,
  handleShowLogin,
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
        type="text"
        id="displayName"
        name="displayName"
        placeholder="Display Name"
        onChange={e => handleChange(e.target.name, e.target.value)}
        value={displayName}
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
      <input
        style={Object.assign({}, localStyles.input, styles.input)}
        type="password"
        id="passwordConfirmation"
        name="passwordConfirmation"
        placeholder="Confirm Password"
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
        Go to Login Instead
      </button>
      <input
        id="submit-registration"
        type="submit"
        value="Register"
        style={Object.assign({}, localStyles.button, styles.button)}
        onClick={handleRegister}
        />
    </div>
  </section>
);

Registration.propTypes = {
  // fields
  username: PropTypes.string,
  displayName: PropTypes.string,
  password: PropTypes.string,
  passwordConfirmation: PropTypes.string,
  // handlers
  handleChange: PropTypes.func.isRequired,
  handleRegister: PropTypes.func.isRequired,
  handleShowLogin: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.shape({
    wrapper: PropTypes.object,
    inputWrapper: PropTypes.object,
    buttonsWrapper: PropTypes.object,
    input: PropTypes.object,
    recoverPassword: PropTypes.object,
    button: PropTypes.object,
  })
};

Registration.defaultProps = {
  // handlers
  handleChange: (e) => {
    console.log('Handle change...');
  },
  handleRegister: (e) => {
    console.log('Handle register...');
  },
  handleShowLogin: (e) => {
    console.log('Handle show login...');
  },
  // styles
  styles: {}
};

export default Registration;
