import paho.mqtt.publish as mqtt_publish
import random
import time
import datetime

# Configuration for connecting to the MQTT broker.
MQTT_CHANNEL_ID = "2488607"
MQTT_HOST = "mqtt3.thingspeak.com"
MQTT_CLIENT_ID = "HCkmNBwVJxw0BAYnLAc6FxU"
MQTT_USERNAME = "HCkmNBwVJxw0BAYnLAc6FxU"
MQTT_PASSWORD = "jzDbgfgljTSuakSJGZkH+Zvw"
TRANSPORT = "websockets"
PORT = 80

# MQTT topic for publishing data.
TOPIC = f"channels/{MQTT_CHANNEL_ID}/publish"

class SensorSimulator:
    """
    Emulates an IoT device generating environmental sensor data: temperature, humidity, and CO2 levels.
    """
    def __init__(self):
        self.temp_range = (-50, 50)
        self.humidity_range = (0, 100)
        self.co2_range = (300, 2000)

    def get_readings(self):
        """
        Simulates generating sensor data readings for temperature, humidity, and CO2.
        """
        temp = random.uniform(*self.temp_range)
        humidity = random.uniform(*self.humidity_range)
        co2 = random.uniform(*self.co2_range)
        return temp, humidity, co2

def publish_sensor_data():
    simulator = SensorSimulator()

    while True:
        temperature, humidity, co2 = simulator.get_readings()

        # Assembling the data payload for publishing.
        payload = f"field1={temperature}&field2={humidity}&field3={co2}"

        # Logging the payload and publishing details.
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time} - Sending data: {payload} to {MQTT_HOST}, Client ID: {MQTT_CLIENT_ID}")

        # Publishing the data to the MQTT broker.
        mqtt_publish.single(
            TOPIC,
            payload,
            hostname=MQTT_HOST,
            transport=TRANSPORT,
            port=PORT,
            client_id=MQTT_CLIENT_ID,
            auth={"username": MQTT_USERNAME, "password": MQTT_PASSWORD},
        )

        time.sleep(5)

# Start the data publishing routine.
if __name__ == "__main__":
    publish_sensor_data()
