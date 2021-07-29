#merge socket & viroustotal CODE
# -*- coding: utf-8 -*-

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

host = "118.67.133.72"
port = 8085



def virustotal(hash_value, fn):
		api_key = '04e5988d0914ff937f7e687813e968491e5dc8203f167d62ceb6431f115db0f5'
		total_url= 'https://www.virustotal.com/vtapi/v2/file/report'
		params = {'apikey' : api_key, 'resource' : hash_value}
		#params = {'apikey' : api_key, 'resource' : 'fafaebe042ba9c59b2c3f65f43774cdb5369f838469e133a7c26e824f6d20cc6'}
		response = requests.get(total_url, params=params)
		result = response.json()

		if result.get('response_code') == 0:
			if '.apk' in str(fn):
				print('===== Send to Cuckoodroid =====')
				string6 = "가상머신에서 파일 실행중...\n"
				return string6		
			else:	
				print("==========! No Match !==========")
				string4 = "444444\n"	#바이러스토탈에서 매칭되는 값 없음
				return string4
		else:
			string5 = "555555\n"	#바이러스토탈에서 매칭되는 값 있음
			print('==========! Matched value is exist !==========')
			return string5


@with_goto
def handle_client(client_socket, addr):
	print("connected client : ",addr)
	url_from_client = client_socket.recv(1024)
	url_decode = url_from_client.decode()
	print(addr,": ",url_decode)
	
	if 'http://' not in url_decode and 'https://' not in url_decode:
		HTTP = 'http://'
		full_url = HTTP+url_decode
		print(full_url)
	else :
		full_url = url_decode

	string = "received url : %s\n"%full_url
	client_socket.sendall(string.encode())
	time.sleep(3)

	try:
		take_url = Request(full_url, headers={'User-Agent' : 'Mozilla/5.0'})
		open_url = urlopen(take_url)
	except:
		string = "invalid url error\n"
		client_socket.sendall(string.encode())
		time.sleep(2)
		goto .end

	check_body = open_url.read()
	#content_type = open_url.headers['content-type']
		
		
	if '</body>' not in str(check_body):
	
		#Check file size(unit:byte)
		size1 = open_url.headers['content-length']

		if int(size1) >= 10000000:
                	#print('!!!! Size too heavy. SORRY I cant download this file. !!!!')	
		        
			string1 = "000000\n"	#파일 다운 불가
			try :
				client_socket.sendall(string1.encode())
				time.sleep(2)
			except :
				goto .end
		else:
			string2 = "111111\n"	#파일 다운 가능
			try :
				client_socket.sendall(string2.encode())
				time.sleep(2)
			except :
				goto .end

			#다운로드 할 파일 이름 설정
			url_list = list(url_decode.split('/'))
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
				response = get(url_decode)
				file.write(response.content)

			#if __name__=="__main__":
			#	download(url_decode,"tmp.zip")

			#make hash_value & print on screen
			sha256_data = hashlib.sha256(response.content).hexdigest()

			string3 = "333333\n"
			try :
				client_socket.sendall(string3.encode())
				time.sleep(2)
			except :
				goto .end

			result = virustotal(sha256_data,file_rename)
			#cuckoodroid로 파일 보내는 코드!!
			if '가상머신' in result:
				print('쿠쿠드루이드로 보내자:-)')
			else:
				pass

			try:
				client_socket.sendall(result.encode())
				time.sleep(3)	
			except :
				goto .end
		
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
			try:
				client_socket.sendall(string.encode())
				time.sleep(3)
				print("a")
			except:
				goto .end
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

			try :
				client_socket.sendall(string1.encode())
				time.sleep(3)
				print("b")
			except:
				goto .end

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

			try:
				client_socket.sendall(string1.encode())
				time.sleep(2)
				print("c")
			except:
				pass
	
	label .end
	
	os.remove('/home/checkurl/python/'+ file_rename)

	string3 = "disconnect in 2sec\n"
	print(string3)
	try:
		client_socket.sendall(string3.encode())
		time.sleep(2)
		client_socket.close()
	except:
		client_socket.close()
	print("disconnect complete")

def new_func():
    pass
	

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
			det=0

			for x in result['scans']:
				if result['scans'][x]['detected']:
					det = det+1
					print("{0:22} : {1}".format(x,result['scans'][x]['result']))

			print("{0} engines detected this file".format(det))
'''

