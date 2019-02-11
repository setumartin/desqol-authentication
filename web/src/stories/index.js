import React from 'react';

import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';
import { linkTo } from '@storybook/addon-links';

import LoginRegistrationRecovery from '../components/LoginRegistrationRecovery';
import Logout from '../components/Logout';
import Profile from '../components/Profile';

storiesOf('LoginRegistrationRecovery', module)
  .add('with default behaviour', () => (
    <LoginRegistrationRecovery
      handleRegister={action('handleRegister')}
      handleLogin={action('handleLogin')}
      handleRecover={action('handleRecover')}
      />
  ));

storiesOf('Logout', module)
  .add('with default behaviour', () => (
    <Logout
      handleLogout={action('handleLogout')}
      />
  ));

storiesOf('Profile', module)
  .add('with default behaviour', () => (
    <Profile
      handleUpdate={action('handleUpdate')}
      />
  ));
