#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'admin'
SITENAME = u'GLUG-Madurai'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = './themes/glug-madurai-theme'

def generate_menu_links_with_site_url(list_of_links_tuple, site_url):
    MENUITEMS = []
    for item in list_of_links_tuple:
        if item[1].startswith("/"):
            MENUITEMS.append((item[0], site_url+item[1]))
        else:
            MENUITEMS.append(item)
    return MENUITEMS

MENULINKS = [
    ('About', '/pages/about.html'),
    ('Mailing List', '/pages/mailing-list.html'),
    ('Meetings', '/pages/meetings.html'),
    ('Announcements', '/category/announcements.html'),
    ('Events', '/category/events.html'),
    ('FStival', 'http://www.fstival.org/'),
]

MENUITEMS = generate_menu_links_with_site_url(MENULINKS, SITEURL)

DISPLAY_PAGES_ON_MENU = False

# Custom setting
SITE_HEADER_IMAGE = 'gnu.svg'
SITE_HEADER_IMAGE_ALT_TEXT = 'GNU Head'
COPYRIGHT_MESSAGE = '&copy; 2011, 2015 GLUG-Madurai. All trademarks and copyrights on this page are owned by their respective owners.'

SHOW_FEED_LINKS = False
SHOW_CATEGORIES = False
SHOW_LINKS = False
SHOW_SOCIAL = False
PAGE_ORDER_BY = 'reversed-date'
