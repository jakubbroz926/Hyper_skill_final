import requests as r
from bs4 import BeautifulSoup as bs

def link(url):
    url_link = r.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if url_link.status_code != 200:
        print(f"The URL returned {url_link.status_code}!")
        return None
    else:
        soup = url_link.content
        #soup = bs(url_link.content, 'html.parser')
        return soup


def souping(soup):
    result = dict()
    result['title'] = soup.find('title').text
    result['description'] = soup.find('meta',{'name':'description'})['content']# Napsat title and meta name description
    return result


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
    name = input("Input the URL:")
    print(file_handling(link(name)))


if __name__ == "__main__":
    main()