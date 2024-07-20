import requests
from bs4 import BeautifulSoup

def history_scraper():
    url = "https://www.britannica.com/on-this-day"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    history_events = soup.find_all(class_ = "featured-event-card card")

    for event in history_events:

        hist_title = event.find(class_ = "title font-18 font-weight-bold mb-10").get_text()
        hist_body = event.find(class_ = "description font-serif").get_text()

    return hist_title, hist_body

if __name__ == "__main__":

    hist_title, hist_body = history_scraper()

    print(f"\n{hist_title}\n{hist_body}\n")