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
![Screenshot 2025-01-30 122059](https://github.com/user-attachments/assets/9584fe14-e9b9-4d37-b3ea-549180d56256)

Install the required Python packages:
```
pip install pandas numpy scikit-learn matplotlib dash plotly
```

#### 1. Pandas
- Pandas is a powerful library for data manipulation and analysis. It provides data structures like DataFrames and Series, which make it easy to handle structured data (e.g., CSV files, Excel sheets).
- Used to load, process, and manipulate sensor and equipment data stored in CSV files.

#### 2. NumPy
- NumPy is a fundamental library for numerical computing in Python. It provides support for arrays, matrices, and mathematical functions.
- Used to generate random sensor data (e.g., temperature, pressure, vibration) and perform numerical operations.

#### 3. Scikit-learn
- Scikit-learn is a machine learning library that provides tools for data modeling, including classification, regression, clustering, and more.
- Used to train a Random Forest classifier for predicting equipment status based on sensor data.

#### 4. Matplotlib
- Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python.
- Not directly used in this project, but it’s a common alternative to Plotly for creating graphs and charts.

#### 5. Dash
- Dash is a framework for building interactive web applications in Python. It is built on top of Flask, Plotly, and React.js.
- Used to create a real-time dashboard for visualizing sensor and equipment data.

#### 6. Plotly
- Plotly is a graphing library that makes interactive, publication-quality graphs. It integrates well with Dash for creating web-based visualizations.
- Used to create interactive line charts for temperature and equipment status in the dashboard.


### 4. Data Generation
Generate the initial data:
```
python scripts/data_generator.py
```
- This script will generate synthetic sensor and equipment data.
- Output: Two CSV files (`sensor_data.csv` and `equipment_data.csv`) will be generated in the `data/` directory.
![Screenshot 2025-01-30 175756](https://github.com/user-attachments/assets/57a1cb43-31b0-47c5-ba9c-f2d3c07673bc)

- Example Content:
  - `sensor_data.csv`:
![Screenshot 2025-01-30 181041](https://github.com/user-attachments/assets/2e363715-edef-4d49-972c-da03e58888bc)

  - `equipment_data.csv`:
![Screenshot 2025-01-30 181023](https://github.com/user-attachments/assets/ccf2281f-c1f9-4548-bdf0-094574a4a0cf)

- Console Output:
![Screenshot 2025-01-30 123557](https://github.com/user-attachments/assets/bbf8fe4b-6ac6-4502-9980-611344e1cf62)

### 5. Data Processing
Train the predictive model:
```
python scripts/data_processor.py
```
- This script will process the data and train a simple predictive model.
- Output: A trained machine learning model (predictive_model.pkl) will be saved in the models/ directory.
![Screenshot 2025-01-30 175748](https://github.com/user-attachments/assets/4b3b3fe9-8a88-4985-bc10-b848d581aa5c)

- Console Output:
![Screenshot 2025-01-30 124946](https://github.com/user-attachments/assets/3977e91a-302a-439c-bcb6-a03db9457f0c)

- The accuracy will vary depending on the random data generated.

### 6. Mining Simulation
Run the mining operation simulation:
```
python scripts/simulation.py
```
- This script will simulate the mining operation using the trained model.
- Output: The simulation will continuously predict the status of mining equipment based on the generated sensor data.

- Console Output:
![Screenshot 2025-01-30 125301](https://github.com/user-attachments/assets/d882886e-c571-426a-947c-fc8c9c186357)

- This will update every 5 seconds.

### 7. Real-Time Visualization
Start the real-time visualization dashboard:
```
python scripts/visualization.py
```
- This script will create a real-time dashboard.
![Screenshot 2025-01-30 130206](https://github.com/user-attachments/assets/90b6a8df-cb4c-4281-97b3-1bcfda37995f)

- Output: A web-based dashboard will display real-time sensor data (e.g., temperature over time).
- Dashboard:
  - Open your browser and navigate to `http://127.0.0.1:8050/`.
  - You will see a live-updating line chart showing the temperature data over time.
  - Example:

https://github.com/user-attachments/assets/8be4fc63-b996-4509-8b99-b693ab4131ee

https://github.com/user-attachments/assets/3d88a91a-a690-44f0-a03c-d39b72a8eef4

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
