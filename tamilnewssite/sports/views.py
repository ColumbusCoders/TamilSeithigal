# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
import feedparser
import logging
import sys
sys.path.append("/home/codercol/webapps/django_tamilnewssite/tamilnewssite")
import common as config


# Create your views here.
feeds = config.GetParseResults(config.sport_urls)

def index(request):
    return render(request,'sports/home.html',{'test':feeds})
