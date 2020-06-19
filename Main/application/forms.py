from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users, Characters, inventory

class RegistrationForm(FlaskForm):
    email = StringField('Email',
            validators = [
                DataRequired(),
                Email()
            ]
    )
    first_name = StringField('First Name',
            validators = [
                DataRequired(),
            ]
    )
    last_name = StringField('Last Name',
            validators = [
                DataRequired(),
            ]
    )
    username = StringField('Username',
            validators = [
                DataRequired(),
            ]
    )
    password = PasswordField('Password',
            validators = [
                DataRequired(),
            ]
    )
    confirm_password = PasswordField('Confirm Password',
            validators = [
                DataRequired(),
                EqualTo('password')
            ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired(),
		])
	remember = BooleanField('Remember Me')
    
	submit = SubmitField('Login')
 
class createcharacter(FlaskForm):
    Characte_name = StringField('Character Name',
            validators = [
                DataRequired(),
            ]
    )
    first_name = StringField('Player Name',
            validators = [
                DataRequired(),
            ]
    )
    background = StringField('Background',
            validators = [
                DataRequired(),
            ]
    )
    char_class = StringField('Class',
            validators = [
                DataRequired(),
            ]
    )
    race = StringField('Race',
            validators = [
                DataRequired(),
            ]
    )
    first_name = StringField('Player Name',
            validators = [
                DataRequired(),
            ]
    )
    alignment = StringField('Alignment',
            validators = [
                DataRequired(),
            ]
    )
    experience_points = StringField('XP Points',
            validators = [
                DataRequired(),
            ]
    )
    strength = StringField('Strength',
            validators = [
                DataRequired(),
            ]
    )
    dexterity = StringField('Dexterity',
            validators = [
                DataRequired(),
            ]
    )
    constitution = StringField('Constitution',
            validators = [
                DataRequired(),
            ]
    )
    intelligence = StringField('Intelligence',
            validators = [
                DataRequired(),
            ]
    )
    wisdom = StringField('Wisdom',
            validators = [
                DataRequired(),
            ]
    )
    charisma = StringField('Charisma',
            validators = [
                DataRequired(),
            ]
    )
    submit = SubmitField('Save Character')

class inventoryform(FlaskForm):
    health_potions = StringField('Health Potions',
            validators = [
            ]
    )
    scrolls = StringField('Scrolls',
            validators = [
            ]
    )
    keys = StringField('Keys',
            validators = [
            ]
    )
    arrows = StringField('Arrows',
            validators = [
            ]
    )
    shortsword = StringField('Short Swords',
            validators = [
            ]
    )
    longsword = StringField('Long Swords',
            validators = [
            ]
    )
    submit = SubmitField('Add Inventory')