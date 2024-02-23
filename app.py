import os

from flask import (Flask, jsonify, request)

app = Flask(__name__)

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
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
