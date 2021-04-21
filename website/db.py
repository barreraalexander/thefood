from flask_mysqldb import MySQL

class DB (MySQL):
    def __init__(self, app=None):
        super().__init__(app=app)

    #//SECTION: CALLS AND QUERIES
    def create_table (self, statement):
        try:    
            cur = self.connection.cursor ()
            cur.execute (statement)
            self.connection.commit ()
        except Exception as e:
            print (e)
            return e

    def get (self, tablename, col='column', value='value', getrandom=False, getall=False, getmany=False):
        statement = (f"""SELECT * FROM {tablename}
        WHERE {col} = "{value}" """)

        if getrandom is True:
            statement = (f"""SELECT * FROM {tablename}
                        ORDER BY RAND() LIMIT 1""")

        elif getall is True:
            statement = (f""" SELECT * FROM {tablename} """)
            cur = self.connection.cursor ()
            cur.execute (statement)
            records = cur.fetchall ()
            return records

        
        if getmany is True:
            cur = self.connection.cursor ()
            cur.execute (statement)
            records = cur.fetchall ()
            return records
            
        cur = self.connection.cursor ()
        cur.execute (statement)
        record = cur.fetchone ()
        return record

    #//SECTION: INSERTS AND UPDATES 
    def insert (self, statement):
        try:
            cur = self.connection.cursor ()
            cur.execute (statement)
            self.connection.commit ()
        except Exception as err:
            print ('ERROR INSERTING INTO DATABASE: \n')
            print (err)

    def remove (self, model):
        statement = f"""DELETE FROM {model.tablename}
        WHERE _id = "{model._id}" """
        cur = self.connection.cursor ()
        cur.execute (statement)
        self.connection.commit()

    def update (self, statement):
        cur = self.connection.cursor()
        cur.execute (statement)
        self.connection.commit ()
