# scripts/data_processor.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

def load_data():
    sensor_data = pd.read_csv("./data/sensor_data.csv")
    equipment_data = pd.read_csv("./data/equipment_data.csv")
    
    # Convert timestamps to datetime for proper merging
    sensor_data["timestamp"] = pd.to_datetime(sensor_data["timestamp"])
    equipment_data["timestamp"] = pd.to_datetime(equipment_data["timestamp"])
    
    # Debug: Print dataset shapes and first few rows
    print(f"Sensor Data Loaded: {sensor_data.shape}")
    print(sensor_data.head())
    
    print(f"\nEquipment Data Loaded: {equipment_data.shape}")
    print(equipment_data.head())

    return sensor_data, equipment_data

def train_model(sensor_data, equipment_data):
    # Ensure timestamps are sorted before merge
    sensor_data = sensor_data.sort_values("timestamp")
    equipment_data = equipment_data.sort_values("timestamp")

    # Use merge_asof for nearest timestamp match
    data = pd.merge_asof(sensor_data, equipment_data, on="timestamp", direction="nearest")

    # Drop rows with missing values after merging
    data.dropna(inplace=True)

    # Debug: Print merged dataset shape
    print(f"\nMerged Data: {data.shape}")
    if data.empty:
        print("Error: Merged dataset is empty! Check timestamp alignment.")
        return
    
    print(data.head())

    # Feature engineering
    status_mapping = {"Running": 0, "Idle": 1, "Maintenance": 2}
    data["status"] = data["status"].map(status_mapping)

    # Check for unmapped values
    if data["status"].isna().any():
        print("Warning: Some status values were not mapped correctly!")

    X = data[["temperature", "pressure", "vibration"]]
    y = data["status"]

    # Debug: Print feature and target shapes
    print(f"\nShape of X: {X.shape}")
    print(f"Shape of y: {y.shape}")

    # Check if data is sufficient for training
    if X.shape[0] < 2:
        print("Error: Not enough data to split into training and test sets.")
        return

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Ensure models directory exists
    os.makedirs("./models", exist_ok=True)

    # Save model
    joblib.dump(model, "./models/predictive_model.pkl", compress=3)
    print("Model saved successfully.")

if __name__ == "__main__":
    sensor_data, equipment_data = load_data()
    train_model(sensor_data, equipment_data)
