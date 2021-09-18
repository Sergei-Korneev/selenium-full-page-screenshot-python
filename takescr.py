#!/usr/bin/python
#The script takes a screenshot of a webpage
#Sergei Korneev 2021

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

_url=sys.argv[1]
_file=sys.argv[2]

def _getscr(_url,_file):
        width="900"
        CHROME_PATH = '/usr/bin/google-chrome'
        CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
        WINDOW_SIZE = width+",500"

        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--hide-scrollbar")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.binary_location = CHROME_PATH

 
        driver = webdriver.Chrome(
                executable_path=CHROMEDRIVER_PATH,
                options=chrome_options
            )  

        driver.get(_url)


# from here http://stackoverflow.com/questions/1145850/how-to-get-height-of-entire-document-with-javascript
        js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'

        scrollheight = driver.execute_script(js)
        driver.set_window_size(width, scrollheight)
        driver.save_screenshot(_file)
        driver.quit()



_getscr(_url,_file)
