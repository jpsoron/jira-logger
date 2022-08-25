from distutils.core import setup
import py2exe
import jiralogger

setup(
    console=[{"script" : "./jiralogger/MainMenu.py","dest_base" : "JiraLogger"}]
)