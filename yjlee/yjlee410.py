import hashlib
import binascii
import requests
import urllib
import urllib3
import json
import shutil
#import urllib.request
import os
import zipfile

from urllib.parse import urlparse   #who is, url 나라 코드 불러오기 위한 import

from goto import with_goto
from urllib.request import Request, urlopen
from requests import get


#zip파일인경우 압축 풀기
#if 'zip' in content_type or 'vnd' in content_type:
file_zip = zipfile.ZipFile('/home/checkurl/bad.zip')
file_ext = file_zip.extractall()
print(file_ext)


file_zip_list = list(file_ext)
print(type(file_zip_list))
print(file_zip_list)

file_zip_count = len(file_zip_list)

# for i in range(0,file_zip_count):
#     etr_zip i = file_zip_list[i]
#     append



file_zip[0]

file_zip.close()#else:
#    file_rename = file_name

#result = virustotal_f(file_rename)
