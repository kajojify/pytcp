from setuptools import find_packages
from distutils.core import setup
from pytcp import version

setup(name='pytcp',
      version=version,
      description='Simple Python 3 async TCP server application.',
      author='Samoilenko Roman',
      author_email='ttahabatt@gmail.com',
      long_description=open('README.md').read(),
      url='https://github.com/kajojify/pytcp',
      packages=find_packages(exclude=['*.pyc']),
      scripts=['bin/pytcp']
      )
