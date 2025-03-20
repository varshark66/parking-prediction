from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# 📍 Parking Locations Data (Example Coordinates)
parking_locations = [
    {"name": "Mall Parking", "lat": 12.9716, "lng": 77.5946},  
    {"name": "Railway Station Parking", "lat": 12.9767, "lng": 77.5800},
    {"name": "Hospital Parking", "lat": 12.9507, "lng": 77.5848}
]

@app.route("/")
def home():
    return render_template("index.html", locations=parking_locations)

# 🚗 Parking Availability Prediction (Dummy Logic)
@app.route("/predict", methods=["POST"])
def predict():
    time = int(request.form.get("time"))
    day_of_week = int(request.form.get("day_of_week"))
    weather = int(request.form.get("weather"))

    # 🎯 Simple Random Prediction Logic (Replace with AI Model Later)
    prediction = random.choice(["Available", "Full", "Limited"])

    return render_template("index.html", prediction=prediction, locations=parking_locations)

if __name__ == "__main__":
    app.run(debug=True)
