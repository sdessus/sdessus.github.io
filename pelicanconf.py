#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
from os import listdir
from os.path import isfile, join
import yaml, json, sys
import shutil

AUTHOR = 'Maïlys et Sylvain'
SITENAME = 'Des voyages, une aventure'
SITEURL = ''
GITHUB_URL = 'https://github.com/sdessus/sdessus.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('GSCF - Considérez faire un don, svp', 'pages/Dons.html'),
         ('Adventure Bag - Considérez faire un geste, svp', 'https://www.journeyera.com/adventure-bag/'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Specify name of a built-in theme
THEME = "pelican-themes/medius"

#Staticman Comments
# STATIC_PATHS = ['comments','images']
# commentsPath = "./content/comments"

# def ymlToJson(file):
#     with open(commentsPath + "/" + file) as stream:
#         return yaml.load(stream)

# commentsYML = [f for f in os.listdir(commentsPath) if os.path.isfile(join(commentsPath, f))]
# COMMENTS = list(map(ymlToJson, commentsYML))

# # shutil.copytree("./content/comments","./output/comments")
# shutil.copy ("staticman.yml","./output")