#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from pelicanconf import *

SITEURL = 'http://pythonbrasil.github.io/wiki'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds.atom'
FEED_ALL_RSS = 'feeds.rss'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

GOOGLE_ANALYTICS_CODE = 'UA-62093919-3'
