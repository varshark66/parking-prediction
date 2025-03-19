import os
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("parking_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        time_hour = int(request.form["time"])  
        day_of_week = int(request.form["day_of_week"])
        weather = int(request.form["weather"])

        # Prepare input data for prediction
        input_data = np.array([[time_hour, day_of_week, weather]])

        # Make prediction
        prediction = model.predict(input_data)
        result = "Available" if prediction[0] == 1 else "Not Available"

        return render_template("index.html", prediction=result)
    except:
        return render_template("index.html", prediction="Error in Prediction")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Get port from Render
    app.run(host="0.0.0.0", port=port)  # Bind to the correct port
