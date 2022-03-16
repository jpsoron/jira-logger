"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

APP = ['MainMenu.py']
DATA_FILES = []
OPTIONS = {}

setup(
    name='JiraLogger',
    version='1.0',
    description='Jira Logger for Python',
    author='Juan Sorondo',
    author_email='jsorondog@gmail.com',
    app=APP,
    data_files=DATA_FILES,
    setup_requires=required,
)