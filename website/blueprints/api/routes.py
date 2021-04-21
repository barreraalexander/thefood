from flask import render_template, url_for, flash,\
                  redirect, request, Blueprint
from flask_login import login_user, login_user,\
                        current_user, login_required
from website.models.recipe import Recipe
from website.models.user import User
from random import choice
import json

api = Blueprint ('api', __name__)

@api.route('/fetch_recipes')
def fetch_recipes():
    models = Recipe.get(getall=True)
    models_as_dict = [ model.as_dict for model in models ]    
    return json.dumps(models_as_dict)


@api.route('/fetch_recipes_by_keyword/<string:keyword>/<int:count>')
def fetch_recipes_by_keyword(keyword, count):
    models = Recipe.get(by="keyword", value=keyword, getmany=True)
    models_as_dict = [ model.as_dict for model in models ]

    if count == 1:
        random = choice(models_as_dict)
        return json.dumps(random)

    return json.dumps(models_as_dict[0:count])


@api.route('/fetch_recipe/<string:model_id>')
def fetch_recipe(model_id):
    if model_id == "random":
        model = Recipe.get(getrandom=True)
        return json.dumps(model.as_dict)

    model = Recipe.get(by="_id", value=model_id)
    return json.dumps(model.as_dict)



@api.route('/add_to_likes', methods=['GET', 'POST'])
def add_to_likes():
    if request.method == 'POST':
        if current_user.is_authenticated:
            user = current_user
        else:
            curr_ip = request.remote_addr
            user = User.get (by='ip_addr', value=curr_ip)
        
        recipe_id = request.json
        likes_ls = user.likes.split('$')
        if recipe_id not in likes_ls:
            user.likes += (f"{recipe_id}$")
            User.update(user)
        else:
            return
    return

@api.route('/add_to_views', methods=['GET', 'POST'])
def add_to_views():
    if request.method == 'POST':
        if current_user.is_authenticated:
            user = current_user
        else:
            curr_ip = request.remote_addr
            user = User.get (by='ip_addr', value=curr_ip)
        
        recipe_id = request.form.get('view_recipe_id')
        views_ls = user.views.split('$')
        if recipe_id not in views_ls:
            user.views += (f"{recipe_id}$")
            User.update(user)
            flash ('successfully added')
        else:
            flash ('already on the list')

    return redirect(url_for('main.recipe', model_id=recipe_id))

    @api.route('/add_to_cart', methods=['GET', 'POST'])
    def add_to_cart():
        if request.method == 'POST':
            if current_user.is_authenticated:
                user = current_user
            else:
                curr_ip = request.remote_addr
                user = User.get (by='ip_addr', value=curr_ip)
            
            recipe_id = request.json
            cart_ls = user.cart.split('$')
            if recipe_id not in cart_ls:
                user.cart += (f"{recipe_id}$")
                User.update(user)
            else:
                return
        return


# @api.route('/add_to_rates/', methods=['GET', 'POST'])
# def add_to_rates():
#     print (request)
#     if request.method == 'POST':
#         if current_user.is_authenticated:
#             user = current_user
#         else:
#             curr_ip = request.remote_addr
#             user = User.get (by='ip_addr', value=curr_ip)
        
#         recipe_id = request.form.get('liked_recipe_id')
#         likes_ls = user.likes.split('$')
#         if recipe_id not in likes_ls:
#             user.likes += (f"{recipe_id}$")
#             # User.update(user)
#         flash ('Added to your Cart')
#         return redirect(url_for('main.index'))

#     return redirect (url_for('main.index'))


@api.route('/login', methods=['GET', 'POST'])
def login():

    user = User.get(by='email', value=form.email.data)
    if user and bcrypt.check_password_hash (user.password, form.password.data):
        login_user (user, remember=True)
        next_page = request.args.get('next')
        return redirect(url_for('main.index'))
    return redirect(url_for('main.recipe', model_id=recipe_id))


@api.route('/register', methods=['GET', 'POST'])
def register():
    hashed_password = bcrypt.generate_password_hash \
                        (form.password.data).decode ('utf-8')                
    newuser = User (form.data)
    newuser.password = hashed_password 
    User.add(newuser)
    return redirect(url_for('users.login'))

    return redirect(url_for('main.recipe', model_id=recipe_id))
