from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('data.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from POST request
        data = request.get_json()
        
        # Convert the data into the correct format for prediction
        features = [
            data['mean_radius'],
            data['mean_texture'],
            data['mean_perimeter'],
            data['mean_area'],
            data['mean_smoothness'],
            data['mean_compactness'],
            data['mean_concavity'],
            data['mean_concave_points'],
            data['mean_symmetry'],
            data['mean_fractal_dimension'],
            data['radius_error'],
            data['texture_error'],
            data['perimeter_error'],
            data['area_error'],
            data['smoothness_error'],
            data['compactness_error'],
            data['concavity_error'],
            data['concave_points_error'],
            data['symmetry_error'],
            data['fractal_dimension_error'],
            data['worst_radius'],
            data['worst_texture'],
            data['worst_perimeter'],
            data['worst_area'],
            data['worst_smoothness'],
            data['worst_compactness'],
            data['worst_concavity'],
            data['worst_concave_points'],
            data['worst_symmetry'],
            data['worst_fractal_dimension']
        ]
        
        # Convert to numpy array and reshape for prediction
        features_array = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features_array)[0]
        
        # Get prediction probabilities
        probabilities = model.predict_proba(features_array)[0]
        
        # The probability of the predicted class
        probability = probabilities[prediction]
        
        # Return the prediction as JSON
        return jsonify({
            'prediction': int(prediction),  # 0 for benign, 1 for malignant
            'probability': float(probability)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)