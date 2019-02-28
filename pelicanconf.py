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
         ('Adventure Bag - Considérez faire un geste, svp', 'https://www.journeyera.com/adventure-bag/'),
         ('Fondation Mudita', 'http://mudita-foundation.org/'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Specify name of a built-in theme
THEME = "pelican-themes/medius"
MEDIUS_AUTHORS = {
    'Maïlys et Sylvain': {
        'description': """
            Juste un couple qui voyage
        """,
        'cover': '../images/Author/Font_author.jpg',
        'image': '../images/Author/Avatar.jpg',
        'links': (('envelope', 'mailto:mailyssylvain0209@gmail.com'),)
    }
}
DISPLAY_CATEGORIES_ON_MENU = False

# Test pour tuto Maïlys
# MENUITEMS = (('Les tutos de Maïlys','Tuto_Mailys.html'),)

#Staticman Comments
commentsPath = "./comments_blog_tdm/comments"

def ymlToJson(file):
    with open(commentsPath + "/" + file) as stream:
        return yaml.load(stream)

commentsYML = [f for f in listdir(commentsPath) if isfile(join(commentsPath, f))]
COMMENTS = list(map(ymlToJson, commentsYML))