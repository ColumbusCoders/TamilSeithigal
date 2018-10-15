# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import feedparser
import sys
sys.path.append("/home/codercol/webapps/django_tamilnewssite/tamilnewssite")
import common as config

# Create your views here.

feeds_bbc = config.GetParseResults(config.divine_urls)
for i in feeds_bbc:
    print ("testing ---->")
    print (i.desc)

def index(request):
    return render(request,'divine/home.html',{'divine':feeds_bbc})
