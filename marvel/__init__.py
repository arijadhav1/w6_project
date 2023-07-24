from flask import Flask
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth
from config import Config
from .helpers import JSONEncoder

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import db as root_db, login_manager, ma 

from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(auth)

app.config.from_object(Config)
root_db.init_app(app)
migrate = Migrate(app, root_db)

ma.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.signin'
app.json_encoder = JSONEncoder
CORS(app)

