from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, AnyOf
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'KIrlL5QfT3eORaIqa65tPIpUuRgHAKeO'

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Email(message='I don\'t like your email.')])
	password = PasswordField('password', validators=[InputRequired(), Length(min=5, max=10), AnyOf(['secret', 'password'])])

@app.route('/Login.html', methods=['GET', 'POST'])
def index():
	form = LoginForm()
	if form.validate_on_submit():
		return 'Form Successfully Submitted!'
	return render_template('login.html', form=form)

class SignupForm(FlaskForm):
    fist_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])

@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		return 'Form Successfully Submitted!'
	return render_template('signup.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)