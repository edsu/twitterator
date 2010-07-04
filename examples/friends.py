#!/usr/bin/env python

"""
usage: friends.py nick
"""

import sys
import twitterator

username = sys.argv[1]

twitter = twitterator.Twitter()
for follower in twitter.statuses_friends(screen_name=username):
    print ("%(name)s [%(screen_name)s]" % follower).encode('utf-8')
