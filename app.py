import pickle
import numpy as np
from flask import Flask, request, jsonify
import json
from flask_cors import CORS
import locale

app = Flask(__name__)
CORS(app)

# Load pre-trained model and columns
model = pickle.load(open('project.pickle', 'rb'))
with open('columns.json', 'r') as f:
    columns = json.load(f)['data_columns']

# Function for prediction
def predict_price(location, size, bath, bhk):
    input_data = np.zeros(len(columns))
    input_data[0] = size
    input_data[1] = bath
    input_data[2] = bhk

    if location in columns:
        loc_index = columns.index(location.lower())
        input_data[loc_index] = 1

    prediction = model.predict([input_data])[0]
    return prediction

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    location = data['location']
    size = float(data['size'])
    bath = int(data['bath'])
    bhk = int(data['bhk'])

    # Set the locale for India (INR format)
    locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')

    predicted_price = predict_price(location, size, bath, bhk)
    predicted_price *= 83.5  # Convert to INR
    predicted_price *= size  # Adjust price based on size

    # Format the price in INR format with commas
    formatted_price = locale.format_string('₹%0.2f', predicted_price, grouping=True)

    return jsonify({'prediction': formatted_price})

if __name__ == '__main__':
    app.run(debug=True)
