import hashlib
import binascii
import requests
import urllib
import urllib3
import json
import shutil
#import urllib.request
import os

from goto import with_goto
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


with open('tmp', "wb") as file:
	response = get(url_input2)
	file.write(response.content)
print(type(file))

v_file = open('tmp', "rb")
print(type(v_file))

data = v_file.read()
v_file.close()

sha256_data = hashlib.sha256(data).hexdigest()
print('hash : '+sha256_data)

