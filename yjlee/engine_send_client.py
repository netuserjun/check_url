## version0.6.1.py참고
## 바이러스토탈에서 악성으로 판별된 해시값
## 결과 엔진과 바이러스 종류 클라이언트로 보내기..


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

from urllib.parse import urlparse   #who is, url 나라 코드 불러오기 위한 import

from goto import with_goto
from urllib.request import Request, urlopen
from requests import get
from pysafebrowsing import SafeBrowsing

host = "118.67.133.72"
port = 8085


@with_goto
def handle_client(client_socket, addr):
	print("connected client : ",addr)
	url_from_client = client_socket.recv(1024)
	url_decode = url_from_client.decode()
	print(addr,": ",url_decode)
	



	api_key = '04e5988d0914ff937f7e687813e968491e5dc8203f167d62ceb6431f115db0f5'
	total_url= 'https://www.virustotal.com/vtapi/v2/file/report'
	#params = {'apikey' : api_key, 'resource' : hash_value}
	params = {'apikey' : api_key, 'resource' : 'c5ca6aa73fdcb523b5e63b52197f134f229792046cbac525d46985ad72880395'}
	#params = {'apikey' : api_key, 'resource' : 'fafaebe042ba9c59b2c3f65f43774cdb5369f838469e133a7c26e824f6d20cc6'}
	#time.sleep(5)
	response = requests.get(total_url, params=params)
	result = response.json()

	scans_items = result.get('scans').items()
	scans_detected_value = list(scans_items)[0][1]['detected']      # 바이러스토탈에서 매칭되는 값 있음 -> 디텍트 값 True / False
	print(scans_detected_value)

	if result.get('response_code') == 0:
		string4 = "444444\n"	#바이러스토탈에서 매칭되는 값 없음
		print("==========! No Match Hash-value !==========")

	else:
		if str(scans_detected_value) == 'False':
			string9 = "999999\n"     #바이러스토탈에서 매칭되는 디텍트 값 False
			print('==========! Engine Undetected Hash-value !==========')

			det=0
			print("{} engines detected this file".format(det))


		else:
			string5 = "555555\n"	#바이러스토탈에서 매칭되는 디텍트 값 True
			print('==========! Engine Detected Hash-value !==========')

			det=0
			engine_name = []
			#str_engine_name = str(engine_name)
			virus_type = []
			#str_virus_type = str(virus_type)

			for x in result['scans']:
				#if result['scans'][x]['detected'] == '':
				if str(result['scans'][x]['detected']) == 'True':
					det = det+1
					print("{0:22} : {1}".format(x,result['scans'][x]['result']))

					engine_name.append(x)
					virus_type.append(result['scans'][x]['result'])

			print("{} engines detected this file".format(det))

			print('')
			print(engine_name)
			print(virus_type)

			string = "바이러스 검출됨'^'\n"
			client_socket.sendall(string.encode())
			client_socket.sendall(engine_name.encode())
			time.sleep(2) 

			string3 = "disconnect in 2sec\n"
			print(string3)
			try:
				client_socket.sendall(string3.encode())
				time.sleep(2)
				client_socket.close()
			except:
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