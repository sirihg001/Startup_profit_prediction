from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
# Load the trained model (Commenting out the above line and replcing the below path in place of MODEL_PATH below while running locally)
#"C:\\Desktop\\pprj\\startup_pred_proj\\model.pkl"
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        rnd_spend = float(request.form["rnd_spend"])
        admin = float(request.form["admin"])
        marketing = float(request.form["marketing"])
        state = request.form["state"]  # Categorical variable

         # Create a DataFrame with correct column names (matching training data)
        features = pd.DataFrame([[rnd_spend, admin, marketing, state]], 
                                columns=["R&D Spend", "Administration", "Marketing Spend", "State"])

        print(f"Feature shape: {features.shape}")  # Debugging
        print(f"Features:\n{features}")  # Check what is being passed

        # Make prediction
        prediction = model.predict(features)[0]
        return f"Predicted Profit: ${prediction:.2f}"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)