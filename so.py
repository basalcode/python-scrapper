import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find_all("a", {"class": "s-pagination--item"})
    print(pages)


def get_jobs():
    last_page = get_last_page()
    return last_page