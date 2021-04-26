import json

with open ('/etc/food_config.json') as config_file:
    config = json.load(config_file)

class DBConfig:
    SECRET_KEY = config.get('SECRET_KEY')
    MYSQL_USER = config.get('MYSQL_USER')
    MYSQL_PASSWORD = config.get('MYSQL_PASSWORD')
    MYSQL_HOST= config.get('MYSQL_HOST')
    MYSQL_DB = config.get('MYSQL_DB')
    MYSQL_CURSORCLASS = "DictCursor"
    shell_conn = "alex:F00dapp1!@recipedb.czl2wgls13df.us-east-1.rds.amazonaws.com"

cacheConfig = {
    "DEBUG": True,         
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300
}
