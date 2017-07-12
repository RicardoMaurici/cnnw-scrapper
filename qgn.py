'''
This code needs newspaper 3k (https://github.com/codelucas/newspaper)
$ sudo apt-get install python3-pip
$ sudo apt-get install python-dev
$ sudo apt-get install libxml2-dev libxslt-dev
$ sudo apt-get install libjpeg-dev zlib1g-dev libpng12-dev
$ curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python3
$ pip3 install newspaper3k
'''


import requests
import time
from bs4 import BeautifulSoup
from random import randint
from newspaper import Article

def scrapper_gnews(query):
    s = '"'+query+'"' #Keywords for query
    s = s.replace(" ","+")
    url = "http://www.google.com.br/search?q=" + s + "&tbm=nws&tbs=qdr:y&lr=dlang_pt"  # URL for query of news results within one year and sort by date

    time.sleep(randint(0, 2))#waiting

    htmlpage = requests.get(url)
    soup = BeautifulSoup(htmlpage.text,'lxml')

    links = []

    for result_table in soup.findAll("div", {"class": "g"}):
        a_click = result_table.find("a")
        title = str(a_click.renderContents()).strip("b'")
        url = "https://www.google.com.br" + str(a_click.get("href"))
        brief = str(result_table.find("div", {"class": "st"}).renderContents()).strip("b'")

        # print("Title: " + title)
        # print("URL: " + url)
        # print("Brief: " + brief)

        links.append(url)

    return links

def scrapper_urls_from_gnews(url_list):
    list = []
    for url in url_list:
        #print(url)
        article = Article(url)
        article.download()
        dict = {}
        dict["url"] = url
        if (article.download() == None):
            article.html
            article.parse()
            dict["title"] = article.title
            dict["headline"] = article.summary
            dict["date"] = article.publish_date
            dict["body"] = article.text
            dict["category"] = article.keywords
        list.append(dict)

    return list

a = scrapper_gnews("formula1") # gets a list with googlenews links for query "formula1"
print(a)
b = scrapper_urls_from_gnews(a) # access links from list and puts the news(title, headline, date, body, category, url) into a list of dicts
print(b)