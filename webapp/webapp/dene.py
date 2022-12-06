# import requests
# import os
# import sys
# import elasticsearch.exceptions
# import csv
# import json_normalize
# import pandas as pd
# import time
# from datetime import datetime
# from datetime import timedelta
# from datetime import date
# from datetime import time
# import numpy as np
# import shutil
# import requests
# import logging
# import wget
# import bs4
# from bs4 import BeautifulSoup
# from newsplease import NewsPlease
# # url="http://www.ensonhaber.com/rss/ensonhaber.xml"
# # url="http://www.trthaber.com/sondakika.rss"
# # url="https://www.sabah.com.tr/rss/teknoloji.xml"
# # url="http://www.milliyet.com.tr/rss/rssNew/teknolojiRss.xml"
# # url="http://www.hurriyet.com.tr/rss/teknoloji"
# # url="http://www.internethaber.com/rss"
# url="https://www.takvim.com.tr/rss/anasayfa.xml"
#
#
# resp = requests.get(url)
# soup = BeautifulSoup(resp.text, 'xml')
#
# for entry in soup.find_all('item'):
#     surl2 = entry.find('link').text
#     # print(surl2)
#     article = NewsPlease.from_url(surl2.strip())
#
#     # print("===================================")
#     try:
#         a = entry.find('link').text
#     except:
#         a="None"
#     try:
#         b = e.text if (e := entry.find('pubDate')) else None
#     except:
#         b="None"
#     try:
#         c = entry.find('title').text
#     except:
#         c="None"
#     # try:
#     #     e = entry.find('description').text.strip()
#
#     e = entry.find('description').text.strip()
#     # print("--------------------------------------")
#     # print(e)
#     # print("--------------------------------------")
#
#     d = article.maintext
#     try:
#         d = " ".join(d.split())
#     except:
#         pass
#     if type(d)=="str":
#         pass
#     else:
#         d = e
#         # print("++++++++++++++++++++++++++++++++++++++++++++++++++4")
#         # print(d)
#         # print("++++++++++++++++++++++++++++++++++++++++++++++++++4")
#         if d.startswith("<a"):
#             d=d.split("/a>")
#             d=d[1]
#         elif d.endswith("a>"):
#             d=d.split("<a")
#             d=d[0]
#         else:
#             d=e
#     w_data = "{} ; {} ; {} ; {}".format(a.strip(),b.strip(), c.strip(), d.strip())
#     print(w_data)







#########========================== start of wikidata.org sparql ==========######################
#                               yapısı
#    {'head': {'vars': ['item', 'itemLabel', 'itemDescription', 'num']}, 'results': {'bindings': []}}


#
# namelist=['Muhammet Ozhan', 'Serkan Unsal', 'Aziz Sancar', 'Mustafa Kopuk']
# import pandas as pd
# import requests
# url = 'https://query.wikidata.org/sparql'
# liste=[]
# for name in namelist:
#     query = """
#     SELECT ?item ?itemLabel ?itemDescription ?num WHERE {
#       SERVICE wikibase:mwapi {
#         bd:serviceParam wikibase:endpoint "www.wikidata.org";
#                         wikibase:api "EntitySearch";
#                         mwapi:search """+'"'+name+'"'+""";
#                         mwapi:language "en".
#         ?item wikibase:apiOutputItem mwapi:item.
#         ?num wikibase:apiOrdinal true.
#       }
#       SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
#     }
#     ORDER BY ASC(?num) LIMIT 10
#     """
#     r = requests.get(url, params = {'format': 'json', 'query': query})
#     data = r.json()
#     for i in data['results']['bindings']:
#         tmp = []
#         qcode=i['item']['value']
#         z=qcode.split('/')
#         qcode=z[4]
#         tmp.append(qcode)
#
#         item_lab=i['itemLabel']['value']
#         tmp.append(item_lab)
#
#         item_desc=i['itemDescription']['value']
#         tmp.append(item_desc)
#
#         liste.append(tmp)
#
# df=pd.DataFrame(liste)
# df.head()

#########------------------ end of wikidata.org sparql --------------######################


#
#
# from celery import shared_task
# import time
# import requests
# import bs4
# from bs4 import BeautifulSoup
# from newsplease import *
# import cloudscraper
# scraper = cloudscraper.create_scraper(delay=10, browser='firefox')
# f_links_tekno = []
# chk_links = []
# counter_tekno = 0
# my_rss_links_tekno2 = 'https://www.ntv.com.tr/teknoloji.rss','https://www.yenisafak.com/teknoloji/rss'
# # my_rss_links_tekno = ['https://www.cumhuriyet.com.tr/rss/10.xml','http://www.hurriyet.com.tr/rss/teknoloji','https://www.star.com.tr/rss/rss.asp?cid=124','https://www.takvim.com.tr/rss/teknoloji.xml','https://www.mansetturkiye.com/rss_teknoloji_15.xml','https://www.yeniakit.com.tr/rss/haber/teknoloji','https://www.ahaber.com.tr/rss/teknoloji.xml','https://www.cnnturk.com/feed/rss/teknoloji','http://www.ensonhaber.com/rss/teknoloji.xml','http://www.mynet.com/haber/rss/kategori/teknoloji/']
# # for i in range(65565):
# print("========================================================================")
# print("started to get RSS")
# print("========================================================================")
# time.sleep(2)
# for url in my_rss_links_tekno2:
#     #
#     resp = requests.get(url)
#     soup = BeautifulSoup(resp.text, 'xml')
#     e_name = soup.find_all('item')
#     if len(e_name) == 0:
#         req = scraper.get(url)
#         # soup = BeautifulSoup(req.text, "html.parser")
#         # resp = requests.get(url)
#         soup = BeautifulSoup(req.text, 'xml')
#         e_name = soup.find_all('item')
#     else:
#         continue
#     print(len(e_name))
#     print(url)
#     for entry in soup.find_all('item'):
#         surl2 = entry.find('link').text
#         print(surl2)
# ------------------- Start of Dosya Birleştirme ___________________________
# import pandas as pd
# my_arr=[]
# file_path='/home/bilgi/Downloads/bg_rss_teknoloji.txt'
# with open(file_path, 'r', newline="", encoding="utf-8") as f:
#  for i in f.readlines()[:]:
#      tmp = []
#      cont=i.split(';')
#      if len(cont)==4:
#          for j in cont:
#
#              tmp.append(j)
#
#          my_arr.append(tmp)
#          tmp = []
#      else:
#          counter=0
#          article = ""
#          for j in cont:
#
#              counter += 1
#
#              if(counter>3):
#                  article+=j
#              else:
#                  tmp.append(j)
#          tmp.append(article)
#          my_arr.append(tmp)
#          tmp = []
#
#
# df=pd.DataFrame(my_arr)
# df.head()
#
#
#
#      print(i)

# from webapp.pycode.google import google_search
# name_list=['A. Arif Ergin', 'Abdullah Atalar', 'Abdullah Erin', 'Abdullah Kaya', 'Abdullah Kizilirmak', 'Adem Tekin', 'Adnan Ertem', 'Afsin Emre Kayipmaz', 'Ahmed Yuksel Ozemre', 'Ahmet Acar', 'Ahmet Arif Ergin', 'Ahmet Cakir', 'Ahmet Demircan', 'Ahmet Emre Bilgili', 'Ahmet Ercan', 'Ahmet Hakan Erol', 'Ahmet Hakan Haliloglu', 'Ahmet Hakan Onur', 'Ahmet Hakan Unlu', 'Ahmet Karakasli', 'Ahmet Oral', 'Ahmet S Yavuz', 'Ahmet Sozen', 'Ahmet Uludag', 'Ahmet Yesevi', 'Ahmet Yildiz', 'Ahmet Yildizhan', 'Akin Ozturk', 'Akkan Surver', 'Akkan Suver', 'Alaattin Buyukkaya', 'Ali Abbasov', 'Ali Alpar', 'Ali Cinar', 'Ali D Guler', 'Ali Daskin', 'Ali Hasanov', 'Ali Kocabas', 'Ali Kuscu', 'Ali Nesin', 'Ali Ozhan Aytekin', 'Ali Veysel Ozden', 'Ali Yildirim', 'Alim Yildiz', 'Alpay Azap', 'Ara Keresteci', 'Arif Ozkan', 'Arman Manukyan', 'Artug Cetin', 'Asim Orhan Barut', 'Asli Erdogan', 'Asu Ozdaglar', 'Ayben Karasu Uysal', 'Aydogan Ozcan', 'Ayhan Kaya', 'Aykut Ozdarendeli', 'Aykut Ozkul', 'Aykut Uren', 'Ayper Somer', 'Ayse Akincigil', 'Ayse Erzan', 'Ayse Isil Karakas', 'Aytul Ercil', 'Aziz Sancar', 'Bahar Demirel', 'Bayram Ozturk', 'Behlul Ozkan', 'Belkis Ozdogan', 'Betul Uralcan', 'Birol Akgun', 'Birol Can', 'Bulent Ertugrul', 'Bulent Kilic', 'Burcu Ozsoy', 'Burcu Ozsoy Cicek', 'Burhanettin Duran', 'Cagan Sekercioglu', 'Caghan Kizil', 'Cahit Arf', 'Can Dincer', 'Can Fuat Delale', 'Can Yucel Karabay', 'Canan Dagdeviren', 'Cansu Canca', 'Carl Blegen', 'Cavid Erginsoy', 'Celal Sengor', 'Cemal Saydam', 'Cemil Tascioglu', 'Cengiz Aktar', 'Cengiz Aydin', 'Cigdem Ozkan Aygun', 'Darbaz Adnan', 'Daron Acemoglu', 'Davut Kavranoglu', 'Deger Saygin', 'Demet Yalcin Kehribar', 'Deniz Caliskan', 'Deniz Cavusoglu', 'Derya Cebeci', 'Didem Ozcimen', 'Dogan Erbahar', 'Dogan Kalafat', 'Dursun Ali Sirin', 'Duygu Sag', 'Ebru Emekli Alturfan', 'Ebru Erbay', 'Ebru Oral', 'Ekmeleddin Ihsanoglu', 'Emin Ozsoy', 'Emrah Altindis', 'Emrah Eroglu', 'Emre Arslan', 'Emre Onur Kahya', 'Eray Gucluer', 'Ercan Malkoc', 'Ercan Varlibas', 'Erdal Arikan', 'Erdal Kayacan', 'Erdem Erkul', 'Erdogan Alkin', 'Erdogan Sendemir', 'Erella Hovers', 'Eren Demir', 'Eren Demirhan', 'Erhan Akin', 'Erhan Sarisin', 'Erhan Usta', 'Erkan Yuce', 'Erol Yildirim', 'Ersan Basar', 'Ersin Yurtsever', 'Ertug Duzgunes', 'Ertugrul Bilgili', 'Ertugrul Gazi Saglam', 'Esra Gul Dardagan Kibar', 'Etem Caliskan', 'Eyup Gumus', 'Fahrettin Altun', 'Fahrettin Koca', 'Faruk Ozlu', 'Faruk Sen', 'Fatih Bulut', 'Fatih Kose', 'Fatma Deniz Aygun', 'Fatma Deniz Sayiner', 'Fatma Deniz Yildiz', 'Fatma Senel Boydag', 'Feray Bakan', 'Feride Acar', 'Feriha Oz', 'Feroz Ahmad', 'Feryal Ozel', 'Fethi Acikel', 'Fevzi Altuntas', 'Fevzi Cakmak Cebeci', 'Fuat Oktay', 'Fuat Sezgin', 'Fusun Eyuboglu', 'Gediz Akdeniz', 'Gokhan Budak', 'Gokhan Hotamisligil', 'Gokhan Onem', 'Gulay Barbarosoglu', 'Gulnur Gollu Bahadir', 'Gulsen Altug', 'Gulsum Basak Saygan', 'Gulustu Salur', 'Gun Kut', 'Guray Yildiz', 'Gurkan Yesiloz', 'Guven Kasikci', 'Hakan Buyukhatipoglu', 'Hakan Celikhisar', 'Hakan Dursun', 'Hakan Uney', 'Hakan Yilmaz', 'Halil Can Gemalmaz', 'Halil Eldemir', 'Halil Ibrahim Zeybek', 'Halil Yildirim', 'Haluk Ozenc', 'Haluk Ozener', 'Hamit Nafiz Pamir', 'Hasan Birol Cotuk', 'Hasan Demirci', 'Hasan Gunduz', 'Hasan Havitcioglu', 'Hasan Tezer', 'Hatice Altug', 'Hatice Atas', 'Hatice Yalcin', 'Hayat Erkanal', 'Hilal Elver', 'Hilmi Ziya Ulken', 'Hulya Guler', 'Hurrem Bodur', 'Huseyin Avni Oktem', 'Huseyin Aydin', 'Huseyin Mutlu', 'Huseyin Onay', 'Huseyin Toprak', 'Huseyin Yildiz', 'Hussein M Ismail', 'Ibrahim Adnan Saracoglu', 'Ibrahim Gokce Yayla', 'Ibrahim Kucuk', 'Ibrahim Muteferrika', 'Iftahar Koksal', 'Igor Ashurbeyli', 'Ihsan Ates', 'Ihsan Gursel', 'Ihsan Yilmaz', 'Ihsaniye Coskun', 'Ilber Ortayli', 'Ilhami Celik', 'Ilhami Kiziroglu', 'Ilke Anac', 'Ilker Tahiroglu', 'Irmak Zileli', 'Ismail Akbay', 'Ismail Besikci', 'Ismail Cinel', 'Ismail Demir', 'Ismail Demircioglu', 'Ismail Demirel', 'Ismail Demirkan', 'Ismail Fidan', 'Ismail Gezgin', 'Ismail Gokhan Deniz', 'Ismail Hakki Bursevi', 'Ismail Hakki Ekin', 'Ismail Hakki Uzuncarsili', 'Ismail Lazoglu', 'Ismail Tufan', 'Ivet Bahar', 'Jale Inan', 'Janet Akyuz Mattei', 'K. Sivan', 'Kadir Cangizbay', 'Kadizade i Rumi', 'Kamil Ugurbil', 'Kamran Turkoglu', 'Karekin Deveciyan', 'Kayihan Pala', 'Kazim Ergin', 'Kemal Erol', 'Kemal Karpat', 'Kemal Kazan', 'Kemal Kirisci', 'Kemal Kurt', 'Kemal Ozdogan', 'Kemal Ozgoren', 'Kemal Oztabak', 'Kemal Ozulken', 'Kerem Kinik', 'Kivanc Birsoy', 'Kivanc Ersoy', 'Koksal Bayraktar', 'Koray Balcioglu', 'Kuddisi Ertugrul', 'Kutlu Merih', 'Levent Akin', 'Levent Trabzonlu', 'Levent Yamanel', 'Leyla Turker Sener', 'Macit Koc', 'Mahmut Aksit', 'Mahmut Sahin', 'Mehmet Akif Somdas', 'Mehmet Ali Alpar', 'Mehmet Ali Kagitci', 'Mehmet Altay Koymen', 'Mehmet Altay Unal', 'Mehmet Bulut', 'Mehmet Cavit Bey', 'Mehmet Celik', 'Mehmet Celikbilek', 'Mehmet Ceyhan', 'Mehmet E. Aydin', 'Mehmet Emin Birpinar', 'Mehmet Eryilmaz', 'Mehmet Gormez', 'Mehmet Gulluoglu', 'Mehmet Gunata', 'Mehmet Gundogdu', 'Mehmet Gunes', 'Mehmet Guney', 'Mehmet Gurbilek', 'Mehmet Karaca', 'Mehmet Keskin', 'Mehmet Musa Aslan', 'Mehmet Mustafa Can', 'Mehmet Mustafa Goksu', 'Mehmet Mustafa Hamidi', 'Mehmet Mustafa Kilickaya', 'Mehmet Mustafa Ozarslan', 'Mehmet Oz', 'Mehmet Ozgur Oktel', 'Mehmet Somel', 'Mehmet Sutyemez', 'Mehmet Tomak', 'Mehmet Unal', 'Mehmet Uyar', 'Mehmet Y Aydin', 'Mehmet Yesiltas', 'Meredith Whittaker', 'Mert Savrun', 'Merthan Dundar', 'Mesut Guner', 'Metin Gurses', 'Metin Heper', 'Metin Ozgen', 'Metin Sitti', 'Metin Tolan', 'Mikdat Kadioglu', 'Miktat Doganlar', 'Mirim Celebi', 'Muazzez Ilmiye Cig', 'Muharrem Bayraktar', 'Mumtaz Soysal', 'Mumtaz Turhan', 'Murat Akova', 'Murat Bas', 'Murat Belge', 'Murat Erdogan', 'Murat S Durakoglugil', 'Murat Yildirim', 'Mustafa Akkus', 'Mustafa Aydin', 'Mustafa Aydinol', 'Mustafa Aysan', 'Mustafa Balci', 'Mustafa Caliskan', 'Mustafa Ciftci', 'Mustafa Erdik', 'Mustafa Gokceoglu', 'Mustafa Hilmi Colakoglu', 'Mustafa Ilicali', 'Mustafa Kaya', 'Mustafa Kibaroglu', 'Mustafa Kocaer', 'Mustafa Kocak', 'Mustafa Safran', 'Mustafa Sahin', 'Mustafa Sait Gonen', 'Mustafa Sancar', 'Mustafa Sen', 'Mustafa Senay', 'Mustafa Sencer Segmen', 'Mustafa Sener', 'Mustafa Sentop', 'Mustafa Senturk', 'Mustafa Sevinc', 'Mustafa Talha Gonullu', 'Mustafa Versan Kok', 'Mustafa Yucel', 'Mustafa Yucel Boz', 'Muzafer Sherif', 'Naci Gorur', 'Nafiz Kocak', 'Nazan Olcer', 'Necati Polat', 'Necmi Karul', 'Necmi Sonmez', 'Nejla Ozer', 'Nesrin Ozoren', 'Nevzat Cevik', 'Nevzat Sahin', 'Nevzat Tarhan', 'Nihat Ali Ozcan', 'Nihat Hatipoglu', 'Nimet Ozguc', 'Niranjan Saggurti', 'Nora Fisher Onar', 'Numan Kurtulmus', 'Nurcan Meral Ozel', 'Nurdan Tozun', 'Nurullah Okumus', 'Oguz Gulseren', 'Okan Ersoy', 'Oktay Uysal', 'Omer Kocak', 'Omer Kucuk', 'Onder Bilg', 'Onur Baser', 'Onur Sen', 'Onur Sener', 'Onur Senol', 'Orhan Ince', 'Orhan Kemal Kahveci', 'Orhan Kemal Yucel', 'Orhan Sencan', 'Orhan Uludag', 'Osman Abali', 'Osman Bilgin Gulcicek', 'Osman Erk', 'Osman Ozdemir', 'Osman Yilmaz', 'Ovgun Ahmet Ercan', 'Oya Baydar', 'Ozer Sencar', 'Ozge Akbulut', 'Ozgur Kasapcopur', 'Ozgur Korkmaz', 'Ozgur Korkmazgil', 'Ozkar Ongen Izver ', 'Ozlem Tureci', 'Pinar Saip', 'R. Erdem Erkul', 'Rahmi Atay', 'Rahmi Oklu', 'Ramazan Yildiz', 'Rasit Tukel', 'Recep Tekin', 'Resat Baris Unlu', 'Rustem Aslan', 'Saadet Arsan', 'Sabahattin Zaim', 'Sadik Esener', 'Sadri Sensoy', 'Sahin Yildirim', 'Sait Akpinar', 'Sait Kapicioglu', 'Saniye Soylemez', 'Sebnem Korur Fincanci', 'Secil Ozkan', 'Sedat Laciner', 'Seddar Yavuz', 'Sehmus Ozden', 'Selami Kuran', 'Selcuk Iz', 'Selim Sami', 'Sema Dogan', 'Sema Kultufan Turan', 'Semra Aydin', 'Semra Cerit Mazlum', 'Semra Kayatas Eser', 'Seniz Cikis', 'Serafeddin Kadir', 'Serap Simsek Yavuz', 'Serap Yazici', 'Serdar Durdagi', 'Serdar Ozcelik', 'Serhat Guvenc', 'Serhat Unal', 'Serif Baris', 'Serkan Yuksel', 'Serkant Ali Cetin', 'Serpil Demirci', 'Seval Izdes', 'Sevil Atasoy', 'Sezer Okay', 'Sibel Ozilgen', 'Sinan Ongen', 'Sinasi Can', 'Soli Ozel', 'Soner Atesogullari', 'Suha Gursey', 'Suha Kucukaksu', 'Sukru Ersoy', 'Sule Toktas', 'Suleyman Allakhverdiev', 'Suleyman ibn Orkhan', 'Suleyman Imanbayevich Imanbayev', 'Suleyman Irvan', 'Suleyman Ismayilov', 'Suleyman Izzat bey', 'Talat Kardas', 'Talat Odman', 'Tarik Yilmaz', 'Tekin Dereli', 'Temel Yilmaz', 'Tevfik Ozlu', 'Tevfik Uyar', 'Tolga Demiryol', 'Tolga Yazi', 'Tosun Terzioglu', 'Tufan Tukek', 'Tugba Tanyeri Erdemir', 'Tunc Ladin', 'Turhan Yavuz', 'Turkay Demir', 'Ugur Coskun', 'Ugur Sahin', 'Ugur Sak', 'Umit Dundar', 'Umut Yildiz', 'Unsal Oskay', 'Ural Akbulut', 'Utku Buyuksahin', 'Utku Kaya', 'Yalcin Yildirim', 'Yaman Tokat', 'Yelda Ozden Ciftci', 'Yesim Erbil', 'Yesim Tasova', 'Yildiz Otuken', 'Yilmaz Ciftci', 'Yucel Altunbasak', 'Yuksel Yalova', 'Yunus Kilic', 'Yusuf C Kaplan', 'Yusuf Leblebici', 'Yusuf Ozgur Cakmak', 'Yusuf Sevki Hakyemez', 'Yusuf Tekin', 'Zafer Kurugol', 'Zafer Toprak', 'Zehra Cataltepe', 'Zehra Sayers', 'Zeki Aslan', 'Ziya Burhanettin Guvenc', 'Ziya Onis', 'Ziya Selcuk', 'Zumrut Begum Ogel', 'Ali Riza Babaoglan', 'Eren Bali', 'Fatih Ozmen', 'Hakan Yildiz', 'Ibrahim Etem Ulagay', 'Mesut Cevik', 'Nurcin Celik', 'Ahmet Mete Isikara', 'Ahu Arslan Yildiz', 'Alfred Heilbronn', 'Ali Yaramanci', 'Alp Eden', 'Altan Cilingiroglu', 'Amiran Kurtkan Bilgiseven', 'Arif Mufid Mansel', 'Arif Selimov', 'Asaf Savas Akat', 'Asuman Aksoy', 'Asuman Baytop', 'Attila Askar', 'Ayhan Ulubelen', 'Aykan Erdemir', 'Aykut Kence', 'Ayse Gul Altinay', 'Ayse Soysal', 'Aziz Ogan', 'Bahriye Ucok', 'Baykan Sezer', 'Bedri Gencer', 'Betul Tanbay', 'Bulent Usta ', 'Burcin Mutlu Pakdil', 'Cagan Hakki Sekercioglu', 'Caglar Keyder', 'Can Kozanoglu', 'Cem Yalcin Yildirim', 'Cezmi Guner Omay', 'Cicek Kahraman', 'David Winfield ', 'Dicle Kogacioglu', 'Dilhan Eryurt', 'Ekrem Akurgal', 'Emine Caykara', 'Emre Kongar', 'Engin Umut Akkaya', 'Enver Yucel', 'Ergi Deniz Ozsoy', 'Erkan Konyar', 'Erol Cerasi', 'Erol Gungor', 'Ersin Doger', 'Faik Yaltirik', 'Fatin Gokmen', 'Fatma Barbarosoglu', 'Fatma Meral Horne Sever', 'Fatma Muge Gocek', 'Fazil Erdogan', 'Fazila Sevket Giz', 'Fergani', 'Ferhat Ozcep', 'Ferhunde Ozbay', 'Fulya Gurses', 'Galip Ulsoy', 'Gaye Su Akyol', 'Gunes Duru', 'Guven Arsebuk', 'Hakan Savli', 'Hakki Ogelman', 'Halet Cambel', 'Halil Demircioglu', 'Halil Vehbi Eralp', 'Haluk Karamagarali', 'Harun Parlar', 'Hasan Pesmen', 'Hasan Unal Nalbantoglu', 'Hasmet Babaoglu', 'Haydar Bulgak', 'Helmuth Theodor Bossert', 'Hermine Agavni Kalustyan', 'Hilal Kaplan', 'Hulya Senkon', 'Husamettin Arslan', 'Kenan Erim', 'Kerim Altug', 'Kerim Erim', 'Mahmut Akok', 'Masatosi Gunduz Ikeda', 'Mehmed Ali Kagitci', 'Mehmet Cihat Ozonder', 'Mehmet Eymen', 'Mehmet Ozdogan', 'Melih Onus', 'Meliha Terzioglu', 'Mevlut Dinc', 'Muammer Yildiz', 'Mubeccel Kiray', 'Muhibbe Darga', 'Munis Dundar', 'Naside Gozde Durmus', 'Nejat Eczacibasi', 'Nermin Abadan Unat', 'Nermin Arik', 'Nermin Erdentug', 'Nermin Gozukirmizi', 'Nese Ozgen', 'Neva Ciftcioglu', 'Nezih Firatli', 'Nihat Berker', 'Nilufer Cinar Corlulu', 'Niyazi Berkes', 'Nur Banu Molla', 'Nur Vergin', 'Nur Yalman', 'Nuri Bilgin', 'Nuzhet Gokdogan', 'Oguz Gundogdu', 'Oguz Okay', 'Oktay Yurdatapan', 'Orhan Serafettin Icen', 'Ozalp Babaoglu', 'Ozer Ozankaya', 'Paris Pismis', 'Pinar Selek', 'Prens Sabahaddin', 'Ratip Berker', 'Reha Oguz Turkkan', 'Remzi Oguz Arik', 'Remziye Hisar', 'Rennan Pekunlu', 'Riyaziyeci Mehmet Nadir Bey', 'Saadet Ergene', 'Saadet Ozen', 'Sabri Ulgener', 'Sakir Kocabas', 'Sedat Alp', 'Selahattin Kantar', 'Selma Soysal', 'Selman Akbulut', 'Sema Salur', 'Semahat Geldiay', 'Semra Eren Nijhar', 'Sencer Ayata', 'Senol Sunat', 'Serif Mardin', 'Sevket Aziz Kansu', 'Sevket Donmez', 'Seyhan Kurt', 'Seyyid Ahmet Arvasi', 'Sezer Ates Ayvaz', 'Sibel Ozbudun', 'Sinan Unlusoy', 'Sinasi Yildirimli', 'Sitki Alp', 'Tahsin Ozguc', 'Tamer Basar', 'Tevfik Okyay Kabakcioglu', 'Tuna Altinel', 'Tuna Ekim', 'Tuncay Taymaz', 'Turhan Baytop', 'Ufuk Esin', 'Ulug Bahadir Alkim', 'Umit Meric', 'Umit Serdaroglu', 'Volkan Aytar', 'Yakin Erturk', 'Yasemin Cebenoyan', 'Yilmaz Oner', 'Yusuf Vardar', 'Yusuf Yagci', 'Zakir Kadiri Ugan', 'Zekeriya Muyesseroglu', 'Zeki Tufekcioglu', 'Zeynep Tufekci', 'Ziya Gokalp', 'Ziyaeddin Fahri Findikoglu']
# fname='/home/bilgi/Desktop/gogdene.csv'
# for i in name_list[:5]:
#     google_search(i.strip(),fname)
