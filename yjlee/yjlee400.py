### 다운로드 되어있는 파일 -> 바이러스토탈 해시값 비교 -> 매칭값 없으면 파일 보내기 ###
### 테스트 파일 : bad.zip , bad2.zip


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


def virustotal_h(hash_value, fn):
        api_key = '04e5988d0914ff937f7e687813e968491e5dc8203f167d62ceb6431f115db0f5'
        total_url= 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey' : api_key, 'resource' : hash_value}
        #params = {'apikey' : api_key, 'resource' : 'fafaebe042ba9c59b2c3f65f43774cdb5369f838469e133a7c26e824f6d20cc6'}
        response = requests.get(total_url, params=params)
        result = response.json()

        if result.get('response_code') == 0:
                string4 = "444444\n"	#바이러스토탈에서 매칭되는 값 없음
                print("==========! No Match Hash-value !==========")
                return string4
        else:
                string5 = "555555\n"	#바이러스토탈에서 매칭되는 값 있음
                print('==========! Matched Hash-value is exist !==========')

def virustotal_f(fn):
        api_key = '04e5988d0914ff937f7e687813e968491e5dc8203f167d62ceb6431f115db0f5'
        
        #바이러스토탈 파일스캔 주소
        scan_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        url_scan_params = {'apikey' : api_key}
        
        #바이러스 의심 파일 설정
        file = fn
        files = {'file' : (file, open(file, 'rb'))}

        #바이러스토탈 파일 스캔 시작
        response_scan = requests.post(scan_url, files=files, params=url_scan_params)
        result_scan = response_scan.json()
        scan_resource = result_scan['resource']

        #바이러스토탈 파일 스캔 결과 주소
        report_url= 'https://www.virustotal.com/vtapi/v2/file/report'
        url_report_params = {'apikey' : api_key, 'resource' : scan_resource}

        #바이러스토탈 파일 스캔 결과 리포트 조회
        response_report = requests.get(report_url, params = url_report_params)
        report = response_report.json()
        print('REPORT : '+ str(report))

        #바이러스토탈에서 결과 값 조회 루프
        while report.get('response_code') == -2:
            print('==========! Your resource is queued for analysis !=========')
            response_report = requests.get(report_url, params = url_report_params)
            report = response_report.json()
            #report_scan_data = report.get('scan_data')
                
            if report.get('response_code') != -2:
                break
                
            time.sleep(5)

        if report.get('response_code') == 0:
            string4 = "444444\n"	#바이러스토탈에서 매칭되는 값 없음
            print("==========! No Match File-Data !==========")
            return string4
        else:
            string5 = "555555\n"	#바이러스토탈에서 매칭되는 값 있음
            print('==========! Matched File-Data is exist !==========')
            return string5

file_name = 'bad2.zip'

with open(file_name, "rb") as file:
    data = file.read()

sha256_data = hashlib.sha256(data).hexdigest()

result = virustotal_h(sha256_data,file_name)

#VirusTotal로 파일 보내는 코드!!
if result == '444444\n':
    string8 = '바이러스토탈에서 파일 돌리는 중.. \n'
    #client_socket.sendall(string8.encode())
    time.sleep(2)                               

    print('=======! Send FILE to VirusTotal !=======')
    result2 = virustotal_f(file_name)
    if result2 == '666666\n':
        string6 = '바이러스토탈_파일_매칭값 없음\n'
        #client_socket.sendall(string6.encode())
        time.sleep(2)
    else:
        string7 = '바이러스토탈_파일_매칭값 있음\n'
        #client_socket.sendall(string7.encode())
        time.sleep(2)
else:
    pass


'''
                        det=0

                        for x in result['scans']:
                                if result['scans'][x]['detected']:
                                        det = det+1
                                        print("{0:22} : {1}".format(x,result['scans'][x]['result']))

                        print("{0} engines detected this file".format(det))
'''   
















# # ZIP file download
# url_input1 = "https://github.com/sk3ptre/AndroidMalware_2019/raw/master/SubscriberFraud.zip"

# # APK file download
# url_input2 = 'https://bit.ly/3yhmX6s'

# # Move to WEB-page & APK file download(ZouenSogeting)
# url_input3 = 'https://bit.ly/3xmCZfj'

# # Move to WEB-page & APK file download(Game-360M)
# url_input4 = 'https://bit.ly/3hmftti'

# # Move to WEB-page & file download
# url_input5 = 'https://www.softonic.kr/download/putty/windows/post-download'

# #file download
# url_input6 = 'https://drive.google.com/uc?export=download&id=1U0zlzuklVKird6UZ3H4vO-2Vt6hPEwB-'

# take_url = Request(url_input1, headers={'User-Agent' : 'Mozilla/5.0'})
# open_url = urlopen(take_url)
# content_type = open_url.headers['content-type']
# print(content_type)


# #다운로드 할 파일 이름 설정
# url_list = list(url_input1.split('/'))
# url_len = len(url_list)
# url_name_num = int(url_len) - 1

# url_last = url_list[url_name_num]

# file_name = url_last[0:3]

# #파일 다운로드하기
# with open(file_name, "wb") as file:
#     response = get(url_input1)
#     file.write(response.content)


# #zip파일인경우 압축 풀기
# if 'zip' in content_type or 'vnd' in content_type:
#     file_name_zip = zipfile.ZipFile('/home/checkurl/'+ file_name)
#     file_name_zip.extractall()
#     file_name_zip.close()

#     file_rename = file_name_zip
# else:
#     file_rename = file_name

# result = virustotal_f(file_rename)

# print(result)