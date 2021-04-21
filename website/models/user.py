from flask import Markup, url_for
from flask_login import UserMixin
from website import login_manager
from website.models.master import Model
from website.models.recipe import Recipe

@login_manager.user_loader
def load_user (_id):
    return User.get(by="_id", value=_id)

class User(Model, UserMixin):
    mtype = 'user'
    tablename = 'users'
    #//SECTION: DB METHODS
    @classmethod
    def get_insert_statement (cls, model):
        statement = (f"""
        INSERT INTO {model.tablename}
            (_id, cart, email, fname,
            img_loc, ip_addr, is_valid,
            likes, password, rates, views)
        VALUES
            ('{model._id}', '{model.cart}',
            '{model.email}', '{model.fname}',
            '{model.img_loc}', '{model.ip_addr}',
            '{model.is_valid}', '{model.likes}',
            '{model.password}', '{model.rates}',
            '{model.views}')""")
        return statement

    @classmethod
    def get_table_statement (cls):
        """
        Returns the DB statement that
        creates this model's table
        """
        statement = (f"""
        CREATE TABLE {cls.tablename}
            (_id varchar(25) PRIMARY KEY,
            cart text,
            email varchar(50) UNIQUE,
            fname varchar(30),
            img_loc varchar(50) DEFAULT 'default.jpg',
            ip_addr varchar(25), 
            is_valid int,
            likes text,
            password varchar(100),
            rates text,
            views text,
            upldate datetime DEFAULT CURRENT_TIMESTAMP(),
            moddate datetime DEFAULT CURRENT_TIMESTAMP()
        )""")
        return statement

    @classmethod
    def get_update_statement(cls, model):
        """ 
        Returns the DB statement that
        updates models in this table
        """
        statement = (f"""UPDATE {cls.tablename}
        SET
            cart = "{model.cart}",
            email = "{model.email}",
            fname = "{model.fname}",
            img_loc = "{model.img_loc}",
            ip_addr = "{model.ip_addr}",
            is_valid = "{model.is_valid}",
            likes = "{model.likes}",
            password = "{model.password}",
            rates = "{model.rates}",
            views = "{model.views}",
            moddate = CURRENT_TIMESTAMP()
        WHERE
            _id = "{model._id}"
        """)
        return statement


    #//SECTION: staticmethods
    @staticmethod
    def get_temp_user (ip_requesting):
        mdict = {
            'cart' : "",
            'email' : None,
            'fname' : None,
            'img_loc' : 'default.png',
            'ip_addr' : ip_requesting,
            'is_valid' : 0,
            'likes': "",
            'password' : None,
            'rates': "",
            'views': "",
        }
        temp_user = User(mdict)
        return temp_user

    #//SECTION: classmethods

    
    #//SECTION: __init__
    def __init__(self, mdict):
        super().__init__(mdict)
        self.cart = mdict['cart']
        self.email = mdict ['email']
        self.fname = mdict ['fname']
        self.img_loc = mdict ['img_loc']
        self.ip_addr = mdict ['ip_addr']
        self.is_valid = mdict ['is_valid']
        self.likes = mdict ['likes']
        self.password = mdict ['password']
        self.rates = mdict ['rates']
        self.views = mdict ['views']

    def liked_recipes (self):
        models = Recipe.get_models(self.likes)
        return models 


    def rated_recipes (self):
        models = Recipe.get_models(self.rates)
        return models


    def viewed_recipes (self):
        models = Recipe.get_models(self.views)
        return models
        

    def __str__(self):
        return f"""
                CART: {self.cart}
                EMAIL: {self.email}
                FIRST NAME: {self.fname}
                IMG LOCATION : {self.img_loc}
                IP ADDRESS: {self.ip_addr}
                IS VALID: {self.is_valid}
                LIKES : {self.likes}
                PASSWORD: {self.password}
                RATES: {self.rates}
                VIEWS: {self.views}
               """
