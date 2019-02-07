import React from 'react';

import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';
import { linkTo } from '@storybook/addon-links';

import Authentication from '../components/Authentication';

storiesOf('Authentication', module)
  .add('with default behaviour', () => (
    <Authentication
      handleSignup={action('handleSignup')}
      handleLogin={action('handleLogin')}
      handleRecoverPassword={action('handleRecoverPassword')}
      />
  ))
  .add('with Esperanto', () => (
    <Authentication
      title='Projekto Erasmus + DESQOL'
      usernameCustomLabel='Uzulnomo'
      passwordCustomLabel='Pasvorto'
      passwordConfirmationCustomLabel='Konfirmu pasvorton'
      recoverPasswordCustomLabel='Retrovu Pasvorton'
      goToSignupCustomLabel='Iru al Subskriba Instead'
      submitLoginCustomLabel='Ensaluti'
      goToLoginCustomLabel='Iru al Salutnomo Anstataŭe'
      submitSignupCustomLabel='Subskriba'
      submitRecoverPasswordCustomLabel='Retrovu Pasvorton'
      handleSignup={action('handleSignup')}
      handleLogin={action('handleLogin')}
      handleRecoverPassword={action('handleRecoverPassword')}
      />
  ));
