# scripts/data_generator.py
import os
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_sensor_data(num_records=1000):
    timestamps = [datetime.now() - timedelta(seconds=i) for i in range(num_records)]
    temperature = np.random.uniform(20, 50, num_records)
    pressure = np.random.uniform(800, 1200, num_records)
    vibration = np.random.uniform(0, 10, num_records)
    
    data = {
        "timestamp": timestamps,
        "temperature": temperature,
        "pressure": pressure,
        "vibration": vibration
    }
    return pd.DataFrame(data)

def generate_equipment_data(num_records=1000):
    equipment_ids = ["Truck-001", "Drill-002", "Conveyor-003"]
    statuses = ["Running", "Idle", "Maintenance"]
    
    timestamps = [datetime.now() - timedelta(seconds=i) for i in range(num_records)]
    equipment_id = [random.choice(equipment_ids) for _ in range(num_records)]
    status = [random.choice(statuses) for _ in range(num_records)]
    
    data = {
        "timestamp": timestamps,
        "equipment_id": equipment_id,
        "status": status
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Ensure the data directory exists
    os.makedirs("./data", exist_ok=True)
    
    sensor_data = generate_sensor_data()
    equipment_data = generate_equipment_data()
    
    sensor_data.to_csv("./data/sensor_data.csv", index=False)
    equipment_data.to_csv("./data/equipment_data.csv", index=False)
    print("Data generated and saved to data/ directory.")
