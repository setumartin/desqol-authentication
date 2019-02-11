import PropTypes from 'prop-types';
import React from 'react';

import Registration from './Registration';
import Login from './Login';
import Recovery from './Recovery';

class LoginRegistrationRecovery extends React.Component {
  constructor(props) {
    super(props);

    this.updateState = this.updateState.bind(this);
    this.bubbleUpRegister = this.bubbleUpRegister.bind(this);
    this.bubbleUpLogin = this.bubbleUpLogin.bind(this);
    this.bubbleUpRecover = this.bubbleUpRecover.bind(this);

    this.state = {
      isLogin: this.props.isLogin,
      isRecoveringPassword: this.props.isRecoveringPassword,
      email: '',
      displayName: '',
      password: '',
      passwordConfirmation: ''
    };
  }

  updateState(key, value) {
    this.setState({ [key]: value });
  }
  
  bubbleUpRegister() {
    this.props.handleRegister({
      email: this.state.email,
      displayName: this.state.displayName,
      password: this.state.password,
      passwordConfirmation: this.state.passwordConfirmation
    });
  }

  bubbleUpLogin() {
    this.props.handleLogin({
      email: this.state.email,
      password: this.state.password
    });
  }

  bubbleUpRecover() {
    this.props.handleRecover({
      email: this.state.email
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
            email={this.state.email}
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
            email={this.state.email}
            displayName={this.state.displayName}
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
          email={this.state.email}
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

LoginRegistrationRecovery.propTypes = {
  // fields
  isLogin: PropTypes.bool,
  isRecoveringPassword: PropTypes.bool,
  // handlers
  handleRegister: PropTypes.func.isRequired,
  handleLogin: PropTypes.func.isRequired,
  handleRecover: PropTypes.func.isRequired,
  // styles
  styles: PropTypes.object.isRequired
};

LoginRegistrationRecovery.defaultProps = {
  // labels
  title: 'Welcome',
  // fields
  isLogin: false,
  isRecoveringPassword: false,
  // handlers
  handleRegister: (e) => {
    console.log('Handle register...');
  },
  handleLogin: (e) => {
    console.log('Handle login...');
  },
  handleRecover: (e) => {
    console.log('Handle recovery...');
  },
  // styles
  styles: {}
};

export default LoginRegistrationRecovery;
