class Job:
    def __init__(self, title, company, link):
        self.title = title
        self.company = company
        self.link = link

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            + f"Company: {self.company}\n"
            + f"URL: {self.link}\n"
        )
