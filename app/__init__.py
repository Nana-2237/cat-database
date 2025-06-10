from flask import Flask
from connector.main import create_table
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    create_table()
    register_routes(app)
    return app
