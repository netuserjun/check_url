from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS('/usr/local/lib/python3.6/site-packages')
driver.get("http://www.naver.com")

options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")


print(driver.current_url)


"""
print(driver.title)
elem=driver.find_element_by_name("q")

elem.clear()

elem.send_keys(Keys.RETURN)

driver.set_window_size(1400,1000)
elem.screenshot("pycon_event.png")
assert "No results found." not in driver.page_source

driver.quit()
"""
