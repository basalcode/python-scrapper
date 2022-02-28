import requests

indded_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

# print(indded_result.text)