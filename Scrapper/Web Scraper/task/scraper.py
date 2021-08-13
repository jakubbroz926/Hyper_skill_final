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
    all_articles = soup.find_all("article",{"class":"u-full-height c-card c-card--flush"})
    news_articles = []
    for i in all_articles:
        if i.find("span",{"class":"c-meta__type"}).text == "News":
            news_articles.append(i)
    names_of_files = list()
    for x, i in enumerate(news_articles):
        main_page = "https://www.nature.com"
        small_soup = link(main_page+i.find("a")["href"])
        title =small_soup.find("title").text
        text_of_file = small_soup.find("div", {"class":"c-article-body u-clearfix"}).text.strip().replace("\n","")
        names_of_files.append(file_handling(title,text_of_file))
    print(names_of_files)
    return names_of_files


def file_handling(title,text):
    title = title.strip(",.-'´’?!").replace("’", "").replace(" ","_")
    with open(f"{title}.txt", "w", encoding = "utf-8") as file:
        file.write(text)
    return file.name
def check(name):
    if 'title' in name:
        print(file_handling(link(name)))
    else:
        print('Invalid movie page!')
def main():
    name = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
    souping(link(name))


if __name__ == "__main__":
    main()