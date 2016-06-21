#! ../env/bin/python

from flask import (Flask,
                   render_template)
from webassets.loaders import PythonLoader as PythonAssetsLoader

from flask_user import (UserManager,
                        SQLAlchemyAdapter)

from appname import assets
from appname.database import db
from appname.main.forms import AppRegisterForm
from appname.main.models import User
from appname.main.views import (main,
                                user_profile)

from appname.extensions import (
    cache,
    assets_env,
    debug_toolbar
)


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/

    Arguments:
        object_name: the python path of the config object,
                     e.g. appname.settings.ProdConfig
    """

    app = Flask(__name__)

    app.config.from_object(object_name)

    # initialize the cache
    cache.init_app(app)

    # initialize the debug tool bar
    debug_toolbar.init_app(app)

    # initialize SQLAlchemy
    db.init_app(app)

    # initialize Flask-User
    db_adapter = SQLAlchemyAdapter(db, User)
    UserManager(db_adapter,
                app,
                register_form=AppRegisterForm,
                user_profile_view_function=user_profile)

    # Import and register the different asset bundles
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    # register our blueprints
    app.register_blueprint(main)

    # Register Error Handlers
    register_errorhandlers(app)

    return app


def register_errorhandlers(app):
    """Register error handlers."""
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
