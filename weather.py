import tkinter as tk
from tkinter import ttk
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        # Variables
        self.location_var = tk.StringVar()
        self.weather_data = {}

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Location Entry
        location_label = tk.Label(self.root, text="Enter Location:")
        location_label.grid(row=0, column=0, padx=10, pady=10)

        location_entry = tk.Entry(self.root, textvariable=self.location_var, width=30)
        location_entry.grid(row=0, column=1, padx=10, pady=10)

        # Get Weather Button
        get_weather_button = tk.Button(self.root, text="Get Weather", command=self.get_weather)
        get_weather_button.grid(row=0, column=2, padx=10, pady=10)

        # Weather Information Labels
        self.weather_labels = ttk.LabelFrame(self.root, text="Weather Information")
        self.weather_labels.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Labels for displaying weather information
        self.temperature_label = tk.Label(self.weather_labels, text="Temperature: ")
        self.temperature_label.grid(row=0, column=0, padx=10, pady=5)

        self.conditions_label = tk.Label(self.weather_labels, text="Conditions: ")
        self.conditions_label.grid(row=1, column=0, padx=10, pady=5)

        self.wind_speed_label = tk.Label(self.weather_labels, text="Wind Speed: ")
        self.wind_speed_label.grid(row=2, column=0, padx=10, pady=5)

    def get_weather(self):
        location = self.location_var.get()
        api_key = "2c4ce0e508a942b8e67d9748900040cf"
        api_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

        try:
            response = requests.get(api_url)
            data = response.json()

            # Extracting relevant weather information
            temperature = data['main']['temp']
            conditions = data['weather'][0]['description']
            wind_speed = data['wind']['speed']

            # Updating labels with weather information
            self.temperature_label.config(text=f"Temperature: {temperature}°C")
            self.conditions_label.config(text=f"Conditions: {conditions}")
            self.wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            # You can add error handling here, like displaying an error message to the user.

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
