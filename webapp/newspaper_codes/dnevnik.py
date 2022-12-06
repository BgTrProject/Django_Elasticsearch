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
from datetime import datetime, timedelta,time,date
import concurrent.futures
import os
import csv
import concurrent
import multiprocessing
from multiprocessing import pool
import io
from pprint import pprint

class dnevnik:
    def __init__(self,date1,date2,categ,filname,dirname,**kwargs):
        self.date1=date1
        self.date2=date2
        self.categ=categ
        self.filname=filname
        self.dirname=dirname
        self.page_links=[]
        self.content_filname=""
        self.link_filname=""


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
        # t1 = datetime(2002, 4, 3)  # en son 2001/02/11 e kadar çalışıyo
        # t2 = datetime(2002, 4, 5)
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        links = []
        link = "https://www.dnevnik.bg/novini/"
        for i in dates:
            newdate = i.strftime('%Y/%m/%d')
            links.append("{}{}{}".format(link, newdate, '/'))
        return links

    def get_link(self,i):
        r = requests.get(i)
        soup = BeautifulSoup(r.content, 'html5lib')
        lnks = soup.find_all("article", attrs={"class": "secondary-article-v2 border-top list-item"})
        try:
            for i in lnks:
                link = '{}{}'.format("https://www.dnevnik.bg", i.find("a").get("href"))
                with open(self.link_filname, 'a') as file:
                    file.write(link + '\n')


            # count = 0
            # for a in soup.find_all('a', href=True):
            #     link = a['href']
            #     count += 1
            #     result = link.startswith(
            #         ('/', 'java', 'https://www.dnevnik.bg/photos/', '#', 'https://www.dnevnik.bg/print/'), 0, 30)
            #     if result == False:
            #         if len(link) > 28:
            #             print(link)
            #             result2 = link.startswith('https://www.dnevnik.bg/')
            #             if result2 == True:
            #                 result3 = link.endswith(('#comments', 'kontakti/'))
            #                 if result3 == False and count % 2 == 1:
            #                     print(link)
            #                     with open(self.link_filname, 'a') as file:
            #                         file.write(link + '\n')
            #                 else:
            #                     pass
            #             else:
            #                 pass
            #         else:
            #             pass
            #     else:
            #         pass
        except:
            pass

    def creator(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        try:
            title = soup.find("h1").getText()
            title = title.split()
            for w in title:
                title_string = title_string + " " + w
        except:
            title_string="None"

            # category = soup.find("span", attrs = {"itemprop":"name"}).getText()
            # print(category)
        try:
            date = soup.find("time", attrs={"itemprop": "datePublished"}).getText()
            date = date.split()
            date = date[1] + date[2] + date[3]
        except:
            date="None"

        try:
            content_array = soup.find("div", attrs={"class": "article-content"}).getText()
            content_array = content_array.split()
            content_string = ""
            title_string = ""

            for w in content_array:
                content_string = content_string + " " + w
        except:
            content_string="None"
                # w_data = url+";"+date+";"+title+";"+content_string
        w_data = "{};{};{};{}".format(url, date, title_string, content_string)
        # write_to_txt(w_data)
        with open(self.content_filname, 'a') as file:
            file.write(w_data + '\n')



    def main(self):
        print("*********************")
        print(self.categ)
        print(self.date1)
        print(self.date2)
        self.page_links=self.dateCreator(self.date1,self.date2)
        for i in self.page_links[:]:
            print(i)
            print("*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-**--*-*-*-*-")

        for i in self.page_links:
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
# url="https://www.dnevnik.bg/novini/2020/10/10/"
# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html5lib')
# lnks=soup.find_all("article", attrs={"class": "secondary-article-v2 border-top list-item"})
# c=0
# for i in lnks:
#     c+=1
#     link='{}{}'.format("https://www.dnevnik.bg",i.find("a").get("href"))
#     print(link)
# print(c)