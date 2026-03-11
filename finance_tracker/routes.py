from flask import  render_template, url_for, flash, redirect, request
from finance_tracker.models import User, Entry
from finance_tracker.forms import regForm, loginForm
from finance_tracker import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = regForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You are now able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login unsuccessful, check your email or password.", 'danger')
    return render_template('login.html', title = 'Login', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title = 'Account')
