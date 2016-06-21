from flask_wtf import Form
from wtforms import (StringField,
                     SubmitField,
                     validators)
from flask_user.forms import RegisterForm


class AppRegisterForm(RegisterForm):
    """ Definition of the App Registration Form.

    This adds application specific fields to the Flask-User RegisterForm class
    """
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])


class UserProfileForm(Form):
    """ Definition of the UserProfileForm

    This form is used by Flask-User.
    """
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])
    submit = SubmitField('Save')
