import hashlib
import binascii
import requests
import urllib
#import urllib2
import urllib3
import json
import shutil
import urllib.request
import os


#FUNCTION : zip file download
from requests import get

def download(url,file_name):
        with open(file_name, "wb") as file:
                response = get(url)
                file.write(response.content)


url_input = "https://github.com/sk3ptre/AndroidMalware_2019/raw/master/SubscriberFraud.zip"
open_url = urllib.request.urlopen(url_input)


#Check content type
content_type = open_url.headers['content-type']
print('=== CONTENT-TYPE : {} ==='.format(content_type))
#web_list = ['html','','']
#content_value = dict(url_input.headers._headers)['Content-Type'].split('/')[1].split(';')[0]

url_input.split('/')[1]

if 'html' not in content_type:
	
	#Check file size(unit:byte)
	size1 = open_url.headers['content-length']    
	print('=== CONTENT-SIZE : {} ==='.format(size1))

	if int(size1) >= 10000000:
		print('!!!! Size too heavy. SORRY I cant download this file. !!!!')
	else:
		if __name__=="__main__":
        		download(url_input,"tmp.zip")	

		#make hash_value & print on screen
		v_file = open("tmp.zip", "rb")
		data = v_file.read()
		v_file.close()
    
		md5_data = hashlib.md5(data).hexdigest()
		sha256_data = hashlib.sha256(data).hexdigest()
		sha512_data = hashlib.sha512(data).hexdigest()
		print("=============== [Show you HASH value] ===============")
		print("")
		print("Hash-Md5 : "+ md5_data)
		print("Hash-SHA256 : "+ sha256_data)
		print("Hash-SHA512 : "+ sha512_data)
		print("")

		os.remove('/home/checkurl/yjlee/tmp.zip')
     
		#send hash_value to Virustotal
		print("")
		print("=========== [Virustatal File Scan Start] ============")
		print("")
   
		api_key = '04e5988d0914ff937f7e687813e968491e5dc8203f167d62ceb6431f115db0f5'

		total_url= 'https://www.virustotal.com/vtapi/v2/file/report'
		params = {'apikey' : api_key, 'resource' : md5_data}
		#params = {'apikey' : api_key, 'resource' : 'fafaebe042ba9c59b2c3f65f43774cdb5369f838469e133a7c26e824f6d20cc6'}
		response = requests.get(total_url, params=params)
		result = response.json()

		if result.get('response_code') == 0:
			print("==========! No Match !==========")
		else:
			det=0    

			for x in result['scans']:
				if result['scans'][x]['detected']:
					det = det+1
					print("{0:22} : {1}".format(x,result['scans'][x]['result']))

			print("{0} engines detected this file".format(det))

else:
	print('!! This URL have no download file !!')
   
''' 
 
#make hash_value & print on screen
v_file = open("tmp.zip", "rb")
data = v_file.read()
v_file.close()
    
md5_data = hashlib.md5(data).hexdigest()
sha256_data = hashlib.sha256(data).hexdigest()
sha512_data = hashlib.sha512(data).hexdigest()
print("=============== [Show you HASH value] ===============")
print("")
print("Hash-Md5 : "+ md5_data)
print("Hash-SHA256 : "+ sha256_data)
print("Hash-SHA512 : "+ sha512_data)
print("")

     
#send hash_value to Virustotal
print("")
print("=========== [Virustatal File Scan Start] ============")
print("")
   
api_key = '04e5988d0914ff937f7e687813e968491e5dc8203f167d62ceb6431f115db0f5'
total_url= 'https://www.virustotal.com/vtapi/v2/file/report'
params = {'apikey' : api_key, 'resource' : md5_data}
#params = {'apikey' : api_key, 'resource' : 'fafaebe042ba9c59b2c3f65f43774cdb5369f838469e133a7c26e824f6d20cc6'}
response = requests.get(total_url, params=params)
result = response.json()

if result.get('response_code') == 0:
	print("==========! No Match !==========")

else:
	det=0    

	for x in result['scans']:
        	if result['scans'][x]['detected']:
                	det=det+1
                	print("{0:22} : {1}".format(x,result['scans'][x]['result']))
    
	print("{0} engines detected this file".format(det))
'''
