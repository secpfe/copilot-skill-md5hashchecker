import os
import requests  # Import the requests module
from flask import (Flask, jsonify, request, render_template)
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/openapi.yaml'  # Our API url (can be a local static file or url)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "MD5 Hash Lookup API"
    },
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

SOURCE_API_BASE_URL = "https://www.nitrxgen.net/md5db"

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/md5/<md5hash>', methods=['GET'])
def get_md5_hash(md5hash):
    response = requests.get(f"{SOURCE_API_BASE_URL}/{md5hash}.json")
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Hash not found or error in source API"}), 404

if __name__ == '__main__':
    app.run
