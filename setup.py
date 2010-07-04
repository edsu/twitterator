# bootstrap easy_install

from setuptools import setup

setup( 
    name = 'twitterator',
    version = '0.2',
    url = 'http://python.org/pypi/twitterator',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    license = 'http://creativecommons.org/licenses/publicdomain/',
    packages = ['.'],
    description = 'iterating functions for twitter api',
    test_suite = 'tests',
    requires = ['httplib2']
)
