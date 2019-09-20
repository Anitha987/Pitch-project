from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
  app = Flask(__name__)

  # Initializing flask extensions
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
  bootstrap.init_app(app)
  db.init_app(app)
  login_manager.init_app(app)
