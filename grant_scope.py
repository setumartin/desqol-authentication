import click
from json import loads
from motor.motor_tornado import MotorClient
from tornado.gen import coroutine
from tornado.ioloop import IOLoop

from api.conf import MONGODB_HOST, MONGODB_DBNAME, WHITELIST

@coroutine
def get_user(db, email):
  user = yield db.users.find_one({
    'email': email
  }, {})
  return user

@coroutine
def add_scope(db, email):
  if not isinstance(email, str):
    click.echo('The email address is not valid!')
    return

  user = yield get_user(db, email)
  if user is not None:
    yield db.users.update(
      {'email':email},
      {'$set':{'scope':"read:db"}
    })
    
    click.echo('SUCCESS: '  + email + ' now has read:db scope privilage')
  else:
    click.echo('ERROR: '  + email + ' is not registered')

@coroutine
def get_users(db):
  cur = db.users.find({}, {
    'email': 1,
    'scope': 1
  })
  docs = yield cur.to_list(length=None)
  print('There are ' + str(len(docs)) + ' users registered:')
  for doc in docs:
    click.echo(doc)

@click.group()
def cli():
    pass

@cli.command()
def list():
    db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]
    IOLoop.current().run_sync(lambda: get_users(db))

@cli.command()
@click.argument('email_address')
def add(email_address):
    db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]
    IOLoop.current().run_sync(lambda: add_scope(db, email_address))

if __name__ == '__main__':
    cli()
