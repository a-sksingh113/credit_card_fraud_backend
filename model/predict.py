import pickle
import numpy as np
import os

model_path = os.path.join(os.path.dirname(__file__), 'credit card fraud model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

def predict_transaction(features: list) -> int:
    arr = np.array(features).reshape(1, -1)
    prediction = model.predict(arr)
    return int(prediction[0])  # 0 = Not Fraud, 1 = Fraud
