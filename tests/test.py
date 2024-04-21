from scrapers.scrape_bsj import scrape_bsj
from scrapers.scrape_web3 import scrape_web3
from scrapers.scrape_wwr import scrape_wwr

keyword = "java"
jobs = []


def scrape_bsj_test(keyword):
    jobs = scrape_bsj(keyword)

    for job in jobs:
        print(job)

    return


def scrape_web3_test(keyword):
    jobs = scrape_web3(keyword)

    for job in jobs:
        print(job)

    return


def scrape_wwr_test(keyword):
    jobs = scrape_wwr(keyword)

    for job in jobs:
        print(job)

    return


def all_test(keyword):
    jobs = scrape_bsj(keyword) + scrape_web3(keyword) + scrape_wwr(keyword)

    for job in jobs:
        print(job)

    return


# scrape_bsj_test(keyword)
# scrape_web3_test(keyword)
# scrape_wwr_test(keyword)

all_test(keyword)
