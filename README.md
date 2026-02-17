# ISS-Tracker
A Python automation project that tracks the International Space Station (ISS) in real time using public APIs and sends a notification when the ISS is above your location during night time.

This project demonstrates API integration, geospatial filtering, time-based logic, and automated alert systems.

# Features
Fetches real-time ISS coordinates via REST API
- Retrieves sunrise and sunset times based on geographic location
- Implements geospatial proximity detection (+/- 5° range)
- Performs time-based filtering to check nighttime conditions
- Sends automated email notifications using SMTP
- Runs as a continuous monitoring system
