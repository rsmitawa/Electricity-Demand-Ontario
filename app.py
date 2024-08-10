from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the pickled model
with open('xgb_electricity_demand_md.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Initialize Flask app
app = Flask(__name__)

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)
    
    # Extract features from the request data
    # Ensure to adjust this part based on how your model expects the input
    features = [data['feature1'], data['feature2'], data['feature3']]  # Modify based on your feature set
    
    # Convert features into a numpy array
    input_data = np.array(features).reshape(1, -1)
    
    # Make a prediction
    prediction = model.predict(input_data)
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction.tolist()})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
