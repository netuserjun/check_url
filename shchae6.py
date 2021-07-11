from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument("--headless")
bs_driver=webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\chromedriver')

import sys
import io
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

print(sys.version)
chrome_options=Options()
chrome_options.add_argument("--headless")
bs_driver=webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\chromedriver')

bs_driver.get('www.naver.com')
bs_driver.find_element_by_xpath('').click()

bs_driver.find_element_by_xpath('').send_keys('')

bs_driver.quit()
