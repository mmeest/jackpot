import requests
from bs4 import BeautifulSoup

loosimiste_arv = 1

viking_url = "https://www.eestiloto.ee/tulemused?game=vikinglotto"

result = requests.get(viking_url)

print("HTTP staatus:", result.status_code)

soup = BeautifulSoup(result.text, "html.parser")

print(soup.prettify())
