from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load your trained model
model = tf.keras.models.load_model('mnist_model.h5',compile = False)

def preprocess_image(image):
    image = image.convert("L")
    image = image.resize((28, 28))
    image = np.array(image)
    image = image / 255.0
    image = image.reshape(1, 28, 28, 1)
    return image

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    try:
        image = Image.open(io.BytesIO(file.read()))
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        digit = np.argmax(prediction[0])
        return jsonify({'digit': int(digit)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
