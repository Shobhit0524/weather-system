# weather-system
The Weather App is a Python-based application designed to display real-time weather information for any city around the world. It provides a Command-Line Interface (CLI).
The main objective of the project is to allow users to quickly check weather conditions such as temperature, humidity, wind speed, and weather description (e.g., cloudy, sunny) in an easy and user-friendly way. The app retrieves weather data from the OpenWeatherMap API, ensuring accurate and up-to-date information.

Problem Solved:
Many users rely on web browsers or mobile apps to check the weather, which may be slow or cluttered with ads. This project provides a lightweight and clean Python-based alternative that can be used directly from the desktop or terminal.

Expected Outcomes:
• A functional weather application supporting both GUI and CLI modes.
• Display of weather details (temperature, humidity, wind speed, weather condition, and icon).
• Enhanced understanding of Python API integration and GUI development.

Workflow / Approach:
1. User enters the name of the city (CLI prompt).
2. The app sends a request to the OpenWeatherMap API using the requests library.
3. The JSON response containing weather data is parsed.
4. The relevant information (temperature, humidity, description, etc.) is extracted.
5. If the user chooses CLI mode, the data is printed neatly in the terminal.

Key Implementation Steps:
1. API Integration: The program connects to the OpenWeatherMap API to fetch real-time data.
2. Error Handling: Handles invalid city names, missing API keys, and connectivity errors gracefully.
3. CLI Interface: Allows users to fetch and display weather information directly in the terminal.
4. Icon Handling: Uses Pillow (PIL.Image and ImageTk) to fetch and display weather condition icons.
