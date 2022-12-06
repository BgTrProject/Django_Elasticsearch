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
from datetime import datetime, timedelta, date
import os
import csv
import concurrent
import multiprocessing
from multiprocessing import pool
import io
from pprint import pprint
import cloudscraper


class nytimes:
    def __init__(self,date1,date2,categ,filname,dirname,**kwargs):
        self.date1=date1
        self.date2=date2
        self.categ=categ
        self.filname=filname
        self.dirname=dirname
        self.page_links=[]
        self.content_filname=""
        self.link_filname=""
        self.scraper = cloudscraper.create_scraper(delay=10, browser='firefox')


        self.newsLinks = []

        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        print(desktop)


        print(self.filname)
        ff = str(filname)

        self.filname = desktop[:-7] + "PycharmProjects/elastic/webapp/g_upload/{}/{}_".format(self.dirname,
                                                                                     self.dirname) + ff  # +"/"+ff
        self.content_filname = self.filname + "_content.txt"
        self.link_filname = self.filname + "_link.txt"
        print(self.link_filname)


    def dateCreator(self,d1,d2):
        dizi = []
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        # print(dates)
        for i in dates:
            # print(i)
            h = i + timedelta(days=1)  # 10958
            startdate = i.strftime("%Y%m%d")
            enddate = h.strftime("%Y%m%d")
            link = 'https://www.nytimes.com/search?dropmab=false&endDate={}&query=&sections={}|nyt%3A%2F%2Fsection%2F4224240f-b1ab-50bd-881f-782d6a3bc527&sort=oldest&startDate={}&types=article'.format(enddate, self.categ, startdate)

            dizi.append(link)
        return dizi

    def get_link(self,url):
        req = self.scraper.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        links = soup.find_all("li", {"class": "css-1l4w6pd"})
        for i in links:
            h = i.find_all("a")
            lnk=""
            for j in h:
                # print(j)
                ln = j.get("href")
                if str(ln.strip()).startswith("http"):
                    lnk=ln
                else:
                # print(ln)
                    lnk = '{}{}'.format("https://www.nytimes.com", ln)

                with open(self.link_filname, 'a') as file:
                    file.write(lnk + '\n')

    def creator(self,url):
        req = self.scraper.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        try:
            titl = soup.find("h1")
            title = titl.getText()
            title = title.replace(";", ":")
        except:
            title = "None"
        # print(title)
        try:
            dat = soup.find("time")
            date = dat.getText()
        except:
            date = "None"
        # print(date)

        try:
            # content_str = soup.find_all("p")
            content_str = soup.find_all("p", {"class": "css-at9mc1 evys1bk0"})
            if len(content_str)==0:
                content_str = soup.find_all("p", {"class": "story-body-text"})
            else:
                pass
            txt = ""
            for i in content_str:
                # print(i.getText())
                txt += i.getText().strip()
                txt = txt.replace(";", ":")
        except:
            txt = "None"
        # print(txt)
        w_data = "{} ; {} ; {} ; {}".format(url, date, title, txt)
        with open(self.content_filname, 'a') as file:
            file.write(w_data + '\n')


    def main(self):
        print("************ started to collect page links")

        self.page_links = self.dateCreator(self.date1, self.date2)
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



#
# ==============================create date
# import datetime
# from datetime import datetime, timedelta, date
# import os
# import numpy as np
# categ="technology"
# # url="https://www.nytimes.com/search?dropmab=false&endDate=20000103&query=&sections=Technology|nyt%3A%2F%2Fsection%2F4224240f-b1ab-50bd-881f-782d6a3bc527&sort=oldest&startDate=20000102&types=article"
# d1="1980-01-01"
# d2="1980-01-05"
# t1 = datetime.strptime(d1, '%Y-%m-%d').date()
# t2 = datetime.strptime(d2, '%Y-%m-%d').date()
# t = timedelta(days=1)
# dates = np.arange(t1, t2, t).astype(datetime)
# # print(dates)
# for i in dates:
#     # print(i)
#     h=i+timedelta(days=1)# 10958
#     startdate = i.strftime("%Y%m%d")
#     enddate = h.strftime("%Y%m%d")
#     n_url='https://www.nytimes.com/search?dropmab=false&endDate={}&query=&sections={}|nyt%3A%2F%2Fsection%2F4224240f-b1ab-50bd-881f-782d6a3bc527&sort=oldest&startDate={}&types=article'.format(enddate,categ,startdate)
#
#     print(n_url)


# ==================================== get_link
# import cloudscraper
# url="https://www.nytimes.com/search?dropmab=false&endDate=20000102&query=&sections=technology|nyt%3A%2F%2Fsection%2F4224240f-b1ab-50bd-881f-782d6a3bc527&sort=oldest&startDate=20000101&types=article"
# scraper = cloudscraper.create_scraper(delay=10, browser='firefox')
# req = scraper.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# links = soup.find_all("li", {"class": "css-1l4w6pd"})
# for i in links:
#     h = i.find_all("a")
#     for j in h:
#         # print(j)
#         ln = j.get("href")
#         # print(ln)
#         lnk = '{}{}'.format("https://www.nytimes.com", ln)
#         print(lnk)
#
#
#
# ================================Creator
# url="https://www.nytimes.com/2000/01/01/technology/visions-technology-quantum-computers-cars-smarter-than-you-are-new-meaning-for.html?searchResultPosition=2"
# url="https://www.nytimes.com/2000/01/01/technology/the-new-york-times-cybercrime.html?searchResultPosition=9"
# url="https://www.nytimes.com/2000/01/01/technology/visions-technology-quantum-computers-cars-smarter-than-you-are-new-meaning-for.html?searchResultPosition=2"
# url="https://archive.nytimes.com/bits.blogs.nytimes.com/2008/10/14/server-maker-to-the-stars-cuts-revenue-forecast/?searchResultPosition=9"
# scraper = cloudscraper.create_scraper(delay=10, browser='firefox')
# req = scraper.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# content_str = soup.find_all("p", {"class": "story-body-text"})
# tt=""
# for i in content_str:
#     h=i.getText()
#     h=h.stripped_string
#     tt+=str(h)
# print(tt)
#
# try:
#     # content_str = soup.find_all("p")
#     # content_str = soup.find_all("p",{"class":"css-at9mc1 evys1bk0"})
#     content_str = soup.find_all("p", {"class": "story-body-text"})
#     txt = ""
#
#     for i in content_str:
#         # h=i.stripped_strings
#
#         print(i.getText().strip())
#         print("--------------------------------------------------------------------------------------")
#         txt += i.getText().lstrip()
#         # txt=txt.strip().replace(";",":")
# except:
#     txt="None"
# print(txt.strip())
# content_str = soup.find_all("p",{"class":"css-at9mc1 evys1bk0"})


# try:
#     titl = soup.find("h1")
#     title = titl.getText()
#     title=title.replace(";",":")
# except:
#     title = "None"
# # print(title)
# try:
#     dat = soup.find("time")
#     date = dat.getText()
# except:
#     date = "None"
# # print(date)


#
# w_data = "{} ; {} ; {} ; {}".format(url, date, title, txt)
# print(w_data)