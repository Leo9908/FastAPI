from pymongo import MongoClient

# Coneccion a base de datos local
db_client = MongoClient().local  # Por defecto se conecta a localhost


# Coneccion a base de datos en produccion
# db_client = MongoClient(
#   'mongodb+srv://leandro:Uso6OmBxwsogA6dQ@cluster0.xmgwqqk.mongodb.net/?retryWrites=true&w=majority').test
