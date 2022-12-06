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
from datetime import datetime, timedelta,date

class milli:
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



# https://www.milligazete.com.tr/arsiv/2019-10-21/
    def dateCreator(self,d1,d2):
        dizi=[]
        tamam_link = "https://www.milligazete.com.tr/arsiv/"
        t1 = datetime.strptime(d1, '%Y-%m-%d').date()
        t2 = datetime.strptime(d2, '%Y-%m-%d').date()
        # t1 = datetime.strptime(d1, '%m/%d/%Y').date()
        # t2 = datetime.strptime(d2, '%m/%d/%Y').date()
        t = timedelta(days=1)
        dates = np.arange(t1, t2, t).astype(datetime)

        for i in dates:
            newdate = i.strftime('%Y-%m-%d')
            dizi.append("{}{}".format(tamam_link, newdate))
            print(newdate)

        return dizi #kanser_links, memekanseri_links, prostat_links, tamamı_links


    def get_link(self,url):
        html = requests.get(url).content
        date = url[37:]
        soup = BeautifulSoup(html, "html.parser")
        for a in soup.find_all('a', href=True):
            link = a['href']
            sp = str(link).split('/')
            new_link=""
            if len(sp) == 3 and str(link).startswith('/') and not str(link).startswith('/sayfa'):
                new_link=link
                cat=str(new_link).split('/')
                if cat[1].startswith("maka"):
                    pass
                else:
                    cat=cat[1]
                    wdata = "{}{} ;{} ;{}".format("https://www.milligazete.com.tr", new_link, date, cat)
                    # print(wdata)
                    with open(self.link_filname, "a", encoding="utf-8") as file:
                        file.write(wdata + "\n")
            else:
                pass

        # list = soup.find_all("div", {"class": "category-news"})
        # try:
        # list = soup.find_all("div", {"class": "f-cat f-item"})
        # for i in list:
        # for j in list:
        #     print("---------------------------")
        #     cat = j.find('h3', {"class": "f-brandon-black"}).text
        #     print(j.find('h3', {"class": "f-brandon-black"}).text)
        #     print("---------------------------")
        #     z = j.find_all('a', {"class": "lb"})
        #     print(z)
        #     for i in z:
        #         wdata = "{}{} ;{} ;{}".format("https://www.milligazete.com.tr", i.get("href"), date, cat)
        #         print(wdata)
        #         print(self.link_filname)
        #         print("88888888888888888888888888888888888888")
        #         with open(self.link_filname, "a", encoding="utf-8") as file:
        #             file.write(wdata + "\n")
        # except:
        #     pass


#https://www.milligazete.com.tr/haber/1708597/abdden-arabistana-teklif-fbi-ekibi-yollayabiliriz
    def creator(self,i):
        j = i.split(';')
        if i.startswith("https://www.milligazete.com.tr/foto"):
            pass
        else:
            date = j[1].strip()
            url = j[0].strip()
            cat = j[2].strip()
            if str(cat) != str(self.categ):
                print("False")
                r = requests.get(url)
                soup = BeautifulSoup(r.content, 'lxml')
                # try:
                try:
                    title = soup.find('h1').getText()
                except:
                    title = "None"
                # print(title)
                # print("------------------")

                txt = ""
                try:
                    art = soup.find("div", {"class": "news-container-text"})
                    z = art.find_all('p')
                    print(z)

                    for i in z:
                        print("******************")
                        print(i.text)
                        txt += i.text
                except:
                    txt = "None"

                cdata = '{} ; {} ; {} ; {}'.format(url, date, title, txt)
                print(cdata)
                with open(self.content_filname, "a", encoding="utf-8") as file:
                    file.write(cdata + "\n")
            else:
                print("True")
                if str(j[2]) == str(cat):
                    print("True2")
                    date = j[1].strip()
                    url = j[0].strip()
                    cat = j[2].strip()

                    r = requests.get(url)
                    soup = BeautifulSoup(r.content, 'lxml')
                    # try:
                    try:
                        title = soup.find('h1').getText()
                        print("ttittl")
                        print(title)
                    except:
                        title = "None"
                    # print(title)
                    # print("------------------")
                    txt = ""
                    try:
                        art = soup.find("div", {"class": "news-container-text"})
                        z = art.find_all('p')
                        print(z)
                        print("zzzz")
                        # txt = ""
                        for i in z:
                            print("===================")
                            print(i.text)
                            txt += i.text
                    except:
                        txt = "None"

                    cdata = '{} ; {} ; {} ; {}'.format(url, date, title, txt)  #cat cıkarıldı
                    print(cdata)
                    with open(self.content_filname, "a", encoding="utf-8") as file:
                        file.write(cdata + "\n")
                else:
                    pass

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

        # print("-----------------------")
        # print(self.content_filname)
        # print(self.link_filname)
        # print("-------------------------")

        for i in self.newsLinks[:]:
            self.creator(i.strip())

        print("Successfully!")






#
# import os
# import bs4
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import numpy as np
# import os
# import time
# import urllib.request
# import re
# import urllib3
# from pandas import DataFrame
# import csv
# import datetime
# from datetime import datetime, timedelta,date
# url="https://www.milligazete.com.tr/arsiv/2020-10-10"
# html = requests.get(url).content
# date = url[37:]
# print(date)
# soup = BeautifulSoup(html, "html.parser")
#
# list = soup.find_all("div", {"class": "col-md-8"})
# # list = soup.find_all("div", {"class": "category-news"})
# # try:
# # list = soup.find_all("div", {"class": "f-cat f-item"})
# # for i in list:
#
# for a in soup.find_all('a', href=True):
#     link = a['href']
#     sp=str(link).split('/')
#     if len(sp)==3 and str(link).startswith('/') and not str(link).startswith('/sayfa'):
#         print(link)
#
#     else:
#         pass
#     print(link)
#
# for j in list:
#     h=j.find_all("a href")
#     print(type(h))
#     print(h)
#
#     print("---------------------------")
#     cat = j.find('h3', {"class": "f-brandon-black"}).text
#     print(j.find('h3', {"class": "f-brandon-black"}).text)
#     print("---------------------------")
#     z = j.find_all('a', {"class": "lb"})
#     print(z)
#     for i in z:
#         wdata = "{}{} ;{} ;{}".format("https://www.milligazete.com.tr", i.get("href"), date, cat)
#         print(wdata)
#         # print(self.link_filname)
#         print("88888888888888888888888888888888888888")









#
# i="https://www.milligazete.com.tr/ekonomi/25-kurusa-satilan-posete-zam-geldi-mi-kurul-kararini-acikladi-690210 ;2020-12-19 ;ekonomi"
# categ="all"
# j =i.split(';')
# if i.startswith("https://www.milligazete.com.tr/foto"):
#     pass
# else:
#     date = j[1].strip()
#     url = j[0].strip()
#     cat = j[2].strip()
#     if str(cat)!=str(categ):
#         print("False")
#         r = requests.get(url)
#         soup = BeautifulSoup(r.content, 'lxml')
#         # try:
#         try:
#             title = soup.find('h1').getText()
#         except:
#             title="None"
#         # print(title)
#         # print("------------------")
#
#         txt=""
#         try:
#             art = soup.find("div", {"class": "news-container-text"})
#             z = art.find_all('p')
#             print(z)
#
#             for i in z:
#                 print("******************")
#                 print(i.text)
#                 txt += i.text
#         except:
#             txt="None"
#
#         cdata = '{} ;{} ;{} ;{} ;{}'.format(url, date,cat,title,txt)
#         print(cdata)
#         # with open(self.content_filname, "a", encoding="utf-8") as file:
#         #     file.write(cdata + "\n")
#     else:
#         print("True")
#         if str(j[2])==str(cat):
#             print("True2")
#             date = j[1].strip()
#             url = j[0].strip()
#             cat = j[2].strip()
#
#
#             r = requests.get(url)
#             soup = BeautifulSoup(r.content, 'lxml')
#             # try:
#             try:
#                 title = soup.find('h1').getText()
#                 print("ttittl")
#                 print(title)
#             except:
#                 title = "None"
#             # print(title)
#             # print("------------------")
#             txt=""
#             try:
#                 art = soup.find("div", {"class": "news-container-text"})
#                 z = art.find_all('p')
#                 print(z)
#                 print("zzzz")
#                 # txt = ""
#                 for i in z:
#                     print("===================")
#                     print(i.text)
#                     txt += i.text
#             except:
#                 txt = "None"
#
#             cdata = '{} ;{} ;{} ;{} ;{}'.format(url, date, cat, title, txt)
#             print(cdata)
#                 # with open(self.content_filname, "a", encoding="utf-8") as file:
#                 #     file.write(cdata + "\n")
#         else:
#             pass