# # from __future__ import absolute_import, unicode_literals
# # from celery import shared_task
# # import time
# # import requests
# # import bs4
# # from bs4 import BeautifulSoup
# # from newsplease import *
# # import cloudscraper
#
#
#
# from datetime import datetime
# from datetime import timedelta
# from datetime import date
# from datetime import time
# import numpy as np
# date_list=[] #with open .txt file
# with open('/home/bilgi/Desktop/tarih.txt', 'r', newline="", encoding="utf-8") as f: # input file path
#     for i in f.readlines():
#        date_list.append(i.strip())
#
# def date_arrange_creator(date,coday,arange):
#     created_date_list = []
#     for i in date:
#         tmp_date_list=[]
#         t1=datetime.strptime(i,'%Y-%m-%d').date()
#         print(t1)
#         t = timedelta(days =int(coday))
#         print(t1+t)
#         t2=t1+t
#         print("-----------------------------------------")
#         dates = np.arange(t1, t2, arange).astype(datetime)
#         for datem in dates:
#             newdate=datem.strftime('%d/%m/%Y')
#             # tmp_date_list.append(newdate)
#             print(newdate)
#             # newdate2=datetime.strftime(datem,'%d/%m/%Y').date()
#             # t2 = timedelta(days =int(coday))
#             tt = datetime.strptime(newdate, '%d/%m/%Y').date()
#             t2 = timedelta(days=1)
#             ndate2=tt+t2
#             newdate2=ndate2.strftime('%d/%m/%Y')
#             # print(ndate2)
#             print(newdate2)
#             last="{}:{}".format(newdate,newdate2)
#             tmp_date_list.append(last)
#             print("=======")
#         created_date_list.append(tmp_date_list)
#     return created_date_list
#
# # for i in date_list:
# newdates=date_arrange_creator(date_list,5,3)
#
#
#
#
#
# newspaper_list=[]#with open .txt file
# with open('/home/bilgi/Desktop/news_list.txt', 'r', newline="", encoding="utf-8") as f: # input file path
#     for i in f.readlines():
#         print(len(i))
#         if len(i)<3:
#             pass
#         else:
#             newspaper_list.append(i.strip())
#
# for t in newdates:
#     for ii in t:
#         i=ii.split(':')
#         for j in newspaper_list:
#             h='{} , {} , {}'.format(i[0],i[1],j)
#             print(h)
#
