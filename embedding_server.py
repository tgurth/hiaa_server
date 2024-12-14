from flask import Flask, request, jsonify
import tensorflow_hub as hub
from flask_cors import CORS, cross_origin
import numpy as np

# Universal Sentence Encoder model
use_model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
# Flask App
app = Flask(__name__)
CORS(app, origins="https://tylergurth.com", methods=["GET", "POST"])

# For taking text and returning embeddings
@app.route('/get_embedding', methods=['POST'])
def get_embedding():
    data = request.get_json()
    sentence = data.get('sentence', '')

    if not sentence:
        return jsonify({'error': 'No sentence provided'}), 400
    
    # Returning the embeddings
    embedding = use_model([sentence])[0].numpy().tolist()
    return jsonify({'embedding': embedding})

if __name__ == '__main__':
    app.run(debug=True)