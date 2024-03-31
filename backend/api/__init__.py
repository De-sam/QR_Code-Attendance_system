from flask import Flask
from flask_restx import Api
from .routes.auth import auth_namespace
from .config.config import config_dict
from .utils import db
from .models import Admins, AttendanceReport, Roles, User, Location, Company, ClockingEvent, QRCode
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


def create_app(config=config_dict['dev']):

    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app, prefix='/api/v1')
    jwt = JWTManager(app)

    api.add_namespace(auth_namespace, path='/auth')

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            'admin': Admins,
            'attendance_report': AttendanceReport,
            'qrcode': QRCode,
            'user': User,
            'location': Location,
            'company': Company,
            'clocking_event': ClockingEvent,
            'role': Roles
        }

    return app
