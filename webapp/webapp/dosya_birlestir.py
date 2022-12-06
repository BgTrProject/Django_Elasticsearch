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