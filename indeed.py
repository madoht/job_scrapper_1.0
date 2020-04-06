import requests
from bs4 import BeautifulSoup

URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&radius=100&l=%EC%84%9C%EC%9A%B8&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch"
LIMIT = 50

def extract_indeed_pages(): 
    indeed_result = requests.get(URL)   
    indeed_soup = BeautifulSoup(indeed_result.text, "html.parser") 
    pagination = indeed_soup.find("div", {"class" : "pagination"}) 
    links = pagination.find_all('a')   
    pages = []  
    for link in links[:-1]: 
        pages.append(int(link.string)) 

    max_pages = pages[-1]
    return max_pages

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start = {page * LIMIT}")
        print(result.status_code)
    return jobs