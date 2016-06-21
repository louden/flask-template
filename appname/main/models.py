from flask_user import UserMixin
from appname.database import db


class User(db.Model, UserMixin):
    """ Definition of the User Model

    This class requires the use of the UserMixin from Flask-User.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User authentication information (required for Flask-User)
    email = db.Column(db.Unicode(255), nullable=False, server_default=u'',
                      unique=True)
    confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default='')
    reset_password_token = db.Column(db.String(100), nullable=False,
                                     server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')

    # User information
    active = db.Column('is_active', db.Boolean(),
                       nullable=False, server_default='0')
    first_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    last_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')

    # Relationships
    roles = db.relationship('Role', secondary='users_roles',
                            backref=db.backref('users', lazy='dynamic'))


class Role(db.Model):
    """ Definition of the Roles Model """
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)

    # for @roles_accepted()
    name = db.Column(db.String(50), nullable=False,
                     server_default=u'', unique=True)

    # for display purposes
    label = db.Column(db.Unicode(255), server_default=u'')


class UsersRoles(db.Model):
    """ Definition of the UserRoles Association Model """
    __tablename__ = 'users_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id',
                                                    ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id',
                                                    ondelete='CASCADE'))