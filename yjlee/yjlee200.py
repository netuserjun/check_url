import hashlib
import binascii
import requests
import urllib
import urllib3
import os
#import urllib.request


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

url_list = list(url_input2.split('/'))
url_len = len(url_list)
url_name_num = int(url_len) - 1

url_last = url_list[url_name_num]
#print(type(url_last)) -> str

file_name = url_last[0:3]
#print(type(file_name)) -> str
#print('FILE NAME : {}'.format(file_name))


#apk파일에 확장자 붙이기
content_type = open_url.headers['content-type']
apk_file = 'vnd.android.package-archive'

if apk_file in content_type:
	file_rename = file_name + '.apk'
	#print('If_type : {}'.format(type(file_rename)))
else:
	file_rename = file_name
	#print('Else_type : {}'.format(type(file_rename)))

with open(file_rename, "wb") as file:
	response = get(url_input2)
	file.write(response.content)

sha256_data = hashlib.sha256(response.content).hexdigest()
print('hash : '+sha256_data)

#os.remove('/home/checkurl/{}'.format(file_rename))


'''
v_file = open(file_name, "rb")
data = v_file.read()
v_file.close()
'''



'''
with open(file_name, "wb") as file:
	response = get(url_input2)
	file.write(response.content)

take_url = Request(url_input2, headers={'User-Agent' : 'Mozilla/5.0'})
open_url = urlopen(take_url)
content_type = open_url.headers['content-type']
print(content_type)

apk_file = 'vnd.android.package-archive'

if apk_file in str(content_type):
	old_name = file_name
	new_name = file_name + '.apk'
	file_rename = os.rename(old_name, new_name)

else:
    pass
'''