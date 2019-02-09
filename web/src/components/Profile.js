import PropTypes from 'prop-types';
import React from 'react';

const localStyles = {
  wrapper: {
  },
  title: {
  },
  paragraphWrapper: {
  },
  p: {
  },
  buttonsWrapper: {
  },
  button: {
  }
};

const Profile = ({
  title,
  // fields
  displayName,
  // handlers
  handleChange,
  handleUpdate,
  // styles
  styles
}) => (
  <section style={Object.assign({}, localStyles.wrapper, styles.wrapper)}>
    <h1 style={Object.assign(localStyles.title, styles.title)}>{title}</h1>
    <div style={Object.assign({}, localStyles.paragraphWrapper, styles.paragraphWrapper)}>
      <p style={Object.assign({}, localStyles.p, styles.p)}>
        Display Name: &nbsp;
        <input
          style={Object.assign({}, localStyles.input, styles.input)}
          type="text"
          id="displayName"
          name="displayName"
          placeholder="Display Name"
          onChange={e => handleChange(e.target.name, e.target.value)}
          value={displayName}
          />
      </p>
    </div>
    <div style={Object.assign({}, localStyles.buttonsWrapper, styles.buttonsWrapper)}>
      <input
        id="submit-update"
        type="submit"
        value="Update Profile"
        style={Object.assign({}, localStyles.button, styles.button)}
        onClick={handleUpdate}
        />
    </div>
  </section>
);

Profile.propTypes = {
  title: PropTypes.string.isRequired,
  // handlers
  handleChange: PropTypes.func.isRequired,
  handleUpdate: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.shape({
    wrapper: PropTypes.object,
    title: PropTypes.object,
    paragraphWrapper: PropTypes.object,
    p: PropTypes.object,
    buttonsWrapper: PropTypes.object,
    button: PropTypes.object,
  })
};

Profile.defaultProps = {
  title: 'Profile',
  // handlers
  handleChange: (e) => {
    console.log('Handle change...');
  },
  handleUpdate: (e) => {
    console.log('Handle update...');
  },
  // styles
  styles: {}
};

export default Profile;
