import requests

api_key = "611945d59b2a05421ba08e8e05d3333f"
city = "Auckland"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

complete_url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(complete_url)
data = response.json()

print(data)  # Debugging: Print the entire response

if data.get("cod") != "404":
    main = data.get("main")
    weather = data.get("weather")[0] if data.get("weather") else None

    if main and weather:
        temperature = main.get("temp")
        pressure = main.get("pressure")
        humidity = main.get("humidity")
        description = weather.get("description")

        print(f"Temperature: {temperature}")
        print(f"Pressure: {pressure}")
        print(f"Humidity: {humidity}")
        print(f"Weather description: {description}")
    else:
        print("Error: Incomplete data received from API")
else:
    print("City Not Found!")