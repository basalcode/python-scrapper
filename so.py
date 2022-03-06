import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.select("a.s-pagination--item span")
    pages = pages[-2]
    return int(pages.text)

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})

        for result in results:
            print(result["data-jobid"])

def get_jobs():
    last_page = get_last_page()
    jos = extract_jobs(last_page)
    return last_page