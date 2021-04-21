from website.models.master import Model

class Rate(Model):
    mtype = 'rate'
    tablename = 'rates'
#//SECTIONS: DB STATEMENTS 
    @classmethod
    def get_insert_statement (cls, model):
        """ 
        Returns the DB statement that
        inserts models in this table
        """
        statement = (f"""
        INSERT INTO {model.tablename}
            (_id, user_id, recipe_id, rate)
        VALUES
            ('{model._id}', '{model.user_id}', '{model.recipe_id}', {model.rate})
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
            (_id char(50) PRIMARY KEY,
            user_id char(50),
            recipe_id char(50),
            rate float,
            upldate datetime DEFAULT CURRENT_TIMESTAMP(),
            FOREIGN KEY (user_id) REFERENCES users(_id)
                ON UPDATE CASCADE,
            FOREIGN KEY (recipe_id) REFERENCES recipes(_id)
                ON UPDATE CASCADE
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
                rate = {model.rate}
            WHERE
                _id = "{model._id}"
        """)
        return statement
#//SECTION: __init__
    def __init__(self, mdict):
        super().__init__(mdict)
        self.user_id = mdict ['user_id']
        self.recipe_id = mdict ['recipe_id']
        self.rate = mdict ['rate']