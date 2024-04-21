from bs4 import BeautifulSoup
from requests import get
from models.job import Job

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}


def get_pages(url):
    # extract the number of pages in the website

    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    pages = soup.find("ul", class_="bsj-nav").find_all("a", class_="page-numbers")

    # pages list empty when there is only one page
    return 1 if len(pages) == 0 else len(pages)


def scrape_bsj(keyword):
    url = f"https://berlinstartupjobs.com/skill-areas/{keyword}"

    pages_to_scrape = get_pages(url)

    jobs = []

    for i in range(pages_to_scrape):
        url_with_page = f"{url}/page/{i+1}"
        response = get(url_with_page, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        job_list = soup.find_all("div", class_="bjs-jlid__wrapper")

        for item in job_list:
            title = item.find("h4", class_="bjs-jlid__h").text
            company = item.find("a", class_="bjs-jlid__b").text
            link = item.find("h4", class_="bjs-jlid__h").find("a")["href"]

            job = Job(title, company, link)
            jobs.append(job)

    return jobs
