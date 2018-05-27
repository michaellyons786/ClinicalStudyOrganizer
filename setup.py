# Code borrowed from https://github.com/pypa/sampleproject

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(name='clinical study organizer',
      version='1.0',
      description='An evolving system for constructing robust studies',
      py_modules=['clinical_study_organizer'],
      author_email='mylonsru@gmail.com',
      author="Michael Lyons",
      package_dir = {'': 'src'}
      )