from flask import Flask
from app.database.db import init_db
from app.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)

    # טעינת קונפיג לאפליקציה
    app.config.from_object(config_class)

    # אתחול הדאטה־בייס (Mongo)
    init_db(app)

    @app.get("/")
    def health_check():
        return {"status": "ok"}

    return app
