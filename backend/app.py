import pickle
from flask import Flask, request, jsonify
import numpy as np

# Load model
model_file = 'model/final_model.bin'
with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

# Labels
stress_labels = {
    0: "Low/Normal (No stress)",
    1: "Medium low (Mild stress)",
    2: "Medium (Moderate stress)",
    3: "Medium (Significant stress)",
    4: "High (Concerning)"
}

# Features used in model
most_important_features = ['heart_rate', 'sleeping_hours', 'snoring_rate', 'body_temperature']

# Initialize Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        input_data = {key: float(data[key]) for key in most_important_features}
    except KeyError as e:
        return jsonify({'error': f'Missing feature: {e}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid input type: {e}'}), 400

    X_input = dv.transform([input_data])
    y_pred = model.predict(X_input)
    predicted_level = int(y_pred[0])
    description = stress_labels.get(predicted_level, 'Unknown')

    return jsonify({
        'stress_level': predicted_level,
        'description': description
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
