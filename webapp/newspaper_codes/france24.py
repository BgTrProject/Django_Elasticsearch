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


class france24:
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
        for i in dates:  # 10958
            n_date = i.strftime("%Y/%m/%d")
            newdate = i.strftime("-%B-%Y")
            link = '{}{}{}'.format("https://www.france24.com/en/archives/", n_date, newdate)
            print(link)
            dizi.append(link)
        return dizi

    def get_link(self,url):
        req = self.scraper.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        links = soup.find_all("li", {"class": "o-archive-day__list__entry"})
        for i in links:
            h = i.find_all("a")
            for j in h:
                # print(j)
                ln = j.get("href")
                lnk = '{}{}'.format("https://www.france24.com", ln)
                if str(lnk.strip()).startswith("https://www.france24.com/en/video"):
                    pass
                else:
                    with open(self.link_filname, 'a') as file:
                        file.write(lnk + '\n')

    def creator(self,url):
        req = self.scraper.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        try:
            titl = soup.find("h1", {"class": "t-content__title a-page-title"})
            title = titl.getText()
        except:
            title = "None"
        try:
            dat = soup.find("time", {"pubdate": "pubdate"})
            date = dat.getText()
        except:
            date = "None"

        try:
            content_str = soup.find_all("p")
            txt = ""
            for i in content_str:
                h = i.getText()
                if h.startswith("Add France 24 to your") or h.startswith("© 2022 Copyright France 24") or h.startswith(
                        "Issued on:"):
                    pass
                else:
                    txt += i.getText().strip()
        except:
            txt = "None"
        w_data = "{};{};{};{}".format(url, date, title, txt)
        with open(self.content_filname, 'a') as file:
            file.write(w_data + '\n')


    # def main(self):
    #     print("************ started to collect page links")
    #
    #     self.page_links = self.dateCreator(self.date1, self.date2)
    #     print("-------- all links---")
    #
    #     for i in self.page_links:
    #         print(i)
    #         self.get_link(i.strip())
    #     print("reading links from {}.,.,.,.,.,.,.,.,.,.,. ".format(self.link_filname))
    #     with open(self.link_filname, 'r', newline='', encoding="utf-8") as f:
    #         for i in f.readlines():
    #             i = i.strip("\n")
    #             self.newsLinks.append(i)
    #
    #     print("-----------------------")
    #     print(self.content_filname)
    #     print(self.link_filname)
    #     print("-------------------------")
    #
    #     for i in self.newsLinks[:]:
    #         self.creator(i.strip())
    #
    #     print("Successfully!")


    def main(self):
        print("reading links from {}.,.,.,.,.,.,.,.,.,.,. ".format(self.link_filname))
        with open(self.link_filname, 'r', newline='', encoding="utf-8") as f:
            for i in f.readlines():
                i = i.strip("\n")
                self.newsLinks.append(i)

        for i in self.newsLinks[93496:]:
            self.creator(i.strip())

        print("Successfully!")







#
# #================================= create date========================
# url="https://www.france24.com/en/archives/2018/02/26-February-2018"
# d1="2018-02-26"
# d2="2018-02-27"
# a="france24"
# b="all"
# c="franc_deneme"
# dene=france24(d1,d2,b,a,c)
# dene.main()


#
# t1 = datetime.strptime(d1, '%Y-%m-%d').date()
# t2 = datetime.strptime(d2, '%Y-%m-%d').date()
# t = timedelta(days=1)
# dates = np.arange(t1, t2, t).astype(datetime)
# print(dates)
# for i in dates:  # 10958
#     n_date=i.strftime("%Y/%m/%d")
#     newdate = i.strftime("-%B-%Y")
#     link = '{}{}{}'.format("https://www.france24.com/en/archives/",n_date, newdate)
#     print(link)
#
#
#     ln = "{}{}".format(link, newdate)
#     print(ln)
#
# #__________________________________________________________________________
#
# #================================= get link ========================
# url="https://www.france24.com/en/archives/2018/02/26-February-2018"
# scraper = cloudscraper.create_scraper(delay=10, browser='firefox')
# req = scraper.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# # lnk=soup.find_all("div",{"class":"fc-item__content "}
#
# links = soup.find_all("li", {"class": "o-archive-day__list__entry"})
# for i in links:
#     h=i.find_all("a")
#     for j in h:
#         # print(j)
#         ln=j.get("href")
#         lnk='{}{}'.format("https://www.france24.com",ln)
#         if str(lnk.strip()).startswith("https://www.france24.com/en/video") or str(lnk.strip()).startswith("https://www.france24.com/en/mediawatch"):
#             pass
#         else:
#             print(lnk)
#
# print(links)
#
#
# # url="https://www.france24.com/en/mediawatch/20180226-2018-02-26-2046-media-watch"
# url="https://www.france24.com/en/20180226-congo-kinshasa-two-killed-crackdown-kabila-protest-march"
# scraper = cloudscraper.create_scraper(delay=10, browser='firefox')
# req = scraper.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# try:
#     titl=soup.find("h1",{"class":"t-content__title a-page-title"})
#     title=titl.getText()
# except:
#     title="None"
# try:
#     dat=soup.find("time",{"pubdate":"pubdate"})
#     date=dat.getText()
# except:
#     date="None"
#
# try:
#     content_str=soup.find_all("p")
#     txt=""
#     for i in content_str:
#         h=i.getText()
#         if h.startswith("Add France 24 to your") or h.startswith("© 2022 Copyright France 24") or h.startswith("Issued on:"):
#             pass
#         else:
#             txt +=i.getText().strip()
# except:
#     txt="None"
# w_data = "{};{};{};{}".format(url, date, title, txt)
# with open(self.content_filname, 'a') as file:
#     file.write(w_data + '\n')
#
# print("==============================")
# print(txt)
# print("==============================")