from selenium import webdriver
import time
"""
options = webdriver.ChromeOptions()

options.add_argument('headless')

options.add_argument('window-size=1920x1080')

options.add_argument("disable-gpu")
"""
# driver = webdriver.Chrome('chromedriver', chrome_options=options)
driver = webdriver.Chrome


elem = driver.find_element_by_name("query")

elem.send_keys("두진이바보")

elem.send_keys(keys.RETURN)
time.sleep(2)


soup = BeautifulSoup(driver.page_source, 'html.parser')

print(soup)
