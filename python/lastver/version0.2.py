# merge socket & viroustotal CODE
# 2021-07-08. Add "http://" string in front of [inputted URL from Andriod]


import socket
import threading
import time
import argparse

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
from pysafebrowsing import SafeBrowsing
##SOD=lKET code##


host = "15.164.127.0"
port = 8085



def virustotal(hash_value):
        api_key = '04e5988d0914ff937f7e687813e968491e5dc8203f167d62ceb6431f115db0f5'
        total_url= 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey' : api_key, 'resource' : hash_value}
        #params = {'apikey' : api_key, 'resource' : 'fafaebe042ba9c59b2c3f65f43774cdb5369f838469e133a7c26e824f6d20cc6'}
        response = requests.get(total_url, params=params)
        result = response.json()

        if result.get('response_code') == 0:
                print("==========! No Match !==========")
                string4 = "444444\n"
                return string4
        else:
                string5 = "555555\n"
                print('=========!! This is an unsafe URL :-) !!=========')
                return string5


@with_goto
def handle_client(client_socket, addr):
	print("connected client : ",addr)
	url_from_client = client_socket.recv(1024)
	url_decode = url_from_client.decode()
	print(addr,": ",url_decode)
	
	# 입력받은 URL 앞에 "http://"문자열 추가
	if 'http://' not in url_decode and 'https://' not in url_decode:
		HTTP = 'http://'
		full_url = HTTP + url_decode
		print(full_url)
	else:
		full_url = url_decode
		print(full_url)


	string = "received url : %s\n"%full_url
	client_socket.sendall(string.encode())
	time.sleep(3)


	try:
		take_url = Request(full_url, headers={'User-Agent' : 'Mozilla/5.0'})
		open_url = urlopen(take_url)
		#content_type = open_url.headers['content-type']
	except:
		string100 = "100\n"
		client_socket.sendall(string100.encode())
		print('=====!!! Warning : Invalid URL !!!=====')
		goto .end
	

	check_body = open_url.read()

	if '</body>' not in str(check_body):
	
		#Check file size(unit:byte)
		size1 = open_url.headers['content-length']

		if int(size1) >= 10000000:
                	#print('!!!! Size too heavy. SORRY I cant download this file. !!!!')	
		        
			string1 = "000000\n"
			client_socket.sendall(string1.encode())
			time.sleep(2)
		else:
			string2 = "111111\n"
			client_socket.sendall(string2.encode())
			time.sleep(2)

			#download zip-file
			with open('tmp.zip', "wb") as file:
				response = get(url_decode)
				file.write(response.content)

			
			#if __name__=="__main__":
			#	download(url_decode,"tmp.zip")

			#make hash_value & print on screen
			v_file = open("tmp.zip", "rb")
			data = v_file.read()
			v_file.close()

			sha256_data = hashlib.sha256(data).hexdigest()

			os.remove('/home/checkurl/python/tmp.zip')

			string3 = "333333\n"
			client_socket.sendall(string3.encode())
			time.sleep(2)

			result = virustotal(sha256_data)
			client_socket.sendall(result.encode())
			time.sleep(3)	

	else:
		print('==! Have no download file !==')

		s = SafeBrowsing("AIzaSyBbIvD8610q2R044Z5_Dy0MzDMEr9n_ajI")
		#url_name = "http://malware.testing.google.test/testing/malware/"
		url_name = url_decode
		r = s.lookup_urls([url_name])
# print(r[url_name]['malicious'])
# print(r[url_name]['threats'])
		if r[url_name]['malicious'] == False : 
			string = "알려진 위협이 존재하지 않는 URL입니다.\n" 

			client_socket.sendall(string.encode())
			time.sleep(3)
			print("a")
		else :
			string1 = "a"

			if r[url_name]['platforms']  == ['PLATFORM_TYPE_UNSPECIFIED'] :
				string1 = "알 수 없는 플랫폼에 대한 위협\n"
			elif r[url_name]['platforms'] == ['WINDOWS'] :
				string1 = "window에 대한 위협\n" 
			elif r[url_name]['platforms'] == ['LINUX'] :
				string1 = "리눅스 대한 위협\n" 
			elif r[url_name]['platforms'] == ['ANDROID'] :
				string1 = "안드로이드에 대한 위협\n"  
			elif r[url_name]['platforms'] == ['OSX'] :
				string1 = "OS X에 대한 위협\n"  
			elif r[url_name]['platforms'] == ['IOS'] :
				string1 = "iOS에 대한 위협\n"  
			elif r[url_name]['platforms'] == ['ANY_PLATFORM'] :
				string1 = "Platform에 대한 위협이 하나 이상 존재합니다\n" 
			elif r[url_name]['platforms'] == ['ALL_PLATFORMS'] :
				string1 = "모든 Platform에 대한 위협이 있습니다\n"
			elif r[url_name]['platforms'] == ['CHROME'] :
				string1 = "Chrome에 대한 위협이 있습니다\n" 

			client_socket.sendall(string1.encode())
			time.sleep(3)
			print("b")

			if r[url_name]['threats'] ==  'THREAT_TYPE_UNSPECIFIED' :
				string1 = "알 수 없는 위협 유형\n"
			elif r[url_name]['threats'] == ['MALWARE']:
				string1 = "위협 유형 : 악성코드\n"
			elif r[url_name]['threats'] == ['SOCIAL_ENGINEERING'] :
				string1 = "위협 유형 : 사회 공학\n"  
			elif r[url_name]['threats'] == ['UNWANTED_SOFTWARE'] :
				string1 = "위협 유형 : 원치 않는 소프트웨어\n"
			elif r[url_name]['threats'] == ['POTENTIALLY_HARMFUL_APPLICATION'] :
				string1 = "위협 유형 : 잠재적으로 유해한 응용 프로그램\n"


			client_socket.sendall(string1.encode())
			time.sleep(2)
			print("c")



	'''
        string2 = "222222\n"
        client_socket.sendall(string2.encode())
        print("send 2 to client")
        #user = client_socket.recv(1024)
        #print(addr,":",user.decode())
        time.sleep(3)
	'''

	label .end

	string3 = "disconnect in 2sec\n"
	print(string3)
	client_socket.sendall(string3.encode())
	time.sleep(2)
	client_socket.close()
	print("disconnect complete")


	
	

def accept_func():
	global server_socket
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind(('',port))
	server_socket.listen(5)

	while 1:
		try:
			client_socket, addr = server_socket.accept()

		except KeyboardInterrupt:
			server_socket.close()
			print("Keybord interrupt")

		print("client handler thread")
		t = threading.Thread(target = handle_client, args=(client_socket,addr))
		t.deamon = True
		t.start()

if __name__=='__main__':
	parser = argparse.ArgumentParser(description = "\n this is server \n -p port\n")
	parser.add_argument('-p', help="port")

	args = parser.parse_args()
	try:
		port = int(args.p)
	except:
		pass
	accept_func()




'''
##VIROUSTOTAL API code##

#FUNCTION : zip file download

def download(url,file_name):
	with open(file_name, "wb") as file:
		response = get(url)
		file.write(response.content)

def virustotal(hash_value):
	api_key = '04e5988d0914ff937f7e687813e968491e5dc8203f167d62ceb6431f115db0f5'
	total_url= 'https://www.virustotal.com/vtapi/v2/file/report'
	params = {'apikey' : api_key, 'resource' : sha256_data}
	#params = {'apikey' : api_key, 'resource' : 'fafaebe042ba9c59b2c3f65f43774cdb5369f838469e133a7c26e824f6d20cc6'}
	response = requests.get(total_url, params=params)
	result = response.json()

	if result.get('response_code') == 0:
		print("==========! No Match !==========")
		string4 = "444444\n"
		return string4
	else:
		string5 = "555555\n"	
		print(':-)')
		return string5


			det=0

			for x in result['scans']:
				if result['scans'][x]['detected']:
					det = det+1
					print("{0:22} : {1}".format(x,result['scans'][x]['result']))

			print("{0} engines detected this file".format(det))
'''

