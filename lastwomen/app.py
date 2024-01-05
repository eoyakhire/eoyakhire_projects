from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    visibility = db.Column(db.String(10), nullable=False)

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    visibility = SelectField('Visibility', choices=[('public', 'Public'), ('private', 'Private')], default='public')

# Use app.app_context() to create an application context
with app.app_context():
    # Create the database tables
    db.create_all()

@app.route('/')
def index():
    posts = Post.query.filter_by(visibility='public').all()
    return render_template('index.html', posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/story")
def story():
    return render_template("story.html")

@app.route("/generate")
def generate():
    return render_template("generate.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, visibility=form.visibility.data)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('posts.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('homepage')) # Redirects the user to their homepage

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_username = request.form['newUsername']
        new_password = request.form['newPassword']

        # Adds the new user to the simulated database
        users[new_username] = new_password

        session['username'] = new_username
        return redirect(url_for('login')) #Redirects the user to the log in page 

    return render_template('register.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)