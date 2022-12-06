#haberturk gazetesi

# tarihe ve kategoriye göre arama yapılabilecek  selenium kullanılması ihtimali var
# https://www.haberturk.com/haber-tuneli/2-haziran-2010-haberleri?kategori=teknoloji
#url="https://www.haberturk.com/haber-tuneli/2-haziran-2010-haberleri?kategori=teknoloji"
#url="https://www.haberturk.com/ekonomi/teknoloji/haber/1059025-google-insanlik-icin-onemli-bir-adim-atti"


#istiklal gazetesi
#208 sayfalık link barındırıyor son tarih =aralık-2015
#url="https://www.istiklal.com.tr/teknoloji?sayfa=208"
#url="https://www.istiklal.com.tr/haber/oukitel-marka-cep-telefonunun-15-gun-sarji-bitmiyor/3533"

import os
import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import urllib.request
import re
import urllib3
from pandas import DataFrame
import csv
import datetime
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class haberturk:
    def __init__(self, date1, date2, categ, filname, dirname,count, **kwargs):
        self.date1 = date1
        self.date2 = date2
        if categ!="":
            self.categ = categ
        elif categ=="all" or categ=="All" or categ=="ALL":
            self.categ="teknoloji"
        else:
            self.categ="teknoloji"

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
        dizi=[]
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)
        dat = ""
        for i in dates:
            datem = i.strftime('%d/%m/%Y')
            date=str(datem).split('/')
            if date[1]=="01":
                dat="{}-{}-{}".format(date[0],'ocak',date[2])
            elif date[1]=="02":
                dat="{}-{}-{}".format(date[0],'subat',date[2])
            elif date[1]=="03":
                dat="{}-{}-{}".format(date[0],'mart',date[2])
            elif date[1]=="04":
                dat="{}-{}-{}".format(date[0],'nisan',date[2])
            elif date[1]=="05":
                dat="{}-{}-{}".format(date[0],'mayis',date[2])
            elif date[1]=="06":
                dat="{}-{}-{}".format(date[0],'haziran',date[2])
            elif date[1]=="07":
                dat="{}-{}-{}".format(date[0],'temmuz',date[2])
            elif date[1]=="08":
                dat="{}-{}-{}".format(date[0],'agustos',date[2])
            elif date[1]=="09":
                dat="{}-{}-{}".format(date[0],'eylul',date[2])
            elif date[1]=="10":
                dat="{}-{}-{}".format(date[0],'ekim',date[2])
            elif date[1]=="11":
                dat="{}-{}-{}".format(date[0],'kasim',date[2])
            else:
                dat="{}-{}-{}".format(date[0],'aralik',date[2])

            print(dat)
            # https: // www.haberturk.com / haber - tuneli / 2 - haziran - 2010 - haberleri?kategori = teknoloji
            url="https://www.haberturk.com/haber-tuneli/{}-haberleri?kategori={}".format(dat,self.categ)
            dizi.append(url)
        return dizi

    def get_link(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        links2 = soup.find_all("div", {"class": "widget-box"})
        lnk2 = ""
        dat = url.split('/')
        date = dat[4].split('?')
        date = date[0]
        date = date[:-10]
        for lnk in links2:
            lnk2 = lnk.find('a')
            data = '{}{} ; {}'.format("https://www.haberturk.com", lnk2.get("href"), date)
            with open(self.link_filname, 'a') as file:
                file.write(data + '\n')

    def creator(self, url):
        urlim = url.split(';')
        url = urlim[0].strip()
        print(url)
        if str(url).startswith("https://www.haberturk.com/video"):
            pass
        else:
            date = urlim[1].strip()
            print(date)
            html = requests.get(url).content
            soup = BeautifulSoup(html, "html.parser")
            try:
                title = soup.find("h1", {"class": "title"}).text.strip()
            except:
                title = "None"
            print(title)

            try:
                txt = ""
                cont = soup.find("article", {"class": "content type1"})
                content = cont.find_all('p')
                for i in content:
                    txt += i.text.strip()
            except:
                txt = "None"
            print(txt)
            cdata = '{} ; {} ; {} ; {}'.format(url, date, title, txt)
            with open(self.content_filname, "a", encoding="utf-8") as file:
                file.write(cdata + "\n")

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

# get_link
# url="https://www.haberturk.com/haber-tuneli/03-subat-2010-haberleri?kategori=teknoloji"
#
# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'lxml')
# links2=soup.find_all("div",{"class": "widget-box"})
# lnk2=""
# dat=url.split('/')
# date=dat[4].split('?')
# date=date[0]
# date=date[:-10]
# for lnk in links2:
#     lnk2=lnk.find('a')
#     link='{}{} ; {}'.format("https://www.haberturk.com",lnk2.get("href"),date)
#     print(link)
#
# # dizi = []
# for a in soup.find_all('widget-box'):
#     link = a['href']
#     print(link)




# creator
# url="https://www.haberturk.com/ekonomi/makro-ekonomi/haber/204632-yeni-dijital-muzik-formati-yolda ; 03-subat-2010"
# urlim=url.split(';')
# url=urlim[0].strip()
# print(url)
# date=urlim[1].strip()
# print(date)
# html = requests.get(url).content
# soup = BeautifulSoup(html, "html.parser")
# try:
#     title = soup.find("h1", {"class": "title"}).text.strip()
# except:
#     title="None"
# print(title)
#
# try:
#     txt = ""
#     cont=soup.find("article",{"class":"content type1"})
#     content=cont.find_all('p')
#     for i in content:
#         txt+=i.text.strip()
# except:
#     txt="None"
# print(txt)
# cdata = '{} ; {} ; {} ; {}'.format(url, date, title, txt)
# with open(self.content_filname, "a", encoding="utf-8") as file:
#     file.write(cdata + "\n")