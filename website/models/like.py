from website.models.master import Model

class Like(Model):
    mtype = 'like'
    tablename = 'likes'


    @classmethod
    def get_insert_statement (cls, model):
        """ 
        Returns the DB statement that
        inserts models in this table
        """
        statement = (f"""
        INSERT INTO {model.tablename}
            (_id, user_id, recipe_id)
        VALUES
            ('{model._id}', '{model.user_id}','{ model.recipe_id}')
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
            (_id varchar(50) PRIMARY KEY,
            user_id varchar(50),
            recipe_id varchar(50),
            upldate datetime DEFAULT CURRENT_TIMESTAMP(),
            FOREIGN KEY (user_id) REFERENCES users(_id)
                ON UPDATE CASCADE,
            FOREIGN KEY (recipe_id) REFERENCES recipes(_id)
                ON UPDATE CASCADE
        )""")
        return statement


    def __init__(self, mdict):
        super().__init__(mdict)
        self.user_id = mdict ['user_id']
        self.recipe_id = mdict ['recipe_id']

    def __str__(self):
        return (f"""
                ID: {self._id}
                USER ID: {self.user_id}
                RECIPE ID: {self.recipe_id}
                """)