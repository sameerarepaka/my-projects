import requests
from bs4 import BeautifulSoup
url = "https://genius.com/Eminem-Mockingbird-lyrics"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
lyrics = soup.find('div',class_='Lyrics-sc-37019ee2-1 jRTEBZ').text.strip()
print(lyrics)

