import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_weather_score(venue, date='2025-05-09'):
    """
    Fetch weather data for a venue on a given date.
    Returns a dictionary with weather score and conditions.
    Placeholder: Replace with NOAA or WeatherAPI integration.
    """
    try:
        # Hypothetical API call (e.g., NOAA or WeatherAPI)
        # Example: response = requests.get(f"https://api.weatherapi.com/v1/forecast.json?key=API_KEY&q={venue}&dt={date}")
        # For now, return static data based on Sutter Health Park, May 9, 2025
        weather_data = {
            'score': 80,  # 0-100, higher = HR-friendly
            'wind': '5 mph out',
            'temp': '70°F',
            'humidity': '50%'
        }
        logging.info(f"Weather score for {venue} on {date}: {weather_data['score']}")
        return weather_data
    except Exception as e:
        logging.error(f"Failed to fetch weather for {venue}: {e}")
        return {'score': 50, 'wind': 'unknown', 'temp': 'unknown', 'humidity': 'unknown'}
