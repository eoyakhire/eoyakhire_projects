import os
import json
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# Configure CS50 Library to use SQLite database
#create our own database
db = SQL("sqlite:///finance.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/journal")
def journal():
    return render_template("journal.html")

@app.route("/visionboard")
def visionboard():
    return render_template("visionboard.html")

@app.route("/generate")
def generate():
    return render_template("generate.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/community")
def community():
    return render_template("community.html")

@app.route("/homepage")
@login_required
def homepage():
    # Render homepage once the user is logged in
    # this will have the user's profile pic, logout oopition and their session
    # every login required page will be extended from this template
    return render_template("homepage.html")

@app.route("/entry", methods=['GET', 'POST'])
@login_required
def diary():

    user_id = session["user_id"]

    if request.method == "POST":
        diary = request.form.get("diary")
        db.execute("INSERT INTO diary (entry) VALUES (?)", diary)
        return render_template("entries.html")
    else:
        db.execute("SELECT entry FROM diary JOIN users ON diary.user_id = users.id WHERE id = ?", user_id)
        return render_template("diary.html")

# @app.route("/generateAI", methods=['GET', 'POST'])
# @login_required
# def generateAI():


# @app.route("/visiobBoard", methods=['GET', 'POST'])
# @login_required
# def visionBoard():


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/homepage")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 403)

        # Ensure password was submitted
        if not password:
            return apology("must provide password", 403)

        # Ensure password confirmation was submitted
        if not request.form.get("confirmation"):
            return apology("must provide confirmation", 403)

        # Ensure password and the user's password confirmation matches
        if (password) != (request.form.get("confirmation")):
            return apology("Password must match", 403)

        sameUser = db.execute("SELECT username FROM users WHERE username = ?", username)

        # Ensures the username does not alrready exsist
        if len(sameUser) != 0:
            return apology("This username already exists", 403)

        # Inserts the user's username and hashed password into the database
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
        return redirect("/login")

    else:
        return render_template("register.html")