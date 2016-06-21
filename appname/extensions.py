from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_assets import Environment

# Setup flask cache
cache = Cache()

# Initialize flask assets
assets_env = Environment()

# Add the DebugToolbar
debug_toolbar = DebugToolbarExtension()
