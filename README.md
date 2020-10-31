# `desqol-authentication`

This project provides an authentication service for the Erasmus+
DESQOL project. Please see the [Setup
Guide](https://docs.google.com/document/d/1G-NltB3Cx_ampDHYeNDEd-Neke99mR7RDLxE5EMnRKM)
for further details.

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

To drop any existing collections in MongoDB:

```
mongo mongodb://localhost:27017
> use auth;
> db.users.drop();
> db.whitelist.drop();
```

To start the server:

```sh
python3 run_server.py
```

The server is available on port 4000.

### Setup on Windows without Docker

To install MongoDB:

* visit [here](https://www.mongodb.com/try/download/community?tck=docs_server)
* username & domain as described [here](https://stackoverflow.com/questions/52092528/mongodb-community-error-when-installing-service-as-local-or-domain-user)


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

To drop any existing collections in MongoDB:

```
mongo mongodb://localhost:27017
> use auth;
> db.users.drop();
> db.whitelist.drop();
```

To start the server:

```sh
python3 run_server.py
```

The server is available on port 4000.

## Whitelisting

To add a user to the whitelist with email address `foo@bar.com` and a gamify flag of `true`:

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

You can interact with the server using:

```sh
curl http://localhost:4000/desqol-auth # this should return a welcome message
curl -X POST http://localhost:4000/desqol-auth/api/registration -d '{"email":"foo@bar.com", "password":"pass", "displayName":"myName"}'
curl -X POST http://localhost:4000/desqol-auth/api/login -d '{"email":"foo@bar.com", "password":"pass"}'
curl -X POST -H "X-Token: YOUR_TOKEN_GOES_HERE" http://localhost:4000/desqol-auth/api/logout

```

## add user scope in db, needed to download user event data

```
$ docker-compose up -d
$ docker-compose exec mongo sh

```

```
> use auth;
> db.users.update({email:"test_with_read_scope@user.com"},{$set:{scope:"read:db"}});

```
