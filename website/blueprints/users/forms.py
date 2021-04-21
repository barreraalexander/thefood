from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, FieldList, FormField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from website.models.user import User
from datetime import datetime

#//SECTION: AUTHENTICATION
class RegistrationForm (FlaskForm):
    fname = StringField('First Name',
                        validators=[DataRequired(),
                        Length(min=2, max=20)])
    
    email = StringField ('Email',
                        validators=[DataRequired(),
                        Email()])

    password = PasswordField ('Password',
                        validators=[DataRequired()])

    confirm_password = PasswordField ('Confirm Password',
                                     validators=[DataRequired(),
                                     EqualTo('password')])

    submit = SubmitField('Sign Up')

class LoginForm (FlaskForm):
    email = StringField ('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField ('Password', validators=[DataRequired()])

    remember = BooleanField ('Remember Me')
    submit = SubmitField('Login')

#//SECTION: UPDATE

class UpdateAccountForm (FlaskForm):
    fname = StringField('First Name',
                            validators=[DataRequired(), Length(min=2, max=20)], default=current_user)
    
    email = StringField ('Email',
                        validators=[DataRequired(), Email()])

    picture = FileField ('Update Profile Picture', validators=[FileAllowed (['jpg', 'jpeg', 'png'])])

    submit = SubmitField('Update')

    def validate_email (self, email):
        user = User.callmodel(email=email)
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

#//SECTION: USER INTERACTONS
class RateRecipeForm (FlaskForm):
    rate = FloatField ('Rate', validators=[DataRequired()])
    rate_recipe_id = StringField ('recipe_id')
    rate_submit = SubmitField ('Submit Rating')

class SaveRecipeForm (FlaskForm):
    recipe_id = StringField ('recipe_id', validators=[DataRequired() ])
    save_submit = SubmitField ('Save for Later')

class LikeRecipeForm (FlaskForm):
    liked_recipe_id = StringField ('recipe_id', validators=[DataRequired()])
    like_submit = SubmitField ('Like')

class ViewRecipeForm (FlaskForm):
    view_recipe_id = StringField ('recipe_id')
    view_submit = SubmitField ('View')


class AddToCartForm (FlaskForm):
    chosen_recipe_id = StringField ("Recipe ID", render_kw={'readonly': True})
    atc_submit = SubmitField ("Add Recipe to Cart")

class OrderForm(FlaskForm):
    ingredients = SelectMultipleField ('Order Ingredients')
    order_submit = SubmitField ("ORDER")
