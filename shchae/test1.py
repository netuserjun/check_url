"""
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
chrome_options=Options()
display=Display(visible=0,size=(800,800))
display.start()

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
"""




from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Options = webdriver.ChromeOptions()
#Options.add_argument('headless')
#Options.add_argument('window-size=1920X1080')
#Options.add_argument("disable-gpu")

chrome_options=Options()
print("cp1")
chrome_options.add_argument('--headless')
print("cp2")

driver = webdriver.Chrome(execuable_path ='/usr/local/bin/chromedriver', chrome_options=chrome_options)

import time
 
driver.get('https://www.naver.com')
elem = headless_driver.find_element_by_class_name("login_msg")
print("cp3")

time.sleep(3)
print("cp4")

soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.select('p.login_msg')[0].text)
 
driver.quit()

