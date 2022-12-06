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
from datetime import datetime, timedelta
import os
import csv
import concurrent
import multiprocessing
from multiprocessing import pool
import io
from pprint import pprint

class sozcu:
    def __init__(self, date1, date2, categ, filname, dirname, **kwargs):
        self.date1 = date1
        self.date2 = date2
        self.categ = categ
        if self.categ != 'gundem' or self.categ != 'dunya':
            self.categ='teknoloji'
        elif str(self.categ)=='all':
            self.categ="teknoloji"
        else:
            self.categ=categ
        print(self.categ)
            # self.categ = categ
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
        self.link_filname = self.filname + "_link.txt"
        print(self.link_filname)
        self.dizi=[]
    # def __init__(self,date1,date2,categ,filname,dirname,**kwargs):
    #     self.date1=date1
    #     self.date2=date2
    #     self.categ=categ
    #     self.dizi=[]
    #     print(categ)
    #     print(self.categ)
    #     self.filname = filname
    #     self.dirname = dirname
    #
    #     if self.categ!='gundem' or self.categ!='dunya':
    #         self.categ='teknoloji'
    #     elif str(self.categ)=='all':
    #         self.categ="teknoloji"
    #     else:
    #         self.categ=categ
    #     # self.categ = categ
    #
    #     self.page_links = []
    #     self.content_filname = ""
    #     self.link_filname = ""
    #
    #     self.newsLinks = []
    #
    #     desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    #     print(desktop)
    #
    #     print(self.filname)
    #     ff = str(filname)
    #
    #     self.filname = desktop[:-7] + "PycharmProjects/elastic/webapp/g_upload/{}/{}_".format(self.dirname,
    #                                                                                           self.dirname) + ff  # +"/"+ff
    #     self.content_filname = self.filname + "_content.txt"
    #     self.link_filname = self.filname + "_link.txt"
    #     print(self.link_filname)

    def dateCreator(self,d1,d2):

        # t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        # t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        # t = timedelta(days=1)
        # dates = np.arange(t1, t2, t).astype(datetime)
        # gundem_links = []
        # dunya_links = []
        # ekonomi_links = []
        # otomotiv_links = []
        # saglik_links = []
        # egitim_links = []
        # teknoloji_links = []

        gundem = "https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPalk2SW1kMWJtUmxiU0k3Y3pvNU9pSndiM04wWDNSNWNHVWlPM002TkRvaWNHOXpkQ0k3ZlE9PQ==/"  # 8146 sayfa
        dunya = "https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPalU2SW1SMWJubGhJanR6T2prNkluQnZjM1JmZEhsd1pTSTdjem8wT2lKd2IzTjBJanQ5/"  # 1895
        ekonomi = "https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPamM2SW1WcmIyNXZiV2tpTzNNNk9Ub2ljRzl6ZEY5MGVYQmxJanR6T2pRNkluQnZjM1FpTzMwPQ==/"  # 1474
        otomotiv = "https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPamc2SW05MGIyMXZkR2wySWp0ek9qazZJbkJ2YzNSZmRIbHdaU0k3Y3pvME9pSndiM04wSWp0OQ==/"  # 175
        saglik = ""  # hatalı sayfa ama açık bıraktım aşağıdaki yorum satırında olan prosesleri açıp doğru bi link girilince çalışır
        egitim = "https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPalk2SW1WbmFYUnBiU0k3Y3pvNU9pSndiM04wWDNSNWNHVWlPM002TkRvaWNHOXpkQ0k3ZlE9PQ==/"  # 295
        teknoloji = "https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPams2SW5SbGEyNXZiRzlxYVNJN2N6bzVPaUp3YjNOMFgzUjVjR1VpTzNNNk5Eb2ljRzl6ZENJN2ZRPT0=/"  # 321
        if self.categ=="gundem":
            for i in range(1, 8000, 1):
                # gundem_links.append("{}{}".format(gundem, i))
                self.dizi.append("{}{}".format(gundem, i))
        elif self.categ=="dunya":
            for i in range(1, 2000, 1):
                # dunya_links.append("{}{}".format(dunya, i))
                self.dizi.append("{}{}".format(dunya, i))
        elif self.categ == "ekonomi":
            for i in range(1, 200, 1):
                self.dizi.append("{}{}".format(ekonomi, i))
        elif self.categ == "otomotiv":
            for i in range(1, 200, 1):
                self.dizi.append("{}{}".format(otomotiv, i))
        elif self.categ == "saglik":
            for i in range(1, 175, 1):
                self.dizi.append("{}{}".format(saglik, i))
        elif self.categ == "egitim":
            for i in range(1, 295, 1):
                self.dizi.append("{}{}".format(egitim, i))
        else:
            for i in range(1, 321, 1):
                print(i)
                self.dizi.append("{}{}".format(teknoloji, i))


        return self.dizi#gundem_links, dunya_links, ekonomi_links, otomotiv_links, saglik_links, egitim_links, teknoloji_links

    def get_link(self,i):
        count = 1
        count2 = 0
        r = requests.get(i)
        soup = BeautifulSoup(r.content, 'html5lib')
        # dizi = []
        for a in soup.find_all('a', href=True):
            link = a['href']
            # print(link)
            if count % 2 == 1:
                # print(link)
                # print(self.link_filname)
                # with open(self.link_filname, 'a') as file:
                with open(self.link_filname, "a", encoding="utf-8") as file:
                    file.write(link + "\n")
                    # dizi.append(link)
            count += 1

    def creator(self,url):
        # r = requests.get(url)
        # soup = BeautifulSoup(r.content, 'html5lib')
        # title = soup.find("h1").getText()
        # content_array = soup.find("div", attrs={"class": "content"}).getText()
        # category_array = soup.find("a", attrs={"class": "text-muted small"}).getText()
        # category_array = category_array.split()
        # date = soup.find("time").getText()
        # date = date.split()
        # date = date[2] + date[3] + date[4]
        # content_array = content_array.split()
        # content_string = ""
        # stop = "aip2('pageStructure',"
        # for w in content_array:
        #     if stop == w:
        #         break
        #     else:
        #         content_string = content_string + " " + w
        #         # w_data = url+";"+date+";"+title+";"+content_string
        # w_data = "{};{};{};{};{}".format(url, category_array[0], date, title, content_string)
        # write_to_txt(w_data)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        try:
            title = soup.find("h1").getText()
        except:
            title = "None"
        try:
            content_array = soup.find("div", attrs={"class": "content"}).getText()
            content_array = content_array.split()
            content_string = ""
            stop = "aip2('pageStructure',"
            for w in content_array:
                if stop == w:
                    break
                else:
                    content_string = content_string + " " + w
        except:
            content_string = "None"
        try:
            category_array = soup.find("a", attrs={"class": "text-muted small"}).getText()
            category_array = category_array.split()
        except:
            category_array = "None"
        try:
            date = soup.find("time").getText()
            date = date.split()
            date = date[2] + date[3] + date[4]
        except:
            date = "None"

            # w_data = url+";"+date+";"+title+";"+content_string
        w_data = "{} ; {} ; {} ; {}".format(url, date, title, content_string)  # çıkarıldı category_array[0],
        print(w_data)
        with open(self.content_filname, 'a') as file:
            file.write(w_data + '\n')


    def main(self):
        print("************ started to collect page links")

        self.page_links=self.dateCreator(self.date1,self.date2)
        print("-------- all links---")


        for i in self.page_links:
            print(i.strip())
            print("lşkjşlk")
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
# url="https://www.sozcu.com.tr/ajax/list-load/bGVDNFhmdTJXNEc2S1E2MzFJZDh5NDlFNkgzMzI3VzdZVG95T250ek9qRXpPaUpqWVhSbFoyOXllVjl1WVcxbElqdHpPams2SW5SbGEyNXZiRzlxYVNJN2N6bzVPaUp3YjNOMFgzUjVjR1VpTzNNNk5Eb2ljRzl6ZENJN2ZRPT0=/1"
# link_filname='/home/bilgi/Desktop/DDD/a2.txt'
# count = 1
# count2 = 0
# r = requests.get(url.strip())
# soup = BeautifulSoup(r.content, 'html5lib')
# dizi = []
# for a in soup.find_all('a', href=True):
#     link = a['href']
#     # print(link)
#     # if count % 2 == 1:
#     #     print(link)
#     print(link_filname)
#     # with open(self.link_filname, 'a') as file:
#     with open(link_filname, "a", encoding="utf-8") as file:
#         print(link)
#         file.write(link + '\n')
# ==================   creator  ==========================
# url="https://www.sozcu.com.tr/2022/teknoloji/marstaki-34-milyar-yillik-mega-tsunami-icin-asteroit-iddiasi-7515630/"
# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html5lib')
# try:
#     title = soup.find("h1").getText()
# except:
#     title="None"
# try:
#     content_array = soup.find("div", attrs={"class": "content"}).getText()
#     content_array = content_array.split()
#     content_string = ""
#     stop = "aip2('pageStructure',"
#     for w in content_array:
#         if stop == w:
#             break
#         else:
#             content_string = content_string + " " + w
# except:
#     content_string="None"
# try:
#     category_array = soup.find("a", attrs={"class": "text-muted small"}).getText()
#     category_array = category_array.split()
# except:
#     category_array="None"
# try:
#     date = soup.find("time").getText()
#     date = date.split()
#     date = date[2] + date[3] + date[4]
# except:
#     date="None"
#
#         # w_data = url+";"+date+";"+title+";"+content_string
# w_data = "{} ; {} ; {} ; {}".format(url,  date, title, content_string) # çıkarıldı category_array[0],
# print(w_data)