from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from website.blueprints.main import FOOD_KEYWORDS
from website.blueprints.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, OrderForm
from website import db, bcrypt
from website.models.recipe import Recipe
from website.models.user import User
from website.components.rate_flexy import component\
                                        as rate_component
users = Blueprint ('users', __name__)


# @users.route('/account', methods=['GET', 'POST'])
# @login_required
# def account():
#     form = UpdateAccountForm ()

#     if form.validate_on_submit():
#         if form.picture.data:
#             picturefile = save_picture(form.picture.data, profilepic=True)
#             current_user.imgfile = picturefile
#             User.update(current_user.__dict__)

#         current_user.fname = form.fname.data
#         current_user.email = form.email.data

#         User.update(current_user.__dict__)

#         return redirect (url_for('users.account'))
#     elif request.method == 'GET':
#         form.fname.data = current_user.fname
#         form.email.data = current_user.email
    
#     profilepic = url_for ('static', filename='images/profilepics/' + current_user.imgfile)

#     return render_template ('account.html', title='Account', form=form, profilepic=profilepic)


@users.route ('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()

    return render_template ('_login.html', title='login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@users.route ('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()

    return render_template ('_register.html', title='Register', form=form)


@users.route('/saved_later')
@login_required
def saved_later():
    profilepic = url_for ('static', filename='images/profilepics/' + current_user.imgfile)
    return render_template ('_saved_later.html', title='Saved Later')

@users.route ('/cart', methods=['GET', 'POST'])
def cart ():
    if current_user.is_authenticated:
        user = current_user
    else:
        curr_ip = request.remote_addr
        user = User.get (by='ip_addr', value=curr_ip)
        if user:
            pass
        else:
            user = User.get_temp_user(curr_ip)

    cart_items = user.cart.split('$')

    recipes = [ Recipe.get(by="_id", value=model_id)\
             for model_id in cart_items ]

    for recipe in recipes:
        if recipe == None:
            recipes.remove(recipe)

    form = OrderForm ()
    if form.validate_on_submit and form.order_submit.data:
        pass
        return redirect(url_for('users.cart'))

    return render_template('_cart.html',
                            title='Cart',
                            models=recipes,
                            form=form)

@users.route ('/rec_viewed', methods=['GET', 'POST'])
def rec_viewed ():
    if current_user.is_authenticated:
        user = current_user
    else:
        curr_ip = request.remote_addr
        user = User.get (by='ip_addr', value=curr_ip)
        if user:
            pass
        else:
            user = User.get_temp_user(curr_ip)
    return render_template('_rec_viewed.html',
                            title = 'Recently Viewed',
                            keywords=FOOD_KEYWORDS,
                            liked_recipes=user.liked_recipes(),
                            rated_recipes=user.rated_recipes(),
                            rate_component=rate_component,
                            viewed_recipes=user.viewed_recipes()
                            )
