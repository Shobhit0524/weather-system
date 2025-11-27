import requests
import os
import time

API_KEY = "22ae137c9e3871d238ed4eafeaaf34c6" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def weather_warning_from_code(weather):
    """Return a weather warning and tip based on the weather condition ID."""
    if not weather:
        return ("No data available", "")
    w = weather[0]
    wid = int(w.get("id", 0))
    desc = w.get("description", "")
    main = w.get("main", "").lower()

    if 200 <= wid <= 232:
        return ("Thunderstorm Alert!", "Stay indoors and unplug electronics.")
    elif 300 <= wid <= 321:
        return ("Light Drizzle", "Take a raincoat just in case.")
    elif 500 <= wid <= 531:
        return ("Rainy Weather", "Carry an umbrella and watch for slippery roads.")
    elif 600 <= wid <= 622:
        return ("❄ Snowfall", "Dress warmly and avoid driving if possible.")
    elif 701 <= wid <= 781:
        return ("Low Visibility", "Drive slowly and keep headlights on.")
    elif wid == 800:
        return ("Clear Skies", "Perfect day to go out and enjoy!")
    elif 801 <= wid <= 804:
        return ("Cloudy", "Cool and calm weather. Maybe take a walk.")
    else:
        return (desc.title() or "General Weather", "")


def fetch_weather(city):
    """Fetch current weather for the given city."""
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        res = requests.get(BASE_URL, params=params, timeout=10)
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 401:
            raise RuntimeError("Invalid API key.")
        elif res.status_code == 404:
            raise RuntimeError("City not found.")
        else:
            raise RuntimeError(f"HTTP {res.status_code}: {res.text}")
    except Exception as e:
        print("Error fetching data:", e)
        return None


def print_weather(data):
    """Display weather data nicely in terminal."""
    if not data:
        return
    name = f"{data.get('name','?')}, {data.get('sys',{}).get('country','')}"
    main = data.get("main", {})
    w = data.get("weather", [{}])[0]
    wind = data.get("wind", {})

    print(f"\nWeather for {name}")
    print("-" * (12 + len(name)))
    print(f"{w.get('main','')} — {w.get('description','')}")
    print(f"Temperature: {main.get('temp','?')} °C (feels like {main.get('feels_like','?')} °C)")
    print(f"Humidity: {main.get('humidity','?')}%")
    print(f"Wind speed: {wind.get('speed','?')} m/s")

    warning, tip = weather_warning_from_code(data.get("weather", []))
    print(f"\n{warning}")
    if tip:
        print(f"Tip: {tip}")
    print("-" * 50)


def main():
    print("=== Terminal Weather App ===")
    print("(Type 'exit' or 'quit' to stop)")
    while True:
        city = input("\nEnter city name: ").strip()
        if city.lower() in ("exit", "quit"):
            print("Goodbye.")
            break
        data = fetch_weather(city)
        print_weather(data)
        time.sleep(1)


if __name__ == "__main__":
    main()
