# scripts/simulation.py
import numpy as np
import pandas as pd
import joblib
from datetime import datetime, timedelta
import time

def simulate_mining_operation():
    model = joblib.load("./models/predictive_model.pkl")
    
    while True:
        # Generate new data point
        new_data = {
            "temperature": [np.random.uniform(20, 50)],
            "pressure": [np.random.uniform(800, 1200)],
            "vibration": [np.random.uniform(0, 10)]
        }
        new_df = pd.DataFrame(new_data)
        
        # Predict equipment status
        prediction = model.predict(new_df)
        status = ["Running", "Idle", "Maintenance"][prediction[0]]
        print(f"Predicted Equipment Status: {status}")
        
        time.sleep(5)  # Simulate every 5 seconds

if __name__ == "__main__":
    simulate_mining_operation()
