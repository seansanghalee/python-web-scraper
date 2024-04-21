from bs4 import BeautifulSoup
from requests import get
from models.job import Job

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}


def get_pages(url):
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    page = (
        soup.find("ul", class_="pagination").find("li", class_="next").find("a")["href"]
    )

    total_pages = 1

    while page != "#":
        url = f"https://web3.career{page}"
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        page = (
            soup.find("ul", class_="pagination")
            .find("li", class_="next")
            .find("a")["href"]
        )
        total_pages += 1

    return total_pages


def scrape_web3(keyword):
    url = f"https://web3.career/{keyword}-jobs"

    pages_to_scrape = get_pages(url)

    jobs = []

    for i in range(pages_to_scrape):
        url_with_page = f"{url}/?page={i+1}"
        response = get(url_with_page, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        job_list = soup.find("tbody", class_="tbody").find_all("tr", class_="table_row")

        for item in job_list:
            if (
                item.find("div", class_="job-title-mobile").find("a").find("h2")
                is not None
            ):
                title = (
                    item.find("div", class_="job-title-mobile")
                    .find("a")
                    .find("h2")
                    .text
                )
                company = item.find("td", class_="job-location-mobile").find("h3").text
                link = f"https://web3.career{item.find("div", class_="job-title-mobile").find("a")["href"]}"
                job = Job(title, company, link)
                jobs.append(job)

    return jobs
