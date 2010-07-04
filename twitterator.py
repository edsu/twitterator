#!/usr/bin/env python

import json
from urllib import urlencode

import httplib2

class Cursor(object):

    def __init__(self, json_key):
        self.json_key = json_key

    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            kwargs['cursor'] = -1
            while True:
                data = f(*args, **kwargs)
                for obj in data[self.json_key]:
                    yield obj
                if data['next_cursor']:
                    kwargs['cursor'] = data['next_cursor']
                else:
                    break
        return wrapped_f


class Twitter:

    def __init__(self, username=None, password=None):
        self.h = httplib2.Http()
        if username and password:
            self.h.add_credentials(username, password)

    def users_show(self, user_id=None, screen_name=None):
        p = {}
        if user_id:
            p['user_id'] = user_id
        elif screen_name:
            p['screen_name'] = screen_name
        else:
            raise RuntimeError("must pass in either user_id or screen_name")
        u = 'https://twitter.com/users/show.json?' + urlencode(p)
        r, j = self.h.request(u)
        return json.loads(j)

    @Cursor('users')
    def statuses_followers(self, user_id=None, screen_name=None, cursor=-1):
        p = {'cursor': cursor}
        if user_id:
            p['user_id'] = user_id
        elif screen_name: 
            p['screen_name'] = screen_name
        else:
            raise RuntimeError("must pass in either user_id or screen_name")
        u = 'https://twitter.com/statuses/followers.json?' + urlencode(p)
        r, j = self.h.request(u)
        return json.loads(j)

    @Cursor('users')
    def statuses_friends(self, user_id=None, screen_name=None, cursor=-1):
        p = {'cursor': cursor}
        if user_id:
            p['user_id'] = user_id
        elif screen_name:
            p['screen_name'] = screen_name
        else:
            raise RuntimeError("must pass in either user_id or screen_name")
        u = 'https://twitter.com/statuses/friends.json?' + urlencode(p)
        r, j = self.h.request(u)
        return json.loads(j)


