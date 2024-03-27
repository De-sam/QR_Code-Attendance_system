from flask import Flask
from flask_restx import Api
from .auth.views import auth_namespace
from .config.config import config_dict
from .utils import db
from .models.users import User
from flask_migrate import Migrate
from .models.location import Location
from .models.company import Company

def create_app(config=config_dict['dev']):

    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    api.add_namespace(auth_namespace, path='/auth')

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'User': User,
            'Location': Location,

        }

    return app
