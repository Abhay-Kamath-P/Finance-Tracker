from flask import Flask, render_template, url_for, flash, redirect
from forms import regForm, loginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(24), nullable=False)
    entries = db.relationship('Entry', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    #type should be either 'income' or 'expense'
    type = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Entry('{self.debit}', '{self.credit}', '{self.category}', '{self.date}')"
    
with app.app_context():
    db.create_all()

entries = [
    {
        'debit' : 180,
        'credit' : 0,
        'category' : 'food',
        'date' : '10 Feb, 2026'
    },
    {
        'debit' : 150,
        'credit' : 0,
        'category' : 'travel',
        'date' : '10 Feb, 2026'
    },
    {
        'debit' : 0,
        'credit' : 2000,
        'category' : 'monthly',
        'date' : '1 Mar, 2026'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', entries = entries, title = "Home")

@app.route("/about")
def about():
    return "<h1>I am Abhay</h1>"

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = regForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@financetracker.com' and form.password.data == 'admin':
            flash("You have successfully logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful, check your email or password.", 'danger')
    return render_template('login.html', title = 'Login', form = form)
