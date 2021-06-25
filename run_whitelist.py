import click
from motor.motor_tornado import MotorClient
from tornado.gen import coroutine
from tornado.ioloop import IOLoop

from api.conf import MONGODB_HOST, MONGODB_DBNAME, WHITELIST


@coroutine
def get_user(db, email):
    user = yield db.whitelist.find_one({
        'email': email
    }, {})
    return user


@coroutine
def insert_user(db, email, gamify, using_gip, gip3days):
    if not isinstance(email, str):
        click.echo('The email address is not valid!')
        return
    if not isinstance(gamify, bool):
        click.echo('The gamify flag is not valid!')
        return
    if not isinstance(using_gip, bool):
        click.echo('The usingGIP flag is not valid!')
        return
    if not isinstance(gip3days, bool):
        click.echo('The gip3days flag is not valid!')
        return
    user = yield get_user(db, email)
    if user is None:
        yield db.whitelist.insert_one({
            'email': email,
            'gamify': gamify,
            'usingGIP': using_gip,
            'gip3PerWeek': gip3days
        })
        click.echo('SUCCESS: ' + email + ' is whitelisted!')
    else:
        click.echo('ERROR: ' + email + ' is already whitelisted!')


@coroutine
def remove_user(db, email):
    if not isinstance(email, str):
        click.echo('The email address is not valid!')
        return
    user = yield get_user(db, email)
    if user is None:
        click.echo('ERROR: ' + email + ' is not whitelisted!')
    else:
        yield db.whitelist.delete_one(user)
        click.echo('SUCCESS: ' + email + ' is no longer whitelisted!')


@coroutine
def get_users(db):
    cur = db.whitelist.find({}, {
        'email': 1,
        'gamify': 1,
        'usingGIP': 1,
        'gip3PerWeek': 1
    })
    docs = yield cur.to_list(length=None)
    print('There are ' + str(len(docs)) + ' users on the whitelist:')
    for doc in docs:
        click.echo(doc)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('email')
@click.option('--gamify/--no-gamify', default=True)
@click.option('--gip/--no-gip', default=True)
@click.option('--gip3days', default=False, is_flag=True)
def add(email, gamify, gip, gip3days):
    db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]
    IOLoop.current().run_sync(lambda: insert_user(db, email.lower(), gamify, gip, gip3days))


@cli.command()
@click.argument('email')
def remove(email):
    db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]
    IOLoop.current().run_sync(lambda: remove_user(db, email))


@cli.command()
def list():
    db = MotorClient(**MONGODB_HOST)[MONGODB_DBNAME]
    IOLoop.current().run_sync(lambda: get_users(db))


if __name__ == '__main__':
    cli()
