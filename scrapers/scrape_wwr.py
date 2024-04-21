from bs4 import BeautifulSoup
from requests import get
from models.job import Job

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}


def scrape_wwr(keyword):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=✓&term={keyword}"

    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    job_list = soup.find("div", class_="jobs-container").find_all("li")

    jobs = []

    for item in job_list:
        if item.get("class") != ["view-all"]:
            title = item.find("span", class_="title").text
            company = item.find("span", class_="company").text
            link = f"https://weworkremotely.com{item.find("a").find_next("a")["href"]}"

            job = Job(title, company, link)
            jobs.append(job)

    return jobs
