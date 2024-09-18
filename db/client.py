# Execute: mongod --dbpath "/Users/alvarikoke/Documents/mongodb/data/"
# Connection: mongodb://localhost

from pymongo import MongoClient

db_client = MongoClient().local
#db_client = MongoClient("mongodb+srv://<username>:<password>@<cluster-address>/<database>?retryWrites=true&w=majority").test