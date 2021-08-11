import requests as r
from bs4 import BeautifulSoup as bs

def link(url):
    url_link = r.get(url,headers={'Accept-Language': 'en-US,en;q=0.5'})
    if url_link.status_code == 200:
        soup = bs(url_link.content, 'html.parser')
        return soup


def souping(soup):
    result = dict()
    result['title'] = soup.find('title').text
    result['description'] = soup.find('meta',{'name':'description'})['content']# Napsat title and meta name description
    return result

def main():
    name = input()
    if 'title' in name:
        print(souping(link(name)))
    else:
        print('Invalid movie page!')

if __name__ == "__main__":
    main()