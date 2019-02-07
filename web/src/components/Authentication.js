import PropTypes from 'prop-types';
import React from 'react';

import Login from './Login';
import Signup from './Signup';
import RecoverPassword from './RecoverPassword';

class Authentication extends React.Component {
  constructor(props) {
    super(props);

    this.updateState = this.updateState.bind(this);
    this.bubbleUpLogin = this.bubbleUpLogin.bind(this);
    this.bubbleUpSignup = this.bubbleUpSignup.bind(this);
    this.bubbleUpRecoverPassword = this.bubbleUpRecoverPassword.bind(this);

    this.state = {
      isLogin: this.props.isLogin,
      isRecoveringPassword: this.props.isRecoveringPassword,
      username: '',
      password: '',
      passwordConfirmation: ''
    };
  }

  updateState(key, value) {
    this.setState({ [key]: value });
  }

  bubbleUpLogin() {
    this.props.handleLogin({
      username: this.state.username,
      password: this.state.password
    });
  }

  bubbleUpSignup() {
    this.props.handleSignup({
      username: this.state.username,
      password: this.state.password,
      passwordConfirmation: this.state.passwordConfirmation
    });
  }

  bubbleUpRecoverPassword() {
    this.props.handleRecoverPassword({
      username: this.state.username
    });
  }

  render() {
    const styles = {
      wrapper: {
      },
      title: {
      },
      flipper: {
      }
    };
    const showCard = () => {
      if (this.state.isLogin && !this.state.isRecoveringPassword) {
        return (
          <Login
            usernameCustomLabel={this.props.usernameCustomLabel}
            passwordCustomLabel={this.props.passwordCustomLabel}
            recoverPasswordCustomLabel={this.props.recoverPasswordCustomLabel}
            goToSignupCustomLabel={this.props.goToSignupCustomLabel}
            submitLoginCustomLabel={this.props.submitLoginCustomLabel}
            username={this.state.username}
            password={this.state.password}
            handleShowSignup={this.updateState}
            handleShowRecover={this.updateState}
            handleLogin={this.bubbleUpLogin}
            handleChange={this.updateState}
            styles={this.props.styles.login}
            />
        );
      } else if (!this.state.isLogin && !this.state.isRecoveringPassword) {
        return (
          <Signup
            usernameCustomLabel={this.props.usernameCustomLabel}
            passwordCustomLabel={this.props.passwordCustomLabel}
            passwordConfirmationCustomLabel={this.props.passwordConfirmationCustomLabel}
            goToLoginCustomLabel={this.props.goToLoginCustomLabel}
            submitSignupCustomLabel={this.props.submitSignupCustomLabel}
            username={this.state.username}
            password={this.state.password}
            passwordConfirmation={this.state.passwordConfirmation}
            handleShowLogin={this.updateState}
            handleSignup={this.bubbleUpSignup}
            handleChange={this.updateState}
            styles={this.props.styles.signup}
            />
        );
      }
      return (
        <RecoverPassword
          usernameCustomLabel={this.props.usernameCustomLabel}
          goToLoginCustomLabel={this.props.goToLoginCustomLabel}
          submitRecoverPasswordCustomLabel={this.props.submitRecoverPasswordCustomLabel}
          username={this.state.username}
          handleShowLogin={this.updateState}
          handleRecoverPassword={this.bubbleUpRecoverPassword}
          handleChange={this.updateState}
          styles={this.props.styles.recoverPassword}
          />
      );
    };
    return (
      <section
        id="main-wrapper"
        style={Object.assign(styles.wrapper, this.props.styles.mainWrapper)}
        >
        <h1 style={Object.assign(styles.title, this.props.styles.mainTitle)}>{this.props.title}</h1>
        <div style={Object.assign(styles.flipper, this.props.styles.flipper)}>{showCard()}</div>
      </section>
    );
  }
}

Authentication.propTypes = {
  // labels
  title: PropTypes.string,
  usernameCustomLabel: PropTypes.string,
  passwordCustomLabel: PropTypes.string,
  passwordConfirmationCustomLabel: PropTypes.string,
  recoverPasswordCustomLabel: PropTypes.string,
  goToSignupCustomLabel: PropTypes.string,
  submitLoginCustomLabel: PropTypes.string,
  goToLoginCustomLabel: PropTypes.string,
  submitSignupCustomLabel: PropTypes.string,
  submitRecoverPasswordCustomLabel: PropTypes.string,
  // fields
  isLogin: PropTypes.bool,
  isRecoveringPassword: PropTypes.bool,
  // handlers
  handleSignup: PropTypes.func.isRequired,
  handleLogin: PropTypes.func.isRequired,
  handleRecoverPassword: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.shape({
    mainWrapper: PropTypes.object,
    mainTitle: PropTypes.object,
    flipper: PropTypes.object,
    signup: PropTypes.shape({
      wrapper: PropTypes.object,
      inputWrapper: PropTypes.object,
      buttonsWrapper: PropTypes.object,
      input: PropTypes.object,
      recoverPassword: PropTypes.object,
      button: PropTypes.object
    }),
    login: PropTypes.shape({
      wrapper: PropTypes.object,
      inputWrapper: PropTypes.object,
      buttonsWrapper: PropTypes.object,
      input: PropTypes.object,
      recoverPasswordWrapper: PropTypes.object,
      recoverPasswordButton: PropTypes.object,
      button: PropTypes.object
    }),
    recoverPassword: PropTypes.shape({
      wrapper: PropTypes.object,
      inputWrapper: PropTypes.object,
      buttonsWrapper: PropTypes.object,
      input: PropTypes.object,
      button: PropTypes.object
    }),
  })
};

Authentication.defaultProps = {
  // labels
  title: 'Erasmus+ DESQOL Project',
  // fields
  isLogin: true,
  isRecoveringPassword: false,
  // handlers
  handleSignup: (e) => {
    console.log('Handle signup...');
  },
  handleLogin: (e) => {
    console.log('Handle login...');
  },
  handleRecoverPassword: (e) => {
    console.log('Handle recover password...');
  },
  // styles
  styles: {}
};

export default Authentication;
