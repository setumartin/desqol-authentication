import PropTypes from 'prop-types';
import React from 'react';

import Registration from './Registration';
import Login from './Login';
import Recovery from './Recovery';

class Authentication extends React.Component {
  constructor(props) {
    super(props);

    this.updateState = this.updateState.bind(this);
    this.bubbleUpRegister = this.bubbleUpRegister.bind(this);
    this.bubbleUpLogin = this.bubbleUpLogin.bind(this);
    this.bubbleUpRecover = this.bubbleUpRecover.bind(this);

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
  
  bubbleUpRegister() {
    this.props.handleRegister({
      username: this.state.username,
      password: this.state.password,
      passwordConfirmation: this.state.passwordConfirmation
    });
  }

  bubbleUpLogin() {
    this.props.handleLogin({
      username: this.state.username,
      password: this.state.password
    });
  }

  bubbleUpRecover() {
    this.props.handleRecover({
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
            username={this.state.username}
            password={this.state.password}
            handleChange={this.updateState}
            handleLogin={this.bubbleUpLogin}
            handleShowRecovery={this.updateState}
            handleShowRegistration={this.updateState}
            styles={this.props.styles.login}
            />
        );
      } else if (!this.state.isLogin && !this.state.isRecoveringPassword) {
        return (
          <Registration
            username={this.state.username}
            password={this.state.password}
            passwordConfirmation={this.state.passwordConfirmation}
            handleChange={this.updateState}
            handleRegister={this.bubbleUpRegister}
            handleShowLogin={this.updateState}
            styles={this.props.styles.register}
            />
        );
      }
      return (
        <Recovery
          username={this.state.username}
          handleChange={this.updateState}
          handleRecover={this.bubbleUpRecover}
          handleShowLogin={this.updateState}
          styles={this.props.styles.recovery}
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
  // fields
  isLogin: PropTypes.bool,
  isRecoveringPassword: PropTypes.bool,
  // handlers
  handleRegister: PropTypes.func.isRequired,
  handleLogin: PropTypes.func.isRequired,
  handleRecover: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.shape({
    mainWrapper: PropTypes.object,
    mainTitle: PropTypes.object,
    flipper: PropTypes.object,
    register: PropTypes.shape({
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
    recovery: PropTypes.shape({
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
  handleLogin: (e) => {
    console.log('Handle login at the authentication component level...');
  },
  handleRegister: (e) => {
    console.log('Handle register at the authentication component level...');
  },
  handleRecover: (e) => {
    console.log('Handle recovery at the authentication component level...');
  },
  // styles
  styles: {}
};

export default Authentication;
