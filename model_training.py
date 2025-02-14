import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the dataset
df = pd.read_csv("C:/Desktop/pprj/startup_pred_proj/50_Startups.csv")
# Define feature columns
X = df[["R&D Spend", "Administration", "Marketing Spend", "State"]]
y = df["Profit"]

# Define column transformer
column_transformer = ColumnTransformer(
    transformers=[
        ("state", OneHotEncoder(drop="first"), [3])  # One-hot encoding for State
    ],
    remainder="passthrough"
)

# Define pipeline
model = Pipeline([
    ("preprocessor", column_transformer),
    ("regressor", LinearRegression())
])

# Train the model
model.fit(X, y)

# Save the model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model training completed and saved as model.pkl")