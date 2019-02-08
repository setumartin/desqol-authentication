# `auth-server`

The `auth-server` requires Python 3 and MongoDB.

To install the dependencies:

```sh
brew install mongodb
```

```sh
pip3 install tornado PyNaCl motor
```

To start MongoDB:

```sh
brew services start mongodb
```

To create the collection in MongoDB:
```
mongo mongodb://localhost:27017
> use auth;
> db.createCollection("users");
````

To start the server:

```sh
python3 run_server.py
```

The server is available on port 4000.
