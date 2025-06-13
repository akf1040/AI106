from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Model ve scaler yükle
model = model = tf.keras.models.load_model('star_model.h5')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Beklenen sırayla 8 özellik alınacak
    features = np.array([
        data['alpha'],
        data['delta'],
        data['u'],
        data['g'],
        data['r'],
        data['i'],
        data['z'],
        data['redshift']
    ]).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    predicted_class = int(np.argmax(prediction, axis=1)[0])
    confidence = float(np.max(prediction))
    return jsonify({'predicted_class': predicted_class, 'confidence': confidence})

if __name__ == '__main__':
    app.run(debug=True) 