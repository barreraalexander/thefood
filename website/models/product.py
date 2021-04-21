from website.models.master import Model


class Product(Model):
    mtype = 'product'
    tablename = 'products'


    @classmethod
    def get_insert_statement (cls, model):
        """ 
        Returns the DB statement that
        inserts models in this table
        """
        statement = (f"""
        INSERT INTO {model.tablename}
            (_id, name, manufacturer, ingredients)
        VALUES
            ('{model._id}', '{model.name}',
            '{  model.manufacturer}', '{  model.ingredients}')
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
            name char(100),
            manufacturer char(100),
            ingredients text
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
            name = "{model.name}",
            manufacturer = "{model.manufacturer}",
            ingredients = "{model.ingredients}"
        WHERE
            _id = "{model._id}"
        """)
        return statement

    def __init__(self, mdict):
        super().__init__(mdict)
        self.name = mdict ['name']
        self.manufacturer = mdict ['manufacturer']
        self.ingredients = mdict ['ingredients']


    def __str__(self):
        return (f"""
                ID: {self._id}
                NAME: {self.name}
                MANUFACTURER: {self.manufacturer}
                INGREDIENTS: {self.ingredients}
                """)