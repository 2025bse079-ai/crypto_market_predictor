import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
import joblib

app = Flask(__name__, static_folder='static')

model = joblib.load('models/btc_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    X = pd.DataFrame([{
        'Prev_Close':  data['prev_close'],
        'Prev_Volume': data['prev_volume'],
        'Prev_High':   data['prev_high'],
        'Prev_Low':    data['prev_low'],
        'MA_7':        data['ma_7'],
        'MA_30':       data['ma_30'],
        'Return_1d':   data['return_1d']
    }])
    prediction = model.predict(X)[0]
    return jsonify({'prediction': round(float(prediction), 2)})

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/chart-data')
def chart_data():
    return send_from_directory('static', 'chart_data.json')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    import os
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
