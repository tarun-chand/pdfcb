from flask import Blueprint, request, jsonify
from models.similarity import query_similar_chunks

query_bp = Blueprint('query', __name__)

@query_bp.route('/query', methods=['GET'])
def query():
    query_text = request.args.get('query')
    if not query_text:
        return jsonify({"error": "No query provided"}), 400
    try:
        results = query_similar_chunks(query_text, top_n=5)
        return jsonify([
            {"similarity": sim, "pdf_name": pdf_name, "text_chunk": chunk}
            for sim, chunk, pdf_name in results
        ]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
