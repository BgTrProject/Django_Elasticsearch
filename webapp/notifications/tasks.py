from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time
import requests
import bs4
from bs4 import BeautifulSoup
from newsplease import *
import cloudscraper

def filter_rss(a,b):
    k = False
    for i in a:
        if str(i)==str(b):
            k=True

    return k

def sifirla(a,b,c):
    for i in b:
        if i not in a:
            c.append(i)
    return c



# a=['a','b','c','d','e']
# b='f'
# h=filter_rss(a,b)
# print(h)

@shared_task()
def sum(a=2,b=3):
    print(a)
    print(b)

    time.sleep(2)
    for i in range(65565):
        if b>100:
            break
        else:
            time.sleep(3)
            return sum(a+b,a*b)






@shared_task()
def get_rss_task():
    f_links=[]
    chk_links=[]
    tmp_links=[]
    counter=0

    my_rss_links=['http://feeds.bbci.co.uk/turkce/rss.xml','https://www.sabah.com.tr/rss/teknoloji.xml','https://www.cnnturk.com/feed/rss/bilim-teknoloji/news','https://www.yeniakit.com.tr/rss/haber/teknoloji','https://www.yenisafak.com/rss?xml=teknoloji','http://www.internethaber.com/rss','http://www.turkiyehaberajansi.com/rss.xml']

    for i in range(65565):

        print("========================================================================")
        print("started to get RSS")
        print("========================================================================")
        time.sleep(2)
        for url in my_rss_links:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'xml')


            for entry in soup.find_all('item'):
                surl2 = entry.find('link').text

                article = NewsPlease.from_url(surl2.strip())
                # a = article.url
                # f_links.append(surl2)
                my_logic=filter_rss(f_links,surl2)
                if my_logic==True:
                    print("####################")
                    print("already exist passing")
                    print("####################")
                    time.sleep(2)
                    continue
                else:
                    try:
                        a = entry.find('link').text
                        f_links.append(a)
                        chk_links.append(a)


                    except:

                        a = "None"
                    try:
                        b = e.text if (e := entry.find('pubDate')) else None
                    except:
                        b = "None"
                    try:
                        c = entry.find('title').text
                    except:
                        c = "None"
                    try:
                        d = article.maintext
                        d = " ".join(d.split())
                    except:
                        d = "None"

                    w_data = "{} ; {} ; {} ; {}".format(a.strip(), b.strip(), c.strip(), d.strip())
                    print(w_data)
                    with open('/home/bilgi/PycharmProjects/elastic/webapp/g_upload/tr_rss_denemem_3.txt', 'a') as file:
                        file.write(w_data + '\n')


                print("********** {} gazetesi haber sonu **********".format(surl2[:25]))
                time.sleep(8)


        print("****************************************************")
        print("starting to sleeeppppppppppp")
        time.sleep(2400)
        print("6 saat geçildiğini varsayalım ...end of sleep")
        print("****************************************************")
        counter+=1
        time.sleep(2)
        if counter%12==0:
            print("__---__---___----__ GÜN SONU SIFIRLAMA _--__---__---")
            print(" 24 saat geçildiği varsayılıyor ")
            print("__---__---___----__ GÜN SONU SIFIRLAMA _--__---__---")
            time.sleep(28)
            f_links= []

            # f_links=sifirla(f_links,chk_links,tmp_links)

        else:
            pass




@shared_task()
def get_rss_task_en():
    f_links_en=[]
    chk_links_en=[]
    tmp_links_en=[]
    counter_en=0

    my_rss_links_en=['http://feeds.bbci.co.uk/news/rss.xml','https://tr.sputniknews.com/export/rss2/archive/index.xml','https://www.ft.com/world?format=rss','https://www.standard.co.uk/news/rss']
    for i in range(65565):
        print("========================================================================")
        print("started to get RSS")
        print("========================================================================")
        time.sleep(2)
        for url in my_rss_links_en:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'xml')
            for entry in soup.find_all('item'):
                surl2 = entry.find('link').text
                article = NewsPlease.from_url(surl2.strip())
                # a = article.url
                # f_links.append(surl2)
                my_logic=filter_rss(f_links_en,surl2)
                if my_logic==True:
                    print("####################")
                    print("already exist passing")
                    print("####################")
                    time.sleep(2)
                    continue
                else:
                    try:
                        a = entry.find('link').text
                        f_links_en.append(a)
                    except:
                        a = "None"
                    try:
                        b = e.text if (e := entry.find('pubDate')) else None
                    except:
                        b = "None"
                    try:
                        c = entry.find('title').text
                    except:
                        c = "None"
                    try:
                        d = article.maintext
                        d = " ".join(d.split())
                    except:
                        d = "None"
                    w_data_en = "{} ; {} ; {} ; {}".format(a.strip(), b.strip(), c.strip(), d.strip())
                    print(w_data_en)
                    with open('/home/bilgi/PycharmProjects/elastic/webapp/g_upload/en_rss_denemem_3.txt', 'a') as file:
                        file.write(w_data_en + '\n')


                print("********** {} gazetesi haber sonu **********".format(surl2[:25]))
                time.sleep(6)
        print("****************************************************")
        print("starting to sleeeppppppppppp")
        time.sleep(2400)
        print("6 saat geçildiğini varsayalım ...end of sleep")
        print("****************************************************")
        counter_en+=1
        time.sleep(2)
        if counter_en%12==0:
            print("__---__---___----__ GÜN SONU SIFIRLAMA _--__---__---")
            print(" 24 saat geçildiği varsayılıyor ")
            print("__---__---___----__ GÜN SONU SIFIRLAMA _--__---__---")
            time.sleep(23)
            f_links_en=[]
        else:
            pass



@shared_task()
def get_rss_task_eu():
    f_links_eu=[]
    chk_links=[]
    counter_eu=0

    my_rss_links_eu=['https://www.dnevnik.bg/rss/','https://gong.bg/rss','http://www.vesti.bg/rss.php','https://dariknews.bg/rss.php','https://www.24chasa.bg/rss']
    for i in range(65565):

        print("========================================================================")
        print("started to get RSS")
        print("========================================================================")
        time.sleep(2)
        for url in my_rss_links_eu:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'xml')


            for entry in soup.find_all('item'):
                surl2 = entry.find('link').text

                article = NewsPlease.from_url(surl2.strip())
                # a = article.url
                # f_links.append(surl2)
                my_logic=filter_rss(f_links_eu,surl2)
                if my_logic==True:
                    print("####################")
                    print("already exist passing")
                    print("####################")
                    time.sleep(2)
                    continue
                else:
                    try:
                        a = entry.find('link').text
                        f_links_eu.append(a)
                    except:

                        a = "None"
                    try:
                        b = e.text if (e := entry.find('pubDate')) else None
                    except:
                        b = "None"
                    try:
                        c = entry.find('title').text
                    except:
                        c = "None"
                    try:
                        d = article.maintext
                        d = " ".join(d.split())
                    except:
                        d = "None"

                    w_data_eu = "{} ; {} ; {} ; {}".format(a.strip(), b.strip(), c.strip(), d.strip())
                    print(w_data_eu)
                    with open('/home/bilgi/PycharmProjects/elastic/webapp/g_upload/bg_rss_denemem_3.txt', 'a') as file:
                        file.write(w_data_eu + '\n')


                print("********** {} gazetesi haber sonu **********".format(surl2[:25]))
                time.sleep(2)


        print("****************************************************")
        print("starting to sleeeppppppppppp")
        time.sleep(2400)
        print("6 saat geçildiğini varsayalım ...end of sleep")
        print("****************************************************")
        counter_eu+=1
        time.sleep(2)
        if counter_eu%12==0:
            print("__---__---___----__ GÜN SONU SIFIRLAMA _--__---__---")
            print(" 24 saat geçildiği varsayılıyor ")
            print("__---__---___----__ GÜN SONU SIFIRLAMA _--__---__---")
            time.sleep(20)
            f_links_eu=[]
        else:
            pass



# teknoloji haberleri
@shared_task()
def get_rss_task_tekno():
    # from celery import shared_task
    # import time
    # import requests
    # import bs4
    # from bs4 import BeautifulSoup
    # from newsplease import *
    # import cloudscraper
    # scraper = cloudscraper.create_scraper(delay=10, browser='firefox')
    f_links_tekno = []
    chk_links = []
    counter_tekno = 0
    my_rss_links_tekno2 = 'https://www.ntv.com.tr/teknoloji.rss','https://www.yenisafak.com/teknoloji/rss'
    my_rss_links_tekno = ['https://www.cumhuriyet.com.tr/rss/10.xml','http://www.hurriyet.com.tr/rss/teknoloji','https://www.yenisafak.com/teknoloji/rss','https://www.star.com.tr/rss/rss.asp?cid=124','https://www.takvim.com.tr/rss/teknoloji.xml','https://www.mansetturkiye.com/rss_teknoloji_15.xml','https://www.yeniakit.com.tr/rss/haber/teknoloji','https://www.ahaber.com.tr/rss/teknoloji.xml','https://www.cnnturk.com/feed/rss/teknoloji','http://www.ensonhaber.com/rss/teknoloji.xml','http://www.mynet.com/haber/rss/kategori/teknoloji/',"https://www.sozcu.com.tr/rss/bilim-teknoloji.xml"]
    for i in range(65565):
        print("========================================================================")
        print("started to get RSS")
        print("========================================================================")
        time.sleep(2)
        for url in my_rss_links_tekno:
            # resp = scraper.get(url)
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'xml')
            e_name=soup.find_all('item')
            # if len(e_name)==0:
            #     req = scraper.get(url)
            #     # soup = BeautifulSoup(req.text, "html.parser")
            #     # resp = requests.get(url)
            #     soup = BeautifulSoup(req.text, 'xml')
            #     e_name = soup.find_all('item')
            # else:
            #     continue
            print(len(e_name))
            print(url)
            # print(e_name[-1])
            #
            # try:
            #     if  len(e_name)==0:
            #         e_name2=soup.find_all('entry')
            #         print("??????")
            #
            #         print(len(e_name2))
            #         print("==================")
            #     else:
            #         pass
            # except:
            #     pass

            for entry in soup.find_all('item'):
                surl2 = entry.find('link').text
                article = NewsPlease.from_url(surl2.strip())
                # article.download()
                a = article.url
                print(a)
                # f_links_tekno.append(surl2)
                my_logic = filter_rss(f_links_tekno, surl2)
                if my_logic == True:
                    print("####################")
                    print("already exist passing")
                    print("####################")
                    time.sleep(2)
                    continue
                else:
                    try:
                        a = entry.find('link').text
                        f_links_tekno.append(a)
                    except:

                        a = "None"
                    try:
                        b = e.text if (e := entry.find('pubDate')) else None
                    except:
                        b = "None"
                    try:
                        c = entry.find('title').text
                    except:
                        c = "None"
                    try:
                        # article.download()
                        d = article.maintext
                        d = " ".join(d.split())

                    except:
                        d =art.text if (art := entry.find('description')) else None
                    w_data_tekno = "{} ; {} ; {} ; {}".format(a.strip(), b.strip(), c.strip(), d.strip())
                    print(w_data_tekno)
                    with open('/home/bilgi/PycharmProjects/elastic/webapp/g_upload/bg_rss_teknoloji_9.txt',
                              'a') as file:
                        file.write(w_data_tekno + '\n')

                print("********** {} gazetesi haber sonu **********".format(surl2[:25]))
                time.sleep(2)

        print("****************************************************")
        print("starting to sleeeppppppppppp")
        time.sleep(2400)
        print("6 saat geçildiğini varsayalım ...end of sleep")
        print("****************************************************")
        counter_tekno += 1
        time.sleep(2)
        if counter_tekno % 12 == 0:
            print("__---__---___----__ GÜN SONU SIFIRLAMA _--__---__---")
            print(" 24 saat geçildiği varsayılıyor ")
            print("__---__---___----__ GÜN SONU SIFIRLAMA _--__---__---")
            time.sleep(20)
            f_links_tekno = []
        else:
            pass

        # https://www.ntv.com.tr/teknoloji.rss
        # https://www.cumhuriyet.com.tr/rss/10.xml
        # http://www.hurriyet.com.tr/rss/teknoloji
        # http://www.milliyet.com.tr/rss/rssNew/teknolojiRss.xml
        # https://www.star.com.tr/rss/rss.asp?cid=124
        # https://www.takvim.com.tr/rss/teknoloji.xml
        # https://www.mansetturkiye.com/rss_teknoloji_15.xml
        # https://www.yeniakit.com.tr/rss/haber/teknoloji
        # https://www.yenisafak.com/rss?xml=teknoloji
        # https://www.ahaber.com.tr/rss/teknoloji.xml
        # https://www.cnnturk.com/feed/rss/bilim-teknoloji/news
        # http://www.ensonhaber.com/rss/teknoloji.xml
        # http://www.mynet.com/haber/rss/kategori/teknoloji/
#
#










# def filter_rss(a,b):
#     k = False
#     for i in a:
#         if str(i)==str(b):
#             k=True
#
#     return k
#
#
# import time
# import requests
# import bs4
# from bs4 import BeautifulSoup
# my_rss_links=['http://feeds.bbci.co.uk/turkce/rss.xml','https://www.sabah.com.tr/rss/teknoloji.xml','https://www.cnnturk.com/feed/rss/bilim-teknoloji/news','https://www.yeniakit.com.tr/rss/haber/teknoloji','https://www.yenisafak.com/rss?xml=teknoloji','http://www.internethaber.com/rss','http://www.turkiyehaberajansi.com/rss.xml']
# links=[]
# b=[]
# tmp=[]
# for i in range(65565):
#
#     print("========================================================================")
#     print("started to get RSS")
#     print("========================================================================")
#
#     counter = 0
#     for url in my_rss_links:
#         resp = requests.get(url)
#         soup = BeautifulSoup(resp.text, 'xml')
#         for entry in soup.find_all('item'):
#             surl2 = entry.find('link').text
#             counter+=1
#             my_logic = filter_rss(links, surl2)
#             links.append(surl2)
#         print(counter)
#     print("summary")
#     print(len(links))
#     for i in links:
#         if i not in b:
#             b.append(i)
#             tmp.append(i)
#         else:
#             pass
#     print(len(b))
#     print(len(tmp))
#     print("----------------")
#     print(links)
#     print(b)
#     print(tmp)
#     tmp=[]
#     time.sleep(240)

