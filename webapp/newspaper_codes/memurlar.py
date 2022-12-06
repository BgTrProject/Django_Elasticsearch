import os
import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import time
import urllib.request
import re
import urllib3
from pandas import DataFrame
import csv
import datetime
from datetime import datetime, timedelta ,date
class memurlar:
    def __init__(self, date1, date2, categ, filname, dirname,count, **kwargs):
        self.date1 = date1
        self.date2 = date2
        self.categ = categ
        self.filname = filname
        self.dirname = dirname
        self.page_links = []
        self.content_filname = ""
        self.link_filname = ""

        self.newsLinks = []

        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)

        print(self.filname)
        ff = str(filname)

        self.filname = desktop[:-7] + "PycharmProjects/elastic/webapp/g_upload/{}/{}_".format(self.dirname,
                                                                                     self.dirname) + ff  # +"/"+ff
        self.content_filname = self.filname + "_content.txt"
        self.count = count
        self.link_filname = self.filname + self.count + "_link.txt"
        print(self.link_filname)

    def dateCreator(self,d1,d2):
        lnk1 = "https://www.memurlar.net/mansetler/default.aspx?typeid=3&page="  # 3098 sayfa , typeid 1,2,3 aynı , 2012 yılına kadar gidiyor...
        lnk2 = "https://www.memurlar.net/mansetler/default.aspx?typeid=4&page="  # 1075 sayfa , 2003 yılına kadar gidiyor..
        lnk3 = "https://www.memurlar.net/sonhaberler/?date={}"
        sonhaber_pages = []
        # for a in range(1, 3099, 1):
        #     a = str(a)
        #     link1 = lnk1 + a
        #     manset1_pages.append(link1)
        # for b in range(1, 1076, 1):
        #     b = str(b)
        #     link2 = lnk2 + b
        #     manset2_pages.append(link2)

        # t1 = datetime(2003, 4, 15)
        # t2 = datetime(2021, 8, 1)
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)

        for j in dates:
            link3 = (lnk3.format(j.strftime('%Y/%m/%d')))

            sonhaber_pages.append(link3)
        return sonhaber_pages

    def get_link(self,link):
        html = requests.get(link).content
        soup = BeautifulSoup(html, "html.parser")
        # list = soup.find_all("div", {"class": "category-news"})
        # list = soup.find_all("div", {"class": "content-items list"})
        # for i in list:
        #     if i == "":
        #         break
        #     else:
        #         href = i.find("a").get("href")
        #         href = "https://www.memurlar.net" + href
        list3 = soup.find_all("a", {"class": "img-left item ma:b:2x"})
        for i in list3:
            hr=i.get("href")
            href = "https://www.memurlar.net" + hr
            with open(self.link_filname, "a", encoding="utf-8") as file:
                file.write(href + "\n")

    def creator(self,url):
        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        # title = soup.find("div", {"class": "DetailPage"}).find("h1").getText()# Çalışıyor
        try:
            title = soup.find("h1", {"class": "title"}).getText()
        except:
            title = "None"
        try:
            date = soup.find("time", {"class": "ma:l"})  # Çalışıyor.
            date = date.get("datetime")
            date = date.split("T")
            date = date[0]
        except:
            date = "None"
        # categori = soup.find("div", {"class": "detail"}).find_all("p")  # Çalışıyor
        # for i in categori:
        #
        #     if i.getText().startswith("Anasayfa") and i.startswith("..."):
        #         break
        #     else:
        #         cat = i.getText()
        try:
            content = soup.find("div", {"class": "detail"}).find_all("p")
            h = ""
            z = ""
            for w in content:
                w = w.getText().replace(" ", " ")
                z = " ".join(w.split())
                h += z
                h = h.strip("googletag.cmd.push(function() { googletag.display('div-gpt-ad-1560331211068-1'); })")
        except:
            h = "None"
        sentence = "{} ; {} ; {} ; {}".format(url, date, title, h)  # çıkarıldı cat,
        with open(self.content_filname, "a", encoding="utf-8") as file:
            file.write(sentence + "\n")

    def main(self):
        print("************ started to collect page links")

        self.page_links=self.dateCreator(self.date1,self.date2)
        print("-------- all links---")


        for i in self.page_links:
            print(i)
            self.get_link(i.strip())
        print("reading links from {}.,.,.,.,.,.,.,.,.,.,. ".format(self.link_filname))
        with open(self.link_filname, 'r', newline='', encoding="utf-8") as f:
            for i in f.readlines():
                i = i.strip("\n")
                self.newsLinks.append(i)


        print("-----------------------")
        print(self.content_filname)
        print(self.link_filname)
        print("-------------------------")

        for i in self.newsLinks[:]:
            self.creator(i.strip())

        print("Successfully!")






    # def get_link(self,link):
    #     import cloudscraper
    #     scraper = cloudscraper.create_scraper(delay=10, browser='firefox')
    #
    #     link='https://www.memurlar.net/sonhaberler/?date=2020/10/10'
    #     req = scraper.get(link)
    #     soup = BeautifulSoup(req.text, "lxml")
    #     # r = requests.get(link)
    #     # soup = BeautifulSoup(r.content, 'html5lib')
    #     list = soup.find_all("div", {"class": "last-news hide"})
    #
    #     for i in list:
    #         h=i.find("a")
    #         print(h.get("href"))
    #
    #     list2 = soup.find_all("div", {"class": "content-items list"})
    #
    #     for i in list2:
    #         print("-----------")
    #         h = i.find("a")
    #         print(h.get("href"))
    #
    #     list3=soup.find_all("a",{"class":"img-left item ma:b:2x"})
    #     for i in list3:
    #         print(i.get("href"))

                # href = i.find("a").get("href")
                # href = "https://www.memurlar.net" + href
                # print(href)


    # url='https://www.memurlar.net/haber/884871/egitime-kar-engeli-36-sehirde-okullar-tatil.html'
    # url="https://www.memurlar.net/haber/931486/yargitay-satin-alinan-dairedeki-kusur-icin-muhendisten-gorus-alinmali.html"
    # html = requests.get(url).content
    # soup = BeautifulSoup(html, "html.parser")
    # # title = soup.find("div", {"class": "DetailPage"}).find("h1").getText()# Çalışıyor
    # try:
    #     title = soup.find("h1", {"class": "title"}).getText()
    # except:
    #     title="None"
    # print(title)
    # try:
    #     date = soup.find("time", {"class": "ma:l"})  # Çalışıyor.
    #     date = date.get("datetime")
    #     date=date.split("T")
    #     date=date[0]
    # except:
    #     date="None"
    # print(date)
    #
    # # date = date[9:-6]
    # # print(date.strip())
    # #
    # # categori = soup.find("div", {"class": "detail"}).find_all("p")  # Çalışıyor
    # # for i in categori:
    # #
    # #     if i.getText().startswith("Anasayfa") and i.startswith("..."):
    # #         break
    # #     else:
    # #         cat = i.getText()
    # try:
    #     content = soup.find("div", {"class": "detail"}).find_all("p")
    #     h = ""
    #     z = ""
    #     for w in content:
    #         w = w.getText().replace(" ", " ")
    #         z = " ".join(w.split())
    #         h += z
    #         h = h.strip("googletag.cmd.push(function() { googletag.display('div-gpt-ad-1560331211068-1'); })")
    # except:
    #     h="None"
    # sentence = "{} ; {} ; {} ; {}".format(url,  date, title, h) #çıkarıldı cat,
    # print(sentence)

#
# html = requests.get(link).content
# soup = BeautifulSoup(html, "html.parser")
# # list = soup.find_all("div", {"class": "category-news"})
# # list = soup.find_all("div", {"class": "content-items list"})
# # for i in list:
# #     if i == "":
# #         break
# #     else:
# #         href = i.find("a").get("href")
# #         href = "https://www.memurlar.net" + href
# list3 = soup.find_all("a", {"class": "img-left item ma:b:2x"})
# for i in list3:
#     hr=i.get("href")
#     href = "https://www.memurlar.net" + hr
#     print(href)
#
# date