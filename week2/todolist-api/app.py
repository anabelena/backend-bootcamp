# import Flask from "flask"
from flask import Flask, jsonify, request  
from app.routes.tasks import task_route
from app.db import db
from app.config import Config

# instancia de Flask 
app = Flask(__name__) #__name__   modulo actual

app.config.from_object(Config)

app.register_blueprint(task_route)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True) #Por cada cambio se hace un reload
