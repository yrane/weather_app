# weather_app
A weather app using OpenWeather Current API

- Provides an API facade to query the OpenWeatherMap "current conditions" API for either a zipcode or city name passed in as a parameter.

- Allows the API caller to pass in a query parameter specifying in which unit the temperature should be formatted (i.e. celsius, fahrenheit, or kelvin.

- Formats the returned data as a JSON object that includes: coordinates (lon / lat), current conditions (e.g. Cloudy, Sunny, etc), and current, high, and low temperatures for the current day in the requested unit.

