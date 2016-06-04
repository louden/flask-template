import os

# *****************************
# Environment specific settings
# *****************************

# The settings below can (and should) be over-ruled by OS environment variable settings

# Flask settings                     # to create a new : import os; os.urandom(24)
SECRET_KEY = 'Change me please'
# PLEASE USE A DIFFERENT KEY FOR PRODUCTION ENVIRONMENTS!

DEBUG = True

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.sqlite'

# Flask-Mail settings
MAIL_USERNAME = 'email@example.com'
MAIL_PASSWORD = 'password'
MAIL_DEFAULT_SENDER = '"AppName" <noreply@example.com>'
MAIL_SERVER = 'MAIL_SERVER', 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False

ADMINS = [
    '"Admin One" <admin1@gmail.com>',
    ]

# STRIPE Settings
# DO NOT PUT YOUR KEYS HERE.  GET THEM FROM THE ENVIRONMENT
STRIPE_PUBLIC_KEY = os.environ['STRIPE_PUBLIC_KEY']
STRIPE_SECRET_KEY = os.environ['STRIPE_SECRET_KEY']