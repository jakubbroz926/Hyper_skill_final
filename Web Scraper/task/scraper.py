import requests as r


def link(url):
    url_link = r.get(url)
    if url_link.status_code == 200:
        try:
            print(url_link.json()["content"])
        except BaseException:
            print("Invalid quote resource!")
    else:
            print("Invalid quote resource!")

def main():
    link(input("Input the URL:"))

if __name__ == "__main__":
    main()