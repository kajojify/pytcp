from setuptools import find_packages
from distutils.core import setup

setup(name='pytcp',
      version='0.1.0',
      description='Simple Python 3 async TCP server application.',
      author='Samoilenko Roman',
      author_email='ttahabatt@gmail.com',
      url='https://github.com/kajojify/pytcp',
      packages=find_packages(exclude=['*.pyc']),
      scripts=['bin/pytcp'],
      )