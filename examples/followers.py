#!/usr/bin/env python

"""
usage: followers.py nick
"""

import sys
import twitterator

username = sys.argv[1]

twitter = twitterator.Twitter()
for follower in twitter.statuses_followers(screen_name=username):
    print ("%(name)s [%(screen_name)s]" % follower).encode('utf-8')
