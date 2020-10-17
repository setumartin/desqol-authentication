# `desqol-authentication`

This project provides an authentication service for the Erasmus+
DESQOL project. Please see the [Setup
Guide](https://docs.google.com/document/d/1G-NltB3Cx_ampDHYeNDEd-Neke99mR7RDLxE5EMnRKM)
for further details.

The `desqol-authentication` server requires Python 3 and MongoDB.

## Setup using Docker

```sh
docker-compose build
docker-compose up
```

The server is available on port 4000.

## Setup on macOS without Docker

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

To create the collection in MongoDB:

```
mongo mongodb://localhost:27017
> use auth;
> db.users.drop();
> db.createCollection('users');
````

To start the server:

```sh
python3 run_server.py
```

The server is available on port 4000.

## Test the Server

You can test the server using:

```sh
curl http://localhost:4000/desqol-auth # this should return a welcome message
curl -X POST http://localhost:4000/desqol-auth/api/login -d '{"email":"foo@bar.com", "password":"pass"}'
```
