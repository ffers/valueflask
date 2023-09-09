#server.py

from flask import Flask, render_template, url_for, request, redirect
from flask_login import current_user, LoginManager
from flask_migrate import Migrate
from datetime import datetime
from db import db
from routes import Blog, Auth, Comment, User_post, Bot


app = Flask(__name__)
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = "helloworld"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True

db.init_app(app)

app.register_blueprint(Blog)
app.register_blueprint(Auth)
app.register_blueprint(Comment)
app.register_blueprint(User_post)
app.register_blueprint(Bot)

from models import Users
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print(request.json)
        return {'ok':True}
    return render_template('index.html', user=current_user)


if __name__ == "__main__":
    app.run(debug=True)

