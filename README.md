# Digital Twin for Mining with Machine Learning

This project demonstrates the implementation of a Digital Twin for a mining operation. It simulates a mining environment, collects sensor and equipment data, processes the data using machine learning, and provides real-time visualization of the mining operation.

## Overview
<img width="959" alt="Screenshot 2025-01-30 at 5 52 30 pm" src="https://github.com/user-attachments/assets/fc96d79d-e639-4ad7-921c-53fca2b5cd6b" />

### Explanation
#### 1. Data Generation (Simulation):
- Simulates sensor data (e.g., temperature, pressure, vibration) and equipment status (e.g., Running, Idle, Maintenance).
- Outputs: `sensor_data.csv` and `equipment_data.csv`.

#### 2. Data Storage (CSV Files):
- Stores the generated sensor and equipment data in CSV files.
- Acts as a central repository for all simulated data.

#### Data Processing & Predictive Modeling:
- Processes the sensor and equipment data.
- Trains a machine learning model (e.g., Random Forest) to predict equipment status.
- Outputs: Trained model (`predictive_model.pkl`).

#### Mining Operation Simulation:
- Uses the trained model to simulate real-time predictions of equipment status.
- Outputs: Predicted equipment status in the console.

#### Real-Time Visualization (Dashboard):
- Visualizes the sensor data (e.g., temperature over time) in a web-based dashboard.
- Built using Dash and Plotly.
- Outputs: Live-updating charts and graphs.

### Data Flow
#### 1. Data Generation → Data Storage:
- Simulated data is saved to CSV files.

#### 2. Data Storage → Data Processing:
- Data is loaded from CSV files for processing and model training.


#### 3. Data Storage → Mining Operation Simulation:
- Real-time data is used for simulating equipment status predictions.

#### 4. Data Storage → Real-Time Visualization:
- Sensor data is visualized in the dashboard.


## Features

- Simulated mining environment with sensor and equipment data.
- Predictive analytics using a Random Forest classifier.
- Real-time monitoring using a Dash/Plotly dashboard.
- Open-source tools and libraries

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - Pandas, NumPy, Scikit-learn, Joblib, Dash, Plotly
- **Data Storage**: CSV files
- **Operating System**: Ubuntu (Linux)

## Setup Instructions
### 1. Prerequisites
- Ubuntu (20.04 or later)
- Python 3.8+
```
sudo apt install python3 python3-pip
```
- Git
```
sudo apt install git
```

### 2. Clone the Repository
Clone this repository to your local machine:
```
git clone https://github.com/MenakaGodakanda/mining-digital-twin.git
cd mining-digital-twin
```

### 3. Set Up a Virtual Environment
Create and activate a Python virtual environment:
```
python3 -m venv dtm
source dtm/bin/activate
```

Install the required Python packages:
```
pip install pandas numpy scikit-learn matplotlib dash plotly
```

### 4. Data Generation
Generate the initial data:
```
python scripts/data_generator.py
```
- This script will generate synthetic sensor and equipment data.
- Output: Two CSV files (`sensor_data.csv` and `equipment_data.csv`) will be generated in the `data/` directory.
- Example Content:
  - `sensor_data.csv`:

  - `equipment_data.csv`:

- Console Output:


### 5. Data Processing
Train the predictive model:
```
python scripts/data_processor.py
```
- This script will process the data and train a simple predictive model.
- Output: A trained machine learning model (predictive_model.pkl) will be saved in the models/ directory.

- Console Output:

- The accuracy will vary depending on the random data generated.

### 6. Mining Simulation
Run the mining operation simulation:
```
python scripts/simulation.py
```
- This script will simulate the mining operation using the trained model.
- Output: The simulation will continuously predict the status of mining equipment based on the generated sensor data.

- Console Output:

- This will update every 5 seconds.

### 7. Real-Time Visualization
Start the real-time visualization dashboard:
```
python scripts/visualization.py
```
- This script will create a real-time dashboard.
- Output: A web-based dashboard will display real-time sensor data (e.g., temperature over time).
- Dashboard:
- Open your browser and navigate to `http://127.0.0.1:8050/`.
- You will see a live-updating line chart showing the temperature data over time.
- Example:

- The chart will update every 5 seconds as new data is generated.

## File Structure
```
mining-digital-twin/
├── data/
│   ├── sensor_data.csv
│   └── equipment_data.csv
├── models/
│   └── predictive_model.pkl
├── scripts/
│   ├── data_generator.py
│   ├── data_processor.py
│   ├── simulation.py
│   └── visualization.py
└── README.md
```

## License
This project is licensed under the MIT License.
