import os
import tempfile
db_file = tempfile.NamedTemporaryFile()


class Config(object):
    """ Configuration details that are common to all environments """
    SECRET_KEY = os.urandom(24)

    # Application settings
    APP_NAME = "MyAppName"
    APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

    # Flask settings
    CSRF_ENABLED = True

    # Flask-User settings
    USER_APP_NAME = APP_NAME
    USER_ENABLE_CHANGE_PASSWORD = True  # Allow users to change their password
    USER_ENABLE_CHANGE_USERNAME = False  # Allow users to change their username
    USER_ENABLE_CONFIRM_EMAIL = False  # Force users to confirm their email
    USER_ENABLE_FORGOT_PASSWORD = True  # Allow users to reset their passwords
    USER_ENABLE_EMAIL = True  # Register with Email
    USER_ENABLE_REGISTRATION = True  # Allow new users to register
    USER_ENABLE_RETYPE_PASSWORD = True  # Prompt for `retype password` in:
    USER_ENABLE_USERNAME = False  # Register and Login with username
    USER_AFTER_LOGIN_ENDPOINT = 'main.restricted'
    USER_AFTER_LOGOUT_ENDPOINT = 'main.home'
    USER_LOGIN_TEMPLATE = 'flask_user/login_or_register.html'
    USER_REGISTER_TEMPLATE = 'flask_user/login_or_register.html'

    # Flask-Mail settings
    MAIL_USERNAME = 'email@example.com'
    MAIL_PASSWORD = 'password'
    MAIL_DEFAULT_SENDER = '"AppName" <noreply@example.com>'
    MAIL_SERVER = 'MAIL_SERVER', 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False

    # A PDL to send errors to
    SUPPORT_EMAILS = [
        '"My App Admins" <admin-pdl@example.com>'
    ]

    # Strip Keys (The live key should be used only on the production server)
    STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', 'XXX')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', 'XXX')


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///../appname.db'

    CACHE_TYPE = 'null'
    ASSETS_DEBUG = True


class TestConfig(Config):
    ENV = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_file.name
    SQLALCHEMY_ECHO = True

    CACHE_TYPE = 'null'
    WTF_CSRF_ENABLED = False


class ProdConfig(Config):
    ENV = 'prod'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../appname.db'

    CACHE_TYPE = 'simple'
