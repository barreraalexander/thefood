from flask import render_template, url_for, flash,\
                  redirect, request, Blueprint
from flask_login import login_user, login_user,\
                        current_user, login_required
from website import db, bcrypt, cache
from website.blueprints.users.forms import AddToCartForm, \
                                           LikeRecipeForm, \
                                           RateRecipeForm, \
                                           ViewRecipeForm
from website.components.chosen_recipe_section import component\
                                        as chosen_component
from website.blueprints.main import FOOD_KEYWORDS, PREVIEW_DIVS_COUNT
from website.components.preview_div import component\
                                        as preview_component
from website.components.rate_flexy import component\
                                        as rate_component

from website.models.recipe import Recipe
from website.models.product import Product
from website.models.user import User
from random import choice


main = Blueprint ('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    atc_form = AddToCartForm()
    like_form = LikeRecipeForm()    
    rate_form = RateRecipeForm()
    view_form = ViewRecipeForm()


    #i need to find a good wya of just get the count of 
    #preview_divs that I need
    # all_models = Recipe.get_all_cached()    
    preview_divs = []
    for i in range (PREVIEW_DIVS_COUNT):
        rand_model = Recipe.get(getrandom=True)
        preview_divs.append(preview_component(rand_model))

    chosen_div = chosen_component()

    return render_template ('_index.html',
                        title='The Food',
                        chosen_div=chosen_div,
                        atc_form=atc_form,
                        like_form=like_form,
                        rate_form=rate_form,
                        view_form=view_form,
                        preview_divs=preview_divs,
                        keywords=FOOD_KEYWORDS,
                        )


@main.route ('/recipes/<string:model_id>', methods=['GET', 'POST'])
def recipe (model_id):
    atc_form = AddToCartForm()
    like_form = LikeRecipeForm()
    model = Recipe.get (by="_id", value=model_id)
            
    return render_template ('_recipe.html',
                        title='The Recipe',
                        model=model,
                        atc_form=atc_form,
                        like_form=like_form)

