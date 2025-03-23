import requests
url = f"https://dog.ceo/api/breeds/image/random"
response = requests.get(url)
if response.status_code == 200:
    print(response.json())
else:
    print("Unable to fetch")