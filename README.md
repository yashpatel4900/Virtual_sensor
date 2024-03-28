# IoT Cloud Solution README

## Introduction
This project demonstrates the creation of a cloud-hosted IoT system designed to collect and visualize sensor data. By leveraging the MQTT protocol for data transfer, it integrates with ThingSpeak for the cloud-based visualization of sensor outputs.

## Setup and Operation

### Steps

- **Sensor Simulation**
  - Developed in Python, this script simulates sensors that provide periodic and random readings of CO2 concentration, humidity, and temperature within specific limits.

- **ThingSpeak Configuration**
  - ThingSpeak was selected as the cloud platform due to its simplicity and effectiveness for IoT projects. It is used here for its MQTT service, facilitating data ingestion and storage.

- **MQTT Configuration and Authentication**
  - The setup involves configuring MQTT channels, clients, and devices with crucial credentials such as channel ID, API key, Client ID, username, and password. This ensures a secure connection to the ThingSpeak MQTT broker.

- **Data Monitoring and Analysis**
  - The Paho MQTT library, along with MQTT Topic, are used for sending sensor data to the ThingSpeak channel. The system continuously monitors and analyzes the data to verify the accurate publishing of sensor readings.

## Conclusion

This IoT solution proficiently collects and forwards data from simulated sensors to the ThingSpeak cloud platform using MQTT. It showcases the system's ability to monitor environmental conditions, laying a groundwork for broader application in various IoT scenarios.
