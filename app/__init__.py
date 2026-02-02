from flask import Flask
from app.database.db import init_db
from app.config import Config

from app.auth.routes import auth_bp
from app.habits.routes import habits_bp
from app.entries.routes import entries_bp
from app.insights.routes import insights_bp
from app.scheduler import start_scheduler


def create_app(config_class=Config):
    app = Flask(__name__)

    # Load Config
    app.config.from_object(config_class)

    # Initial DB
    init_db(app)

    @app.get("/")
    def health_check():
        return {"status": "ok"}

    start_scheduler()
    app.register_blueprint(habits_bp)
    app.register_blueprint(entries_bp)
    app.register_blueprint(insights_bp)
    app.register_blueprint(auth_bp)

    return app
