from genericpath import exists
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, 'html.parser')

    pagination_list = soup.find("ul", {"class": "pagination-list"})

    links = pagination_list.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]

    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0 * LIMIT}")
    
    soup = BeautifulSoup(result.text, 'html.parser')

    results = soup.find_all("table", {"class": "jobCard_mainContent"})
    
    for result in results:
        title = result.select("h2.jobTitle span:last-child")[0].text
        company = result.find("span", {"class": "companyName"}).string
        print(f"{title} - {company}")
    
    return jobs