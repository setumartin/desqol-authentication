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
  email,
  // handlers
  handleChange,
  handleRecover,
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
        id="email"
        name="email"
        placeholder="email"
        onChange={e => handleChange(e.target.name, e.target.value)}
        value={email}
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
        onClick={handleRecover}
        />
    </div>
  </section>
);

Recovery.propTypes = {
  // fields
  email: PropTypes.string,
  // handlers
  handleChange: PropTypes.func.isRequired,
  handleRecover: PropTypes.func.isRequired,
  handleShowLogin: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.object.isRequired
};

Recovery.defaultProps = {
  styles: {}
};

export default Recovery;
