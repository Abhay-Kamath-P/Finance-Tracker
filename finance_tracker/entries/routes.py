from flask import  render_template, url_for, flash, redirect
from finance_tracker.models import Entry
from finance_tracker.entries.forms import EntryForm
from finance_tracker import db
from flask_login import current_user, login_required

from flask import Blueprint

entries = Blueprint('entries', __name__)

@entries.route("/entry/new", methods=['GET', 'POST'])
@login_required
def new_entry():
    form = EntryForm()
    if form.validate_on_submit():
        category_label = dict(form.category.choices).get(form.category.data, form.category.data)
        entry = Entry(amount=form.amount.data, type=form.type.data, category=category_label, user_id=current_user.id, note=form.note.data)
        db.session.add(entry)
        db.session.commit()
        flash('Entry has been created.', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_entry.html', title = 'New Entry', form = form)