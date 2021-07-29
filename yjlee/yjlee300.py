 
import hashlib
import binascii
import requests
import urllib
import urllib3
import json
import shutil
#import urllib.request
import os       
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


take_url = Request(url_input2, headers={'User-Agent' : 'Mozilla/5.0'})
open_url = urlopen(take_url)

#다운로드 할 파일 이름 설정
url_list = list(url_input2.split('/'))
url_len = len(url_list)
url_name_num = int(url_len) - 1

url_last = url_list[url_name_num]

file_name = url_last[0:3]

#apk파일에 확장자 붙이기
content_type = open_url.headers['content-type']
apk_file = 'vnd.android.package-archive'

if apk_file in content_type:
    file_rename = file_name + '.apk'
else:
    file_rename = file_name

#파일 다운로드하기
with open(file_rename, "wb") as file:
    response = get(url_input2)
    file.write(response.content)

# #파일 삭제...
# path = '/home/checkurl/'
# file_list = os.listdir(path)
# print(str(file_list))
# print(path + file_rename)

# if '.apk' in str(file_list):
#     os.remove(path + file_rename)
# else:
#     print('======')