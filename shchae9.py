from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_argument('headless')
# options.add_argument('window-size=1920X1080')
# options.add_argument("disable-gpu")

driver = webdriver.Chrome('chromedriver', chrome_options=options)
import time


driver.get('https://ko.rakko.tools/tools/11/https://ko.rakko.tools/tools/11/')
elem = driver.find_element_by_class_name("one_column_box_search_area")
elem.send.keys("www.naver.com")
elem = driver.find_element_by_class_name("black_btn")
elem.click()

# elem.send_keys(Keys.RETURN)

time.sleep(3)

# driver.implicitly_wait(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
a = soup.select("div.res_tbl") 
print(a)

driver.quit()


"""


driver = webdfiveer.chrome
driver.get("http://afdasfas")

elem = driver.find_element_by_name("query")
elem.send_keys("거니")
elem.send_keys(Keys.RETURN)



elem = driver.find_element_by_class_name("txt_gray")
elem.send_keys("안녕하세요 반갑숩니다.")

elem = driver.find_element_by_class_name("btn_check")
elem.click()

soup = beautifulsoup(driver.page_source, 'html.parser')

"""
