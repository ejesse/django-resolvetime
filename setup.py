#!/usr/bin/env python

from distutils.core import setup

setup(name='Django Resolve Time',
      version='1.0',
      description='This is a templatetag to convert a datetime object to a format that reflects the time difference between now and the time of given datetime object',
      author='Kasun Herath',
      author_email='kasunh01 at gmail dot com',
      url='https://github.com/kasun/django-resolvetime',
      packages=['resolvetime'],
     )