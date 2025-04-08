import time
import random  # Replace with actual sensor reading
import joblib # type: ignore
from config import MODEL_PATH
from notify import send_notification

# Load ML model
model = joblib.load(MODEL_PATH)

def read_sensors():
    # Replace with real sensor library readings
    soil_moisture = round(random.uniform(10.0, 90.0), 2)
    temperature = round(random.uniform(15.0, 40.0), 2)
    return soil_moisture, temperature

while True:
    soil, temp = read_sensors()
    print(f"Soil Moisture: {soil} | Temperature: {temp}")

    # Predict irrigation need
    input_data = [[soil, temp]]
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        send_notification("Irrigation needed! Moisture is low.")
    else:
        print("No irrigation needed.")
