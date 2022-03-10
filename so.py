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

def extract_job(html):
    title = html.find("a", {"class": "s-link"}).string
    company = html.select("h3.fc-black-700 span:first-child")[0].string
    company = company is not None and company.strip("\n").strip("\r").rstrip()

    print(company)

    location = html.select("h3.fc-black-700 span:last-child")[0].string
    location = location.get_text(strip=True).strip("\r").strip("\n")
    job_id = html['data-jobid']

    return { "title": title, "company": company, "location": location, "link": f"https://stackoverflow.com/jobs/{job_id}" }

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser") 
        results = soup.find_all("div", {"class":"-job"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs