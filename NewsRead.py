import requests
from bs4 import BeautifulSoup

def latestnews():
    url = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    headlines = soup.find_all("a", class_="DY5T1d RZIKme")

    for index, headline in enumerate(headlines[:10], start=1):
        print(f"{index}. {headline.get_text()}")
