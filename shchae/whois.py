import urllib.request
import json

from urllib.parse import urlparse
import socket

url = 'https://www.google.com'
o = urlparse(url)
hostname = o.hostname

port = o.port or (443 if o.scheme == 'https' else 80)

ip = socket.getaddrinfo(hostname, port)[0][4][0]

# ip = '8.8.8.8'
whois_key = '2021070217171054876809'

query = "http://whois.kisa.or.kr/openapi/whois.jsp?query=" + ip + "&key="+ whois_key + "&answer=json";
request = urllib.request.urlopen(query).read().decode("utf-8")

jsonObtions = json.load(request.read())
print(jsonObtions.get("whois").get("countryCode"))
