import requests as r
from bs4 import BeautifulSoup as bs

def link(url):
    url_link = r.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if url_link.status_code != 200:
        print(f"The URL returned {url_link.status_code}!")
        return None
    else:
        #soup = url_link.content
        soup = bs(url_link.content, 'html.parser')
        return soup


def souping(soup):
    result = dict()
    all_articles = soup.find_all("article",{"class":"u-full-height c-card c-card--flush"})
    news_articles = []
    for i in all_articles:
        if i.find("span",{"class":"c-meta__type"}).text == "News":
            news_articles.append(i)
    for x,i in enumerate(news_articles):
        print(x,i.find("a").get("href"))
    print(news_articles)
            #pro každý link z new_articles zavolat nový link, vysekat titul a tělo článku a uložito ho


def file_handling(page_content):
    if page_content is not None:
        file_html = open("source.html", "wb")
        file_html.write(page_content)
        file_html.close()
        return "Content saved."
def check(name):
    if 'title' in name:
        print(file_handling(link(name)))
    else:
        print('Invalid movie page!')
def main():
    name = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
    print(souping(link(name)))


if __name__ == "__main__":
    main()