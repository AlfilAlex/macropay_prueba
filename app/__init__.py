from flask import Flask
from .database.database import Directory

contact_directory = Directory("./app/database/fakedatabase.json")


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')
    with app.app_context():
        from .contacts.routes import contacts
        app.register_blueprint(contacts)

        return app
