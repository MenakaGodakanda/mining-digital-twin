# scripts/visualization.py
from datetime import datetime
import numpy as np
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import threading
import time

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Mining Operation Digital Twin Dashboard", style={'textAlign': 'center'}),
    
    # Graph for Temperature Over Time
    dcc.Graph(id="live-temperature-graph"),
    
    # Graph for Equipment Status Over Time
    dcc.Graph(id="live-equipment-status-graph"),
    
    # Interval component to update the graphs every 5 seconds
    dcc.Interval(id="interval-component", interval=5000, n_intervals=0)
])

# Callback to update the temperature graph
@app.callback(
    Output("live-temperature-graph", "figure"),
    Input("interval-component", "n_intervals")
)
def update_temperature_graph(n):
    # Load sensor data
    data = pd.read_csv("./data/sensor_data.csv")
    
    # Create a line chart for temperature over time
    fig = px.line(data, x="timestamp", y="temperature", title="Temperature Over Time")
    return fig

# Callback to update the equipment status graph
@app.callback(
    Output("live-equipment-status-graph", "figure"),
    Input("interval-component", "n_intervals")
)
def update_equipment_status_graph(n):
    # Load equipment data
    equipment_data = pd.read_csv("./data/equipment_data.csv")
    
    # Map status to numerical values for better visualization
    status_map = {"Running": 0, "Idle": 1, "Maintenance": 2}
    equipment_data["status_numeric"] = equipment_data["status"].map(status_map)
    
    # Create a line chart for equipment status over time
    fig = px.line(equipment_data, x="timestamp", y="status_numeric", 
                  title="Equipment Status Over Time",
                  labels={"status_numeric": "Status", "timestamp": "Time"},
                  hover_data={"status_numeric": False, "status": True})
    
    # Customize the y-axis to show status labels instead of numbers
    fig.update_yaxes(tickvals=[0, 1, 2], ticktext=["Running", "Idle", "Maintenance"])
    
    return fig

# Function to simulate new data
def run_simulation():
    while True:
        # Simulate new sensor data
        new_sensor_data = {
            "timestamp": [datetime.now()],
            "temperature": [np.random.uniform(20, 50)],
            "pressure": [np.random.uniform(800, 1200)],
            "vibration": [np.random.uniform(0, 10)]
        }
        new_sensor_df = pd.DataFrame(new_sensor_data)
        new_sensor_df.to_csv("./data/sensor_data.csv", mode="a", header=False, index=False)
        
        # Simulate new equipment data
        new_equipment_data = {
            "timestamp": [datetime.now()],
            "equipment_id": [np.random.choice(["Truck-001", "Drill-002", "Conveyor-003"])],
            "status": [np.random.choice(["Running", "Idle", "Maintenance"])]
        }
        new_equipment_df = pd.DataFrame(new_equipment_data)
        new_equipment_df.to_csv("./data/equipment_data.csv", mode="a", header=False, index=False)
        
        # Wait for 5 seconds before generating new data
        time.sleep(5)

# Run the simulation in a separate thread
if __name__ == "__main__":
    threading.Thread(target=run_simulation, daemon=True).start()
    app.run_server(debug=True)
