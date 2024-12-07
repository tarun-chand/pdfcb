from flask import Flask
from config import Config
from routes.process_pdf import process_pdf_bp
from routes.query import query_bp

app = Flask(__name__)
app.config.from_object(Config)

# Register blueprints for routes
app.register_blueprint(process_pdf_bp)
app.register_blueprint(query_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
