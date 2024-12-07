import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

