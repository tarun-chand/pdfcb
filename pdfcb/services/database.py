from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client['pdf_database']
collection = db['pdf_embeddings']
