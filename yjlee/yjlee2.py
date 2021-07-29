import hashlib
import binascii
import requests
import urllib
#import urllib2
import urllib3
import json
import shutil
#import urllib.request
from urllib.request import Request, urlopen
#from bs4 import BeautifulSoup
import os

# move to web page
url_input10 = 'https://madplay.github.io/post/python-urllib'

# move to web page
url_input11 = 'http://ylh6.nkmos.fit/'

# move to web page
url_input12 = 'https://juyoung-1008.tistory.com/4'

url_input13 = 'https://github.com/datacharmer/test_db'


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

#open_url1 = urllib.request.urlopen(url_input1)
#open_url2 = urllib.request.urlopen(url_input3)
#open_url3 = Request(url_input1, headers={'User-Agent' : 'Mozilla/5.0'})
#open_url4 = Request(url_input4, headers={'User-Agent' : 'Mozilla/5.0'})
#open_url10 = urllib.request.urlopen(url_input10)
#open_url11 = urllib.request.urlopen(url_input11)
#open_url12 = urllib.request.urlopen(url_input12)

#url = "https://www.naver.com"
#open_url = urllib.request.urlopen(url_input3)
take_url = Request(url_input1, headers={'User-Agent' : 'Mozilla/5.0'})
open_url = urlopen(take_url)
HTML = open_url.read()
#print(HTML)
#dict(HTML)
#print(type(HTML))

content_type = open_url.headers['content-type']
print(content_type)
apk_file = 'vnd.andriod.package-archive'
if apk_file in content_type:
	old_name = 'tmp'
	new_name = 'tmp.apk'
	file_rename = os.rename(old_name, new_name)
	print(file_rename)

#decoding = HTML.decode()
#print(decoding)
#href_value = HTML.find('a href')
#print(href_value)

if '</body>' not in str(HTML):
	print('No Body')
else:
	print('Body is exist')

#print("HEADER => {}".format(open_url.headers.__dict__))

'''
all1 = open_url1.body
all2 = open_url2.headers.__dict__
all3 = urlopen(open_url3).headers.__dict__
all4 = urlopen(open_url4).headers.__dict__
all10 = open_url10.headers.__dict__
#all11 = open_url11.headers.__dict__
all12 = open_url12.headers.__dict__


other1 = open_url1.headers['ETag']
other2 = open_url2.headers['ETag']
other3 = urlopen(open_url3).headers['ETag']
other4 = urlopen(open_url4).headers['ETag']
other10 = open_url10.headers['ETag']
#type11 = open_url11.headers['ETag']
other12 = open_url12.headers['ETag']
'''

'''
print(' ')
print('ZIP.files body : {}'.format(all1))
print(' ')
print('APK.files header : {}'.format(all2))
print(' ')
print('APK.files(Sogeeting) header : {}'.format(all3))
print(' ')
print('APK.files(Game-360m) header : {}'.format(all4))
print(' ')
print('------------------------------------------------------------------')
print(' ')
print('MOVE to Wb-Page header : {}'.format(all10))
print(' ')
#print('MOVE to Wb-Page header : {}'.format(all11))
#print(' ')
print('MOVE to Wb-Page header : {}'.format(all12))
print(' ')


print('=======================================================================')


print(' ')
print('ZIP.files header : {}'.format(other1))
print(' ')
print('APK.files header : {}'.format(other2))
print(' ')
print('APK.files(Sogeeting) header : {}'.format(other3))
print(' ')
print('APK.files(Game-360m) header : {}'.format(other4))
print(' ')
print('------------------------------------------------------------------')
print(' ')
print('MOVE to Wb-Page header : {}'.format(other10))
print(' ')
#print('MOVE to Wb-Page header : {}'.format(other11))
#print(' ')
print('MOVE to Wb-Page header : {}'.format(other12))
print(' ')
'''




'''
for i, url in enumerate([open_url1, open_url2, open_url3, open_url4, open_url5]):
	print("Download_all {} => {} ".format(i+1, dict(url.headers._headers.__dict))


for j, url in enumerate([open_url1, open_url2, open_url3, open_url4, open_url5]):
	print("Download_all {} => {} ".format(j+1, dict(url.headers._headers)['Content-Type']))



for k, url in enumerate([open_url_, open_url2, open_url3, open_url4, open_url5]):
	print("url_other {} => {} ".format(k+1, dict(url.headers.__dict__)))
'''


'''
#Check content type4
print('')
type4 = open_url4.headers['content-type']
print('4. Content-type ==>> {}'.format(type4))
print('')
all_4 = open_url4.headers.__dict__
print('4. All-header ==>> {}'.format(all_4))
print('')
# print('DOWNLOAD FILE ==>> {}'.format(all_3))

#Check content type5
print('')
type5 = open_url5.headers['content-type']
print('5. Content-type ==>> {}'.format(type5))
print('')
all_5 = open_url5.headers.__dict__
print('5. All-header ==>> {}'.format(all_5))
'''



'''#Check content type1
type1 = open_url_.headers['content-type']
#all_1 = open_url_.headers.__dict__
print('DOWNLOAD FILE ==>> {}'.format(type1))

#Check content type3
type3 = open_url3.headers['content-type']
#all_3 = open_url3.headers.__dict__
print('MOVE TO WEB PAGE ==>> {}'.format(type3))
'''


#print('=== CONTENT-TYPE : {} ==='.format(type1))


'''
if 'html' not in type1:
	#Check content size
	size1 = open_url3.headers['content-length']
	print('=== CONTENT-SIZE : {} ==='.format(size1))

else :
	print('I want to go HOME...')
'''

#Check content encoding method
#method1 = open_url_.headers['content-encoding']
#print('=== CONTENT-ENCODING : {} ==='.format(method1))









''' md5_data= hashlib.md5(data).hexdigest()
    sha256_data = hashlib.sha256(data).hexdigest()
    sha512_data = hashlib.sha512(data).hexdigest()
api_key = '04e5988d0914ff937f7e687813e968491e5dc8203f167d62ceb6431f115db0f5'
'''


'''
#3 Hash_value

result = []
hashs = [md5_data, sha256_data, sha512_data]

for i in range(len(hashs)):
	params = {'apikey' : api_key, 'resource' : hashs[i]}
	response = requests.get(total_url, params=params)
	result.append(response.json())
'''
