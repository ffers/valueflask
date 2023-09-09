from flask import Blueprint, redirect, render_template, request, flash, redirect, url_for, jsonify, session
from models import Comment, Posts, Reply, Reply2, Users, Posts
from flask_login import login_required, current_user
from db import db
import sys

# from app.utils.auth import login_required

bp = Blueprint('User', __name__, template_folder='templates')

@bp.route("/blog/<username>")
@login_required
def author(username):
    user = Users.query.filter_by(username=username).first()

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('index'))

    posts = user.posts
    return render_template("user_templates/posts_author.html", user=current_user, posts=posts, username=username)

@bp.route("/blog/<username>/<int:id>")
@login_required
def author_post(username, id):
    user = Users.query.filter_by(username=username).first()
    id_post = Posts.query.filter_by(id=id).first()

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('index'))

    return render_template("user_templates/posts_author.html", user=current_user, posts=id_post, username=username)

