"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# import webapp.webapp.views
from .views import *
import re
from django.urls import path
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from django.conf.urls.static import static

from .settings import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    # # path('',home_view),
    path('',index),
    path('index',index),
    path('arama',arama),
    path('contact',contact),
    path('get_rss',get_rss),
    path('rss_get_news',rss_get_news),
    path('rss_file_upload',rss_file_upload),
    path('txt_to_elastica',txt_to_elastica),
    path('txt_file_upload',txt_file_upload),
    path('txt_to_elastic',txt_to_elastic),

    path('newspaper_get_news',newspaper_get_news),
    path('newspaper_date_file_upload', newspaper_date_file_upload),
    path('newspaper_name_file_upload', newspaper_name_file_upload),
    path('get_newspaper_crawl',get_newspaper_crawl),


    path('arama',arama,name="arama"),
    path('search/', PublisherDocumentView.as_view({'get': 'list'})),
    path('admin/', admin.site.urls),


]
# +static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
if settings.DEBUG:
  urlpatterns += static(settings.DOWNLOAD_G_URL, document_root=settings.DOWNLOAD_G_ROOT) #If uploading is the only thing, and the file is not meant to be displayed or read, you don't need to add this
