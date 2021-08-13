import requests as r
from bs4 import BeautifulSoup as bs

def links(url, number):
    univ_search = "?searchType=journalSearch&sort=PubDate&page="
    links_urls = [url+univ_search+str(i) for i in range(1, number + 1)]
    return links_urls
def os_handler():
    pass

def directory_creation(lst_links,topic):
    print(lst_links)
    globals()[f"Page_{len(lst_links)}"] = dict()
    for i,link in enumerate(lst_links):

        souping(r.get(link),headers = {'Accept-Language':'en-US,en;q=0.5'})

def souping(getlink, topic):
    soup = bs(getlink.content,"html.parser")
    all_articles = soup.find_all("article",{"class":"u-full-height c-card c-card--flush"})
    news_articles = []
    for i in all_articles:
        if i.find("span",{"class":"c-meta__type"}).text == topic:
            news_articles.append(i)
    print(news_articles[0])
    # names_of_files = list()
    # for x, i in enumerate(news_articles):
    #     main_page = "https://www.nature.com"
    #     small_soup = link(main_page+i.find("a")["href"])
    #     title =small_soup.find("title").text
    #     text_of_file = small_soup.find("div", {"class":"c-article-body u-clearfix"}).text.strip().replace("\n","")
    #     names_of_files.append(file_handling(title,text_of_file))
    # print(names_of_files)
    # return names_of_files


def file_handling(title,text):
    title = title.strip(",.-'´’?!").replace("’", "").replace(" ", "_")
    with open(f"{title}.txt", "w", encoding = "utf-8") as file:
        file.write(text)
    return file.name
def inputs():
    return int(input()),input()

def main():
    number, topic = 4, "Nature Briefing"
    name = "https://www.nature.com/nature/articles"
    lst_urls = links(name, number)
    directory_creation(lst_urls,topic)


if __name__ == "__main__":
    main()