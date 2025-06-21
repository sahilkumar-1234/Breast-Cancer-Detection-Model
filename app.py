from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
try:
    with open('data.pkl', 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    print(f"Error loading model: {str(e)}")
    # In production, you might want to exit here or handle differently

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400
            
        data = request.get_json()
        
        # Convert the data into the correct format for prediction
        features = [
            data['mean_radius'],
            data['mean_texture'],
            # ... (all your other features)
            data['worst_fractal_dimension']
        ]
        
        # Verify feature count
        if len(features) != 30:  # Update with your actual feature count
            return jsonify({'error': f'Expected 30 features, got {len(features)}'}), 400
        
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]
        probabilities = model.predict_proba(features_array)[0]
        probability = probabilities[prediction]
        
        return jsonify({
            'prediction': int(prediction),
            'probability': float(probability)
        })
        
    except KeyError as e:
        return jsonify({'error': f'Missing feature: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
else:
    app.config['JSON_SORT_KEYS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
