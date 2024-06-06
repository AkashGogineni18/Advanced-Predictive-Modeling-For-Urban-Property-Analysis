from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors module
import util

app = Flask(__name__)
CORS(app)  # Apply CORS to your Flask app

# Endpoint to fetch location names
@app.route("/get_location_names")
def get_location_names():
    response = jsonify({"locations": util.get_location_names()})
    return response


# Endpoint to predict home price
@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    try:
        total_sqft = float(request.form["total_sqft"])
        location = request.form["location"]
        bhk = int(request.form["bhk"])
        bath = int(request.form["bath"])

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        response = jsonify({"estimated_price": estimated_price})

    except ValueError as ve:
        return jsonify({"error": "Invalid input data. Please check your inputs."}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return response


if __name__ == "__main__":
    print("Starting python server for Home Price prediction")
    util.load_saved_artifacts()
    app.run()
