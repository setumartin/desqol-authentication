import React from 'react';

import { storiesOf } from '@storybook/react';
import { action } from '@storybook/addon-actions';
import { linkTo } from '@storybook/addon-links';

import Authentication from '../components/Authentication';
import Logout from '../components/Logout';
import Profile from '../components/Profile';

storiesOf('Authentication', module)
  .add('with default behaviour', () => (
    <Authentication
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
