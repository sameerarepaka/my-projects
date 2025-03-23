import requests
api_key = "8c8e32d7c17360caeddb370445620c8d"
city = "Palakollu"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
if response.status_code == 200:
    weather_data = response.json()
    print(f"Temperature:{weather_data['main']['temp']}k")
    print(f"Weather:{weather_data['weather'][0]['description']}")
else:
    print("Failed to fetch data")

