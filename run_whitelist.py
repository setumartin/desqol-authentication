import click
from motor.motor_tornado import MotorClient
from tornado.gen import coroutine
from tornado.ioloop import IOLoop

from api.conf import MONGODB_HOST, MONGODB_DBNAME, WHITELIST

@coroutine
def get_user(db, email):
  user = yield db.whitelist.find_one({'email': email})
  return user

@coroutine
def insert_user(db, email, gamify):
  user = yield get_user(db, email)
  if user is None:
    yield db.whitelist.insert_one({
        'email': email,
        'gamify': gamify
    })
    click.echo('SUCCESS: '  + email + ' is whitelisted!')
  else:
    click.echo('ERROR: '  + email + ' is already whitelisted!')
    
@coroutine
def get_users(db):
  cur = db.whitelist.find()
  docs = yield cur.to_list(length=None)
  for doc in docs:
    click.echo(doc)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('email')
@click.argument('gamify')
def add(email, gamify):
    db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]
    IOLoop.current().run_sync(lambda: insert_user(db, email, gamify))

@cli.command()
def list():
    db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]
    IOLoop.current().run_sync(lambda: get_users(db))  

if __name__ == '__main__':
    cli()