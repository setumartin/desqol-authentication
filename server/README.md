# desqol-auth-server

To start MongoDB:

```
brew services start mongodb
```

To create the collection in MongoDB:

```
# mongo mongodb://localhost:27017
# > use desqol-auth;
# > db.createCollection("users");
```

To install dependencies:

```
pip3 install tornado
```

To start the server:

```
python3 run_server.py
```
