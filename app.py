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
        time = int(request.form["time"])  
        day_of_week = int(request.form["day_of_week"])
        weather = int(request.form["weather"])

        # Prepare input data for prediction
        input_data = np.array([[time, day_of_week, weather]])  # ✅ Fixed Variable Name

        # Make prediction
        prediction = model.predict(input_data)
        result = "Available" if prediction[0] == 1 else "Not Available"

        return render_template("index.html", prediction=result)
    except Exception as e:
        return render_template("index.html", prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)  
