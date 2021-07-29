from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://ko.rakko.tools/tools/11/")  
bsObject = BeautifulSoup(html, "html.parser") 
print (bsObject.head.find("meta", {"name":"description"}).get('content'))

print(bsObject.head.title) # 웹 문서 전체가 출력됩니다.
