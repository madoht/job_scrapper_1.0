import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs/developer-jobs-using-python?pg=i"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "pagination"}).find_all("a")
    print(pages)

def get_jobs():
    last_page = get_last_page()
    return []