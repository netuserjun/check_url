from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

driver.get('http://naver.com')

driver.implicitly_wait(3)
driver.get_screenshot_as_file('naver_main.png')

driver.quit()

"""
url = "https://www.naver.com"

browser = webdriver.PhantomJS()

browser.implicitly_wait(3)
browser.get(url)
print('class="logo_naver"')
browser.save_screenshot("Website.png")
browser.quit()

"""
