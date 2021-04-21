from flask import Flask
from flask_assets import Environment
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_login import LoginManager
from website.db import DB
from website.configs import DBConfig, cacheConfig
from website.utils.assets import bundles

bcrypt = Bcrypt()
cache = Cache(config=cacheConfig)
db = DB()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
assets = Environment ()

def create_app (config_class=DBConfig):
    app = Flask  (__name__)
    app.config.from_object(DBConfig)

    assets.init_app(app)
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app (app)
    login_manager.init_app (app)    
    
    from website.blueprints.main.routes import main
    from website.blueprints.users.routes import users
    from website.blueprints.api.routes import api
    from website.blueprints.errors.handlers import errors

    assets.register(bundles)
    app.register_blueprint (main)
    app.register_blueprint (users)
    app.register_blueprint (api, url_prefix="/api")
    app.register_blueprint (errors, url_prefix="/error")

    return app