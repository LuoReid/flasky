from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, current_app

from . import main
from .forms import NameForm
from .. import db
from ..models import User
from ..email import send_email


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        user = User.query.filter_by(username=name).first()
        if user is None:
            user = User(username=name)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'],
                           'New User','mail/new_user', user=user)
            # if app.config['FLASKY_ADMIN']:
            #     send_email(app.config['FLASKY_ADMIN'],
            #                 'New user', 'mail/new_user', user=user)
        else:
            session['known'] = True
        old_name = session.get('name')
        if old_name is not None and old_name != name:
            flash('Looks like you have changed your name!')
        session['name'] = name
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())
