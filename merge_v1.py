#merge socket & viroustotal CODE


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
import urllib.request
import os


##SOD=lKET code##


host = "15.164.127.0"
port = 8085

def handle_client(client_socket, addr):
	print("connected client : ",addr)
	url_from_client = client_socket.recv(1024)
	print(addr,": ",url_from_client.decode())
	string = "received url : %s\n"%url_from_client.decode()
	client_socket.sendall(string.encode())
	time.sleep(3)

	content_type = url_from_client.headers['content-type']

	if 'html' not in content_type:
	
		#Check file size(unit:byte)
		size1 = open_url.headers['content-length']

		if int(size1) >= 10000000:
                	#print('!!!! Size too heavy. SORRY I cant download this file. !!!!')	
		        
			string1 = "000000\n"
			client_socket.sendall(string1.encode())
			time.sleep(3)
		else:
			string2 = "111111\n"
			client_socket.sendall(string2.encode())
			time.sleep(3)

			if __name__=="__main__":
				download(url_from_client,"tmp.zip")

			#make hash_value & print on screen
			v_file = open("tmp.zip", "rb")
			data = v_file.read()
			v_file.close()

			sha256_data = hashlib.sha256(data).hexdigest()

			os.remove('/home/checkurl/yjlee/tmp.zip')

			result = virustotal(sha256_data)
			client_socket.sendall(result.encode())
			time.sleep(3)	


'''
        string2 = "222222\n"
        client_socket.sendall(string2.encode())
        print("send 2 to client")
        #user = client_socket.recv(1024)
        #print(addr,":",user.decode())
        time.sleep(3)
'''

	else:
		print('Have no download file')

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




##VIROUSTOTAL API code##

#FUNCTION : zip file download
from requests import get

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
		string4 = "444444"
		return string3
	else:
		string5 = "555555"	
		return string4
                       

			'''	
			det=0

                        for x in result['scans']:
                                if result['scans'][x]['detected']:
                                        det = det+1
                                        print("{0:22} : {1}".format(x,result['scans'][x]['result']))

                        print("{0} engines detected this file".format(det))
			'''

