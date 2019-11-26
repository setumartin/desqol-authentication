# `desqol-authentication`

The `desqol-authentication` server requires Python 3 and MongoDB.

## Setup using Docker

Edit `api/conf.py` and change `localhost` to `mongo`.

Then:

```sh
docker-compose build
docker-compose up
```

The server is available on port 4000.

## Setup without Docker on macOS

To install MongoDB:

```sh
brew tap mongodb/brew
brew install mongodb-community
```

To install Python 3 and the required libraries:

```sh
brew install python3
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
curl localhost:4000/desqol-auth # this should return a welcome message
curl -X POST localhost:4000/desqol-auth/api/login -d '{"email":"foo@bar.com", "password":"pass"}'
```
