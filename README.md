# `desqol-authentication`

This project provides an authentication service for the Erasmus+
DESQOL project.

The `desqol-authentication` server requires Python 3 and MongoDB.

## Setup

### Setup using Docker

```sh
docker-compose build
docker-compose up
```

The server is available on port 4000.

### Setup on macOS without Docker

To install MongoDB:

```sh
brew tap mongodb/brew
brew install mongodb-community
```

To install Python 3 and the required libraries:

```sh
brew install pyenv
pyenv install 3.9.0
eval "$(pyenv init -)"
pyenv global 3.9.0
pip3 install -r requirements.txt
```

To start MongoDB:

```sh
brew services start mongodb/brew/mongodb-community
```

To start the server:

```sh
python3 run_server.py
```

The server is available on port 4000.

### Setup on Windows without Docker

To install MongoDB:

* visit
  [here](https://www.mongodb.com/try/download/community?tck=docs_server)
* username & domain as described
  [here](https://stackoverflow.com/questions/52092528/mongodb-community-error-when-installing-service-as-local-or-domain-user)


To install Python 3 and the required libraries:

```cmd
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

To start MongoDB:

```sh
"C:\Program Files\MongoDB\Server\4.4\bin\mongo"
```

To start the server:

```sh
python3 run_server.py
```

The server is available on port 4000.

## Whitelisting a User

To add a user to the whitelist with email address `foo@bar.com` and a
gamify flag of `true`:

```sh
python run_whitelist.py add foo@bar.com true
```

To list the users on the whitelist:

```sh
python run_whitelist.py list
```

## Test the Server

You can run the automated tests using:

```sh
python run_test.py
```

## Usage

To check that the server is running:

```sh
# locally
http://localhost:4000/desqol-auth/api

# or on production (no 'api' suffix) 
curl https://jira.itcarlow.ie/desqol-auth/
```

To register a new user:

```sh
curl -X POST http://localhost:4000/desqol-auth/api/registration -d '{"email":"foo@bar.com", "password":"pass", "displayName":"Mr. Foo Bar"}'


# or on production (no 'api' suffix) 
curl https://jira.itcarlow.ie/desqol-auth/registration -d '{"email":"foo@bar.com", "password":"pass", "displayName":"Mr. Foo Bar"}'
```

You need to whitelist email addresses before you can register them.

To login:

```sh
curl -X POST http://localhost:4000/desqol-auth/api/login -d '{"email":"foo@bar.com", "password":"pass"}'


# or on production (no 'api' suffix) 
curl https://jira.itcarlow.ie/desqol-auth/login -d '{"email":"foo@bar.com", "password":"pass"}'
```

This will return a token. To get all information regarding the current
user:

```sh
curl -H "X-Token: YOUR_TOKEN_GOES_HERE" http://localhost:4000/desqol-auth/api/user

# or on production (no 'api' suffix) 
curl -H "X-Token:YOUR_TOKEN_GOES_HERE" https://jira.itcarlow.ie/desqol-auth/user
```

To logout:

```sh
curl -X POST -H "X-Token: YOUR_TOKEN_GOES_HERE" http://localhost:4000/desqol-auth/api/logout


# or on production (no 'api' suffix) 
curl -X POST -H "X-Token: YOUR_TOKEN_GOES_HERE" https://jira.itcarlow.ie/desqol-auth/logout
```

### Tokens

A token is 64 hexadecimal digits, e.g.,
`8442f1b13728312fce04429fe90ac15235bbf2902f613f937880fff0728d56bb`. A
token expires and is intended to be short-lived. A token expires two
hours after login, after a logout, or if there is another login from
the same user, generating a new token.

## add user scope in db, needed to download user event data

To grants user permission to download recordData table  with email address `foo@bar.com`:

```sh
python grant_scope.py add foo@bar.com
```

To list the users and their permissions:

```sh
python grant_scope.py list
