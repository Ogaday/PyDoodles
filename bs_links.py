# A script to find the links in the beautiful soup homepage (without using
# beautiful soup!?)

import requests

from brackets import pairs



if __name__=="__main__":
    r = requests.get("http://www.crummy.com/software/BeautifulSoup/")
    page = str(r.content, encoding = "utf-8")

    links = []
    for i, j in pairs(page):
        if page[i:i+6] == "a href":
            links.append(page[i:j])

            for link in links:
        print(link[8:-1])