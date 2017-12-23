#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS = ['plugins']
PLUGINS = ['jinja_filters']

AUTHOR = u'Fluxoid Ltd.'
DESCRIPTION = u'Site description'
FOOTER_TEXT = u'Copyright &copy; Fluxoid Ltd. 2017'
SITENAME = u'Cyclismo by Fluxoid Ltd.'
SITEURL = 'http://127.0.0.1:8000'

NAVBAR = {
  'title' : u'Cyclismo by Fluxoid Ltd.',
  'link': u'/index.html'
}

MENUITEMS = (
    ('GitHub', 'https://github.com/fluxoid-org/CyclismoProject'),
    ('About Fluxoid', 'https://www.fluxoid.org'),
    ('About Cyclismo', '/pages/the-story.html'),
)

PAGE_HEADING = {
  'title' : u'Cyclismo',
  'subtitle': u'Free and open-source cycling simulator for Android',
  'button_text': u'Available on GitHub',
  'button_link': u'https://github.com/fluxoid-org/CyclismoProject'
}

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Anything tagged with these will be added to the respective area
CAROUSEL_TAG = 'carousel'
FEATURETTE_TAG = 'featurette'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../FluxoidOnePageWonder/'
