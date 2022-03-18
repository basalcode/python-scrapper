from genericpath import exists
import requests
from bs4 import BeautifulSoup

LIMIT = 50

def get_last_page(url):
    result = requests.get(url)

    soup = BeautifulSoup(result.text, 'html.parser')

    pagination_list = soup.find("ul", {"class": "pagination-list"})

    links = pagination_list.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]

    return max_page

def extract_job(html):
    title = html.select("h2.jobTitle span:last-child")[0].text
    company = html.find("span", {"class": "companyName"}).string
    location = html.find("div", {"class": "companyLocation"}).string
    job_id = html["data-jk"]

    return {"title": title, "company": company, "location": location, "link": f"https://www.indeed.com/viewjob?jk={job_id}"}

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={0 * LIMIT}")
        
        soup = BeautifulSoup(result.text, 'html.parser')

        results = soup.find_all("a", {"class": "sponTapItem"})
        
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    
    return jobs

def get_jobs(word):
    url = f"https://www.indeed.com/jobs?q={word}&limit={LIMIT}"
    last_pages = get_last_page(url)
    jobs = extract_jobs(last_pages)

    return jobs