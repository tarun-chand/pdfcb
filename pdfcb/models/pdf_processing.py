from pdfminer.high_level import extract_text
import openai
from config import Config
from services.database import collection
from uuid import uuid4
import logging

openai.api_key = Config.OPENAI_API_KEY

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def chunk_text(text, chunk_size=500):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])

def process_pdf(file_path):
    try:
        # Extract text from the PDF
        text = extract_text(file_path)
        logger.info(f"Extracted text from {file_path}")

        # Chunk the text and generate embeddings for each chunk
        for chunk in chunk_text(text):
            response = openai.Embedding.create(
                input=chunk,
                model="text-embedding-ada-002"
            )
            embedding = response['data'][0]['embedding']

            # Prepare document to store in MongoDB
            document = {
                "_id": str(uuid4()),
                "pdf_name": file_path,
                "text_chunk": chunk,
                "embedding": embedding
            }

            # Insert document into MongoDB
            collection.insert_one(document)
            logger.info(f"Inserted chunk from {file_path} into MongoDB")

    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        raise
