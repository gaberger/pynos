#!/usr/bin/env python
'''
Setup for pynos
'''
from setuptools import setup, find_packages

setup(name='pynos',
      version='1.0.0',
      description='Brocade NOS Library.',
      author='Brocade Communications, LLC',
      author_email='mstone@brocade.com',
      url='http://www.brocade.com/',
      packages=find_packages(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Networking'
      ])
