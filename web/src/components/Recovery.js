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
  }
};

const Recovery = ({
  // fields
  username,
  // handlers
  handleChange,
  handleRecoverPassword,
  handleShowLogin,
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
        placeholder="Username"
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
        Go to Login Instead
      </button>
      <input
        id="submit-recover-password"
        name="submit-recover-password"
        type="submit"
        value="Recover Password"
        style={Object.assign({}, localStyles.button, styles.button)}
        onClick={handleRecoverPassword}
        />
    </div>
  </section>
);

Recovery.propTypes = {
  // fields
  username: PropTypes.string,
  // handlers
  handleChange: PropTypes.func.isRequired,
  handleRecoverPassword: PropTypes.func.isRequired,
  handleShowLogin: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.shape({
    wrapper: PropTypes.object,
    inputWrapper: PropTypes.object,
    buttonsWrapper: PropTypes.object,
    input: PropTypes.object,
    button: PropTypes.object
  })
};

Recovery.defaultProps = {
  // handlers
  handleChange: (e) => {
    console.log('Handle change...');
  },
  handleRecoverPassword: (e) => {
    console.log('Handle recover password...');
  },
  handleShowLogin: (e) => {
    console.log('Handle show login...');
  },
  // styles
  styles: {}
};

export default Recovery;
