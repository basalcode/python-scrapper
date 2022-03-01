import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

# print(indded_result.text)
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination_list = indeed_soup.find("ul", {"class": "pagination-list"})

links = pagination_list.find_all("a")

pages = []

for link in links[:-1]:
    pages.append(int(link.string))

print(pages)