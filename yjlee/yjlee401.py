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



def virustotal_h(hash_value):
    api_key = '04e5988d0914ff937f7e687813e968491e5dc8203f167d62ceb6431f115db0f5'
    total_url= 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey' : api_key, 'resource' : hash_value}
            #params = {'apikey' : api_key, 'resource' : 'c5ca6aa73fdcb523b5e63b52197f134f229792046cbac525d46985ad72880395'}
            #params = {'apikey' : api_key, 'resource' : 'fafaebe042ba9c59b2c3f65f43774cdb5369f838469e133a7c26e824f6d20cc6'}
    time.sleep(5)
    response = requests.get(total_url, params=params)
    result = response.json()
        #str_result = str(result)
        #print(str_result)

    scans_items = result.get('scans').items()
    scans_detected_value = list(scans_items)[0][1]['detected']      # 바이러스토탈에서 매칭되는 값 있음 -> 디텍트 값 True / False
    print(scans_detected_value)



    if result.get('response_code') == 0:
        string4 = "444444\n"	#바이러스토탈에서 매칭되는 값 없음
        print("==========! No Match Hash-value !==========")
        return string4
    else:
        if str(scans_detected_value) == 'False':
            string9 = "999999\n"     #바이러스토탈에서 매칭되는 디텍트 값 False
            print('==========! Engine Undetected Hash-value !==========')

            det=0
            print("{} engines detected this file".format(det))
            return string9

        else:
            string5 = "555555\n"	#바이러스토탈에서 매칭되는 디텍트 값 True
            print('==========! Engine Detected Hash-value !==========')

            list_x = []
            list_result = []
            det=0

            for x in result['scans']:
            #if result['scans'][x]['detected'] == '':
                if str(result['scans'][x]['detected']) == 'True':
                    det = det+1
                    print("{0:22} : {1}".format(x,result['scans'][x]['result']))

                    list_x.append(x)
                    list_result.append(result['scans'][x]['result'])

                    print("{} engines detected this file".format(det))

                    string_x = str(list_x)
                    string_result = str(list_result)

                    return string_x, string_result

file_name = 'test_test'
result0,result1 = virustotal_h('c5ca6aa73fdcb523b5e63b52197f134f229792046cbac525d46985ad72880395')

print(type(result0))
print(type(result1))