import shutil
import requests as r
from bs4 import BeautifulSoup as Bs
import os


def links(url, number):
    univ_search = "?searchType=journalSearch&sort=PubDate&page="
    links_urls = [url + univ_search + str(i) for i in range(1, number + 1)]
    return links_urls


def directory_creation(lst_links, topic):
    for i, link in enumerate(lst_links):
        names_of_txts, texts = souping(r.get(link), topic)
        file_handling(names_of_txts, texts, i + 1)
    print("Saved all articles.")


def souping(getlink, topic):
    soup = Bs(getlink.content, "html.parser")
    all_articles = soup.find_all("article", {"class": "u-full-height c-card c-card--flush"})
    news_articles = []
    for i in all_articles:
        if i.find("span", {"class": "c-meta__type"}).text == topic:
            news_articles.append(i)
    names_of_txts = list()
    texts = list()
    for i in news_articles:
        names_of_txts.append(i.find("a").text.strip("-").replace(":", "").replace(" ", "_"))
        url = "https://www.nature.com" + i.find("a")["href"]
        small_soup = Bs(r.get(url).content, "html.parser")
        texts.append(
            small_soup.find("div", {"class": "article-item__body"}).text)
#There are some possibly missing class types, which would be needed for different topics
    return names_of_txts, texts


def file_handling(titles, texts, number):
    os.mkdir(f"Page_{number}")
    os.chdir(f"Page_{number}")
    for i, (title, text) in enumerate(zip(titles, texts)):
        with open(f"{title}.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(line for line in text.strip().splitlines() if line != ''))
            file.flush()
    os.chdir("..")


def inputs():
    return int(input()), input()


def clear():
    for i in os.listdir():
        if "Page" in i:
            shutil.rmtree(i)


def main():
    number, topic, = int(input("Number of pages")), input()
    name = "https://www.nature.com/nature/articles"
    lst_urls = links(name, number)
    directory_creation(lst_urls, topic)


if __name__ == "__main__":
    if input("Do you want cleat your root folder? If yes, type c for clear: ") == "c":
        clear()

    else:
        main()