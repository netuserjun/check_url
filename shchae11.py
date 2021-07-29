import requests

url = "http://media.daum.net"
url = "media.daum.net"

try:
    rsp = requests.get(url)
except requests.exceptions.HTTPError:
    print("http 에러가 발생")
except requests.exceptions.Timeout:
    print("Tim Out 에러가 발생")
except requests.exceptions.MissingSchema:
    print("http, https 를 추가해 주세요")

from selenium import webdriver
url = 'https://nid.naver.com/nidlogin.login'

# 가상 브라우저를 활성화
driver = webdriver.PhantomJS()
driver.get(url) 
select_id = driver.find_element_by_id('id')
print("session정보 : \n{}\ntag 이름 : {}\ntetxt 내용 : {}".format(
    select_id,  select_id.tag_name, select_id.text))
