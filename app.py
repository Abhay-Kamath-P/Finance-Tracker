from flask import Flask, render_template, url_for, flash, redirect
from forms import regForm, loginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'


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
            flash("You have successfully logged in", 'success')
            return redirect(url_for('home'))
        else:
            flash("Login unsuccessful", 'danger')
    return render_template('login.html', title = 'Login', form = form)
