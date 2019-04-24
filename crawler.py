"""
Created on Fri Apr 28 15:13:01 2019

@author: maxxx580
"""

import csv
import io
import pprint as pp
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver

url = input('Set base url: ')
fname = input('Enter output file name: ')
path_to_chromedriver = input('Enter driver directory (default path will be used if not set): ')

if not path_to_chromedriver:
    path_to_chromedriver = '/usr/local/bin/chromedriver'

if not fname:
    fname = 'output.csv'

def scroll(url):
    browser = webdriver.Chrome(executable_path = path_to_chromedriver)
    browser.get(url)
    last = browser.execute_script('return document.body.scrollHeight')
    while True:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(5)
        nxt = browser.execute_script('return document.body.scrollHeight')
        if nxt == last:
            break
        else:
            last = nxt
    return browser.page_source

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    twts = []
    
    return twts


if __name__ == "__main__":
    html = scroll(url)
    parse(html)
