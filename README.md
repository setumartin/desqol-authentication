# `desqol-authentication`

The `desqol-authentication` server requires Python 3 and MongoDB.

To install the dependencies:

```sh
brew tap mongodb/brew
brew install mongodb-community
```

```sh
pip3 install tornado PyNaCl motor
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
