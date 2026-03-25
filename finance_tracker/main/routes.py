from flask import  render_template, url_for, flash, redirect, request
from finance_tracker.models import Entry
from flask_login import current_user, login_required


from flask import Blueprint

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    entries = Entry.query.filter_by(user_id=current_user.id).order_by(Entry.date.desc()).paginate(page=page, per_page=10)
    return render_template('home.html', entries=entries, title="Home")

@main.route("/about")
def about():
    return "<h1>I am Abhay</h1>"