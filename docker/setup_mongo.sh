#!/bin/sh
mongo mongodb://mongo:27017
use auth;
db.createCollection('users');
db.createCollection('whitelist');
