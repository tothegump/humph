#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


classifiers = ['License :: OSI Approved :: MIT License']

setup(name='humph',
      version='%s.%s.%s' % (0, 0, 1),
      description='The nothing to lose Python web framework.',
      long_description=open('README.md').read(),
      author='tothegump',
      author_email='tothegump@gmail.com',
      url='http://github.com/tothegump/humph/',
      py_modules=['humph'],
      license='MIT',
      classifiers=classifiers,
      )
