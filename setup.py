#!/usr/bin/env python

from distutils.core import setup
import setuptools

setup(name='gnca',
      version='1.0',
      description='Decentralized GNCA',
      author='Daniele Grattarola, Lorenzo Livi, Cesare Alippi',
      author_email='grattd@usi.ch',
      url='https://github.com/danielegrattarola/GNCA',
      packages=setuptools.find_packages("gnca"),
     )