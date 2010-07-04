import unittest

import twitterator

class TwitterTests(unittest.TestCase):

    def test_user(self):
        t = twitterator.Twitter()
        u = t.users_show(screen_name='edsu')
        self.assertEqual(u['id'], 14331818)

    def test_statuses_followers(self):
        t = twitterator.Twitter()
        count = 0
        for follower in t.statuses_followers(screen_name='t'):
            self.assertTrue(follower['screen_name'])
            if count > 200:
                break
            count += 1
        self.assertEqual(count, 201)

    def test_statuses_friends(self):
        t = twitterator.Twitter()
        count = 0
        for friend in t.statuses_friends(screen_name='t'):
            self.assertTrue(friend['screen_name'])
            if count > 200:
                break
            count += 1
        self.assertEqual(count, 201)
