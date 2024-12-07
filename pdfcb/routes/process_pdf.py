from flask import Blueprint, request, jsonify
from models.pdf_processing import process_pdf
import os

process_pdf_bp = Blueprint('process_pdf', __name__)

@process_pdf_bp.route('/process_pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        print("Request files received:", request.files)
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    try:
        file_path = os.path.join('static/uploads', file.filename)  # Save temporarily
        file.save(file_path)
        process_pdf(file_path)
        os.remove(file_path)  # Clean up uploaded file after processing
        return jsonify({"message": f"{file.filename} processed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
