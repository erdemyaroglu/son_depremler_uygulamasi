import requests
from bs4 import BeautifulSoup

def fetch_afad_data(limit=20):
    url = "https://deprem.afad.gov.tr/last-earthquakes.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")

    earthquakes = []
    for row in rows[1:limit+1]:  # Başlıktan sonraki ilk N satır
        cells = row.find_all("td")
        if cells:
            date = cells[0].text.strip()
            depth = cells[3].text.strip()
            magnitude = cells[5].text.strip()
            location = cells[6].text.strip()
            earthquakes.append((date, location, magnitude, depth))
    return earthquakes
