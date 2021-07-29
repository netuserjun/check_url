#merge socket & viroustotal CODE
# -*- coding: utf-8 -*-  => version0.3에서 가져옴
# 다운로드되는 파일 이름 설정(.apk 붙이기)
# 파일 다운로드 동작 코드 단축
# Whois api 추가 
# virustotal함수에 cuckoodroid로 넘어가는 스트링 추가   -> 제거
# Virustotal에 매칭되는 해시값 없는 경우, Virustotal에 파일 넘기기
# Virustotal에 매칭되는 해시값 있는 경우, 디텍트 엔진 출력


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



def virustotal_h(hash_value):
        api_key = '04e5988d0914ff937f7e687813e968491e5dc8203f167d62ceb6431f115db0f5'
        total_url= 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey' : api_key, 'resource' : hash_value}
        #params = {'apikey' : api_key, 'resource' : 'c5ca6aa73fdcb523b5e63b52197f134f229792046cbac525d46985ad72880395'}
        #params = {'apikey' : api_key, 'resource' : 'fafaebe042ba9c59b2c3f65f43774cdb5369f838469e133a7c26e824f6d20cc6'}

        response = requests.get(total_url, params=params)
        result = response.json()
        #str_result = str(result)
        #print('RESULT : '+ str(result))

        if result.get('response_code') == 0:
                string4 = "444444\n"	#바이러스토탈에서 매칭되는 값 없음
                print("==========! No Match Hash-value !==========")
                return string4,0
        else:
                scans_items = result.get('scans').items()
                scans_detected_value = list(scans_items)[0][1]['detected']      # 바이러스토탈에서 매칭되는 값 있음 -> 디텍트 값 True / False
                print(scans_detected_value)

                if str(scans_detected_value) == 'False':
                        string9 = "999999\n"     #바이러스토탈에서 매칭되는 디텍트 값 False
                        print('==========! Engine Undetected Hash-value !==========')
                        
                        det=0
                        print("{} engines detected this file".format(det))
                        return string9,0

                else:
                        #바이러스토탈에서 매칭되는 디텍트 값 True
                        print('==========! Engine Detected Hash-value !==========')

                        list_x = ['V_name']
                        list_result = ['M_type']
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

        time.sleep(5)

        #바이러스토탈 파일 스캔 결과 리포트 조회
        response_report = requests.get(report_url, params = url_report_params)
        report = response_report.json()
        #print('REPORT : '+ str(report))

        #바이러스토탈에서 파일 스캔 결과 값 조회 루프
        while report.get('response_code') == -2:
                print('==========! Your resource is queued for analysis !=========')
                # time.sleep(1)
                response_report = requests.get(report_url, params = url_report_params)
                
                try:
                        report = response_report.json()
                        #report_scan_data = report.get('scan_data')
                except:
                        pass

                if report.get('response_code') != -2:
                        break
                
                time.sleep(5)

        if report.get('response_code') == 0:
                string1 = "666666\n"  #바이러스토탈에서 파일 조회 -> 매칭되는 값 없음
                print("==========! No Match File-Data !==========")
                return string1,0
        else:
                #바이러스토탈에서 파일 조회 -> 매칭되는 값 있음
                print('==========! Matched File-Data is exist !==========')

                list_x = ['V_name']
                list_result = ['M_type']
                det=0

                for x in report['scans']:
                        #if result['scans'][x]['detected'] == '':
                        if str(report['scans'][x]['detected']) == 'True':
                                det = det+1
                                print("{0:22} : {1}".format(x,report['scans'][x]['result']))

                                list_x.append(x)
                                list_result.append(report['scans'][x]['result'])

                print("{} engines detected this file".format(det))

                string_x = str(list_x)
                string_result = str(list_result)

                return string_x, string_result

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

        try:
                take_url = Request(full_url, headers={'User-Agent' : 'Mozilla/5.0'})
                open_url = urlopen(take_url)
        except:
                print('==! invalid url error !==')
                string = "invalid url error\n"
                client_socket.sendall(string.encode())
                goto .end

        check_body = open_url.read()
        #content_type = open_url.headers['content-type']


        if '</body>' not in str(check_body) or 'downloader' in str(check_body):

                #Check file size(unit:byte)
                size1 = open_url.headers['content-length']

                if int(size1) >= 10000000:
                        #print('!!!! Size too heavy. SORRY I cant download this file. !!!!')	

                        string1 = "000000\n"	#파일 다운 불가
                        try :
                                client_socket.sendall(string1.encode())
                        except :
                                goto .end
                else:
                        string2 = "111111\n"	#파일 다운 가능
                        try :
                                client_socket.sendall(string2.encode())
                        except :
                                goto .end

                        #다운로드 할 파일 이름 설정
                        url_list = list(url_decode.split('/'))
                        url_len = len(url_list)
                        url_name_num = int(url_len) - 1

                        url_last = url_list[url_name_num]

                        file_name = url_last[0:3]

                        # #apk파일에 확장자 붙이기
                        # content_type = open_url.headers['content-type']
                        # apk_file = 'vnd.android.package-archive'

                        # if apk_file in content_type:
                        #         file_rename = file_name + '.apk'
                        # else:
                        #         file_rename = file_name

            #파일 다운로드하기
                        with open(file_name, "wb") as file:
                                response = get(url_decode)
                                file.write(response.content)

            #if __name__=="__main__":
            #	download(url_decode,"tmp.zip")

                        #make hash_value
                        sha256_data = hashlib.sha256(response.content).hexdigest()
                        time.sleep(2)

                        string3 = "333333\n"
                        try :
                                client_socket.sendall(string3.encode())
                        except :
                                goto .end

                        result0, result1 = virustotal_h(sha256_data)

                        #print(result0)
                        #print(result1)

                        #VirusTotal로 파일 보내는 코드!!
                        if result0 == '444444\n' or result0 == '999999\n':
                                string8 = '바이러스토탈에서 파일 돌리는 중.. \n'
                                client_socket.sendall(string8.encode())                               

                                print('======! Send FILE to VirusTotal !======')
                                result2, result3 = virustotal_f(file_name)

                                if result2 == '666666\n':
                                        string6 = '바이러스토탈_파일_바이러스_미검출~\n'
                                        client_socket.sendall(string6.encode())
                                else:
                                        string7 = '바이러스토탈_파일_바이러스_검출!\n'
                                        string_x = result2 + '\n'
                                        string_result = result3 + '\n'

                                        client_socket.sendall(string_x.encode())
                                        time.sleep(0.5)
                                        client_socket.sendall(string_result.encode())
                                        time.sleep(0.5)
                                        client_socket.sendall(string7.encode())
                        else:
                                string = "바이러스토탈_해시값_Detected!\n"
                                string_x = result0 + '\n'
                                string_result = result1 + '\n'

                                client_socket.sendall(string_x.encode())
                                time.sleep(0.5)
                                client_socket.sendall(string_result.encode())
                                time.sleep(0.5)
                                client_socket.sendall(string.encode())

                        try:
                                string = 'Bye-bye\n'
                                client_socket.sendall(string.encode())
                                time.sleep(0.5)	
                        except :
                                goto .end

                        if len(str(file_name)) == 3:
                                path = '/home/checkurl/'        #/home/checkurl/python/
                                os.remove(path + file_name)
                        else:
                                pass
		
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
                        string2 = "알 수 없음\n"

                        # url = 'https://www.facebook.com'
                        o = urlparse(full_url)
                        hostname = o.hostname

                        port = o.port or (443 if o.scheme == 'https' else 80)

                        ip = socket.getaddrinfo(hostname, port)[0][4][0]
                        print(ip)
                        # ip = '8.8.8.8'
                        whois_key = '2021070217171054876809'

                        query = "http://whois.kisa.or.kr/openapi/whois.jsp?query=" + ip + "&key="+ whois_key + "&answer=json";
                        request = urllib.request.urlopen(query).read().decode("utf-8")


                        # jsonObject = json.loads(request)
                        # print(jsonObject)
                        # print(jsonObject.get(“whois").get("countryCode"))

                        try:
                                jsonObject = json.loads(request)
                                countryCode=jsonObject.get("whois").get("countryCode")
                                countryCode = countryCode + "\n"
                                client_socket.sendall(string.encode())
                                time.sleep(2)
                                client_socket.sendall(countryCode.encode())
                                time.sleep(3)
                                print(jsonObject.get("whois").get("countryCode"))
                        except:
                                #jsonObject=None
                                client_socket.sendall(string.encode())
                                time.sleep(2)
                                client_socket.sendall(string2.encode())
                                time.sleep(2)
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


        # file_list = os.listdir(path)
        # if '.apk' in str(file_list):
        #         os.remove(path + file_rename)
        #         print('=== Success to file remove ===')
        # else:
        #         print('=== No file for remove ===')

        string3 = "disconnect_in_1sec\n"
        print(string3)     
        try:
                client_socket.sendall(string3.encode())
                time.sleep(0.5)
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

