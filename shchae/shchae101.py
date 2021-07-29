from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

driver = webdriver.Chrome('chromedriver', chrome_options=options)

from selenium.webdriver.common.keys import Keys


url = 'https://ko.rakko.tools/tools/11/'
driver.get(url)

driver.implicitly_wait(3)

# driver.execute_script("location.reload()")

elem = driver.find_element_by_id("serchIp")
elem.send_keys("www.naver.com")
elem.send_keys(Keys.RETURN)


from bs4 import BeautifulSoup

driver.implicitly_wait(3)


"""
elem = driver.find_element_by_class_name("txt_gray")
elem.send_keys("안녕하세오 반갑숩니다")

elem = driver.find_element_by_class_name("btn_check")
elem.click()
"""
# soup = BeautifulSoup(html, 'html.parser')

soup = BeautifulSoup(driver.page_source, 'html.parser')

print(soup)
# time.sleep(2)
#country = soup.find_all("td", {"span class":"country_name"})
#print(country)
#print(soup.select("td.country_name").text)
"""
for x in soup:
    print(x.text)
"""
# (소중한거 안사라지게 조심조심) print(soup.find_all("td"))

# print(soup.find_all("td"))


driver.quit()

