from urllib.request import Request, urlopen
from requests import get

# ZIP file download
url_input1 = "https://github.com/sk3ptre/AndroidMalware_2019/raw/master/SubscriberFraud.zip"

# APK file download
url_input2 = 'https://bit.ly/3yhmX6s'

# Move to WEB-page & APK file download(ZouenSogeting)
url_input3 = 'https://bit.ly/3xmCZfj'

# Move to WEB-page & APK file download(Game-360M)
url_input4 = 'https://bit.ly/3hmftti'

# Move to WEB-page & file download
url_input5 = 'https://www.softonic.kr/download/putty/windows/post-download'

#file download
url_input6 = 'https://drive.google.com/uc?export=download&id=1U0zlzuklVKird6UZ3H4vO-2Vt6hPEwB-'


take_url = Request(url_input6, headers={'User-Agent' : 'Mozilla/5.0'})
open_url = urlopen(take_url)

content_type = open_url.headers['content-type']
content_length = open_url.headers['content-length']
headers = open_url.headers.__dict__
check_body = open_url.read()

print('content-type -> '+ content_type)
print('content-length -> '+ str(content_length))
print('Headers -> '+ str(headers))
#print('Body : '+ str(check_body))
