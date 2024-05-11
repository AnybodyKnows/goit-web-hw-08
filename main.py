from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://goittestdb:1234@cluster0.goh2ue4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.goit

# Send a ping to confirm a successful connection
try:
    db.cats.insert_many([
        {
            "name": 'Boris',
            "age": 12,
            "features": ['ходить в лоток', 'не дає себе гладити', 'сірий'],
        },
        {
            "name": 'Murzik',
            "age": 1,
            "features": ['ходить в лоток', 'дає себе гладити', 'чорний'],
        },
    ])
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



