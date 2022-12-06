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

dizi=[]
for i in range(23):
    url='{}{}/'.format("https://english.elpais.com/science-tech/",i)
    dizi.append(url)
links=[]
for url in dizi:
    # print(url)


# def get_link(url):

    # scraper = cloudscraper.create_scraper(delay=10, browser='firefox')
    req = requests.get(url).content
    soup = BeautifulSoup(req, "html.parser")
    content_str = soup.find_all("a", {"class": "c_m_c _pr _db"})
    for i in content_str:
        h=i.get("href")
        new_url='{}{}'.format("https://english.elpais.com",h)
        print(new_url)
        links.append(new_url)
content_filname="/home/bilgi/PycharmProjects/elastic/webapp/g_upload/aaa_elpais_science_tech_content.txt"
for url in links:
    print(url)

    # url="https://english.elpais.com/science_tech/2020-06-16/spanish-covid-19-expert-there-is-more-virus-circulating-now-than-before-the-state-of-alarm.html"
    req = requests.get(url).content
    soup = BeautifulSoup(req, "html.parser")
    try:
        titl=soup.find("h1")
        title=titl.getText().strip()
    except:
        title="None"
    # print(title.getText())
    try:
        dat=soup.find("time")
        date=dat.getText().strip()
    except:
        date="None"
    # print(dat.getText())
    txt = ""
    try:
        content_str=soup.find_all("p")

        for i in content_str:
            h=i.getText().strip()
            txt +=h.strip()
    except:
        txt="None"

    print(url, date.strip(), title.strip(), txt.strip())
    w_data = "{} ; {} ; {} ; {}".format(url, date.strip(), title.strip(), txt.strip())
    with open(content_filname, 'a') as file:
        file.write(w_data + '\n')

counter=0
with open("/home/bilgi/websites/rubic2/webapp/g_upload/all_france24_2/all_france24_2_france24_content.txt", 'r', newline='', encoding="utf-8") as file:
    for i in file.readlines():
        i = i.strip("\n")
        counter +=1
        if counter>66995:
            print(i)
print(counter)