import json


class DBConfig:
    SECRET_KEY = "secret_key"
    MYSQL_USER = "alex"
    MYSQL_PASSWORD = "F00dapp1!"
    MYSQL_HOST= "recipedb.czl2wgls13df.us-east-1.rds.amazonaws.com"
    MYSQL_DB = "thefood"
    MYSQL_CURSORCLASS = "DictCursor"
    shell_conn = "alex:F00dapp1!@recipedb.czl2wgls13df.us-east-1.rds.amazonaws.com"

class DBLocalConfig:
    SECRET_KEY = 'secret_key'
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "Barr1993"
    MYSQL_HOST = "localhost"
    MYSQL_DB = "the_food"
    MYSQL_CURSORCLASS = "DictCursor"
    shell_conn = "root:Barr1993@localhost"

cacheConfig = {
    "DEBUG": True,         
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}
