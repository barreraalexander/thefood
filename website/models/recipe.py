from flask import Markup, url_for, current_app
from website import cache
from website.models.master import Model
import json

NATIONALITY_KEYWORD_LS = []

class Recipe (Model):
    mtype = 'recipe'
    tablename = 'recipes'
#//SECTION: CLASS METHODS
#//SECTION: DB METHODS
    @classmethod
    def get_insert_statement (cls, model):
        """ 
        Returns the DB statement that
        inserts models in this table
        """
        statement = (f"""
        INSERT INTO {model.tablename}
            (_id, name, url, description,
            ingredients, steps, preptime,
            cooktime, totaltime, keyword,
            rating, img_locs)
        VALUES
            ('{model._id}', '{model.name}',
            '{model.url}', '{ model.description}',
            '{model.ingredients}', '{model.steps}',
            '{model.preptime}', '{model.cooktime}',
            '{model.totaltime}', '{model.keyword}',
            {model.rating}, '{model.img_locs}')
        """)
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
            name varchar(100) UNIQUE,
            url varchar(100) UNIQUE,
            description text,
            ingredients text,
            steps text,
            preptime varchar(25),
            cooktime varchar(25),
            totaltime varchar(25),
            keyword varchar(25),
            rating float DEFAULT 0,
            img_locs text,
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
        statement = (f"""UPDATE {model.tablename}
        SET
            name = "{model.name}",
            url = "{model.url}",
            description = "{model.description}",
            ingredients = "{model.ingredients}",
            steps = "{model.steps}",
            preptime = "{model.preptime}",
            cooktime = "{model.cooktime}",
            totaltime = "{model.totaltime}",
            keyword = "{model.keyword}",
            rating = {model.rating},
            img_locs = "{model.img_locs}"
            moddate = CURRENT_TIMESTAMP()
        WHERE
            _id = "{model._id}"
        """)
        return statement

#//SECTION: STATIC METHODS
    @staticmethod
    def get_models(data):
        """
        data is a $-separated blob
        of _ids from the db. 
        """
        spl_data = data.split('$')
        models = [ Recipe.get(by='_id', value=elem) \
                 for elem in spl_data \
                 if elem != "" \
                 and elem != False ]
        return models

    @staticmethod
    @cache.cached(timeout=0)
    def get_all_cached():
        models = Recipe.get(getall=True)
        return models
        
# //SECTION: __init__
    def __init__(self, mdict):
        super().__init__(mdict)
        self.name = mdict['name']
        self.url = mdict['url']
        self.description = mdict['description']
        self.ingredients = mdict['ingredients']
        self.steps = mdict['steps']
        self.preptime = mdict['preptime']
        self.cooktime = mdict['cooktime']
        self.totaltime = mdict['totaltime']
        self.keyword = mdict['keyword']
        self.rating = mdict['rating']
        self.img_locs = mdict['img_locs']

#//SECTION: PROPERTIES
    @property
    def as_json(self):
        model_json = json.dumps (self.as_dict)
        return model_json

    @property
    def as_dict(self):
        return {
            '_id': self._id,
            'name': self.name,
            'ingredients': self.ingredients,
            'steps': self.steps,
            'cooktime': self.cooktime,
            'preptime': self.preptime,
            'totaltime': self.totaltime,
            'keyword': self.keyword,
            'rating': self.rating,
            'href': url_for('main.recipe', model_id=self._id),
            'img_locs':self.img_locs,
        }
    

    def __str__(self):
        return (f"""
                ID: {self.id}
                NAME: {self.name}
                URL: {self.url}
                INGREDIENTS: {self.ingredients}
                STEPS: {self.steps}
                PREP TIME: {self.preptime}
                COOK TIME: {self.cooktime}
                TOTAL TIME: {self.totaltime}
                KEYWORD: {self.keyword}
                RATING: {self.rating}
                IMGFILES FILENAME: {self.img_locs}
                """)