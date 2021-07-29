from pysafebrowsing import SafeBrowsing
 = SafeBrowsing("AIzaSyBbIvD8610q2R044Z5_Dy0MzDMEr9n_ajI")
                url_name = url_decode
                r = s.lookup_urls([url_name])
# print(r[url_name]['malicious'])
# print(r[url_name]['threats'])
                if r[url_name]['malicious'] == False :
                        string = "알려진 위협이 존재하지않는 URL입니다.\n"

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
                                string1 = "Platform에대한 위협이 하나 이상 존재합니다\n"
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
