import functools

from flask import (
    session, Blueprint, g, redirect, render_template, request, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash
from todo_app.db import get_db

todo_bp = Blueprint("todo", __name__, url_prefix="/")

# routing to homepage
@todo_bp.route("/", methods=["GET", "POST"])
def todo():
    return render_template("home/index.html")