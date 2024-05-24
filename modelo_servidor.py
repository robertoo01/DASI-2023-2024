from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
#pip install flask-cors
from flask_cors import CORS

from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)

# Cargamos los modelos:
modelo_Reg = joblib.load('modelo.pkl') #Modelo de regresion
modelo_RN = load_model('modelo_RN.h5') #Modelo de Red Neuronal

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form
        features = [float(data[f'feature{i}']) for i in range(len(data))]
        features = np.array(features).reshape(1, -1)
        prediction = modelo_Reg.predict(features)
        
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/predict2', methods=['POST'])
def predict2():
    try:
        data = request.form
        features = [float(data[f'feature{i}']) for i in range(len(data))]
        features = np.array(features).reshape(1, -1)
        prediction = modelo_RN.predict(features)
        
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
