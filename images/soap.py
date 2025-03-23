from bs4 import BeautifulSoup
import requests

url = "https://genius.com/Lil-tecca-taste-lyrics"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Look for divs containing the lyrics
lyrics_divs = soup.find_all('div', class_=lambda c: c and 'Lyrics__Container' in c)

# Extract the text from all the divs found
lyrics = ""
for div in lyrics_divs:
    lyrics += div.get_text(separator="\n", strip=True) + "\n\n"

if lyrics:
    print(lyrics)
else:
    print("No lyrics found")
