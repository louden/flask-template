#!/usr/bin/env python

import os

from datetime import datetime
from flask.ext.script import Manager, Server
from flask.ext.script.commands import ShowUrls, Clean
from appname import create_app
from appname.database import db
from appname.main.models import User, Role

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('APPNAME_ENV', 'dev')
app = create_app('appname.settings.{}Config'.format(env.capitalize()))

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """

    return dict(app=app, db=db, User=User)


@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """

    db.create_all()


@manager.command
def seeddb():
    """ Seeds the database with a user with the user role and one with the
        admin role
    """

    # Create all tables
    db.create_all()

    # Adding roles
    admin_role = find_or_create_role('admin', u'Admin')

    # Add users
    find_or_create_user(u'Admin', u'Example', u'admin@example.com',
                        'Password1', admin_role)
    find_or_create_user(u'User', u'Example', u'user@example.com',
                        'Password1')

    # Save to DB
    db.session.commit()


def find_or_create_role(name, label):
    """ Find existing role or create new role; used by seeddb """
    role = Role.query.filter(Role.name == name).first()
    if not role:
        role = Role(name=name, label=label)
        db.session.add(role)
    return role


def find_or_create_user(first_name, last_name, email, password, role=None):
    """ Find existing user or create new user; used by seeddb """
    user = User.query.filter(User.email == email).first()
    if not user:
        user = User(email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=app.user_manager.hash_password(password),
                    active=True,
                    confirmed_at=datetime.utcnow())
        if role:
            user.roles.append(role)
        db.session.add(user)
    return user

if __name__ == "__main__":
    manager.run()
