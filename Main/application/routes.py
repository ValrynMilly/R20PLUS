from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt
from application import app
from application.forms import RegistrationForm, LoginForm
from application.models import Posts, Users
from flask import render_template, redirect, url_for, request
from flask import Flask, render_template


@app.route('/signup.html', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(email=form.email.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('post'))
    return render_template('signup.html', title='Register', form=form)


@app.route("/login.html", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('login.html'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)