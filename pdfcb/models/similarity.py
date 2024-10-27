import openai
import numpy as np
from services.database import collection

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def query_similar_chunks(query_text, top_n=5):
    # Generate embedding for the query text using OpenAI
    response = openai.Embedding.create(
        input=query_text,
        model="text-embedding-ada-002"
    )
    query_embedding = response['data'][0]['embedding']
    
    # Fetch all documents from MongoDB
    all_docs = list(collection.find({}))
    
    # Calculate similarity for each document
    similarities = []
    for doc in all_docs:
        similarity = cosine_similarity(query_embedding, doc["embedding"])
        similarities.append((similarity, doc["text_chunk"], doc["pdf_name"]))
    
    # Sort by similarity
    sorted_similarities = sorted(similarities, key=lambda x: x[0], reverse=True)
    return sorted_similarities[:top_n]
