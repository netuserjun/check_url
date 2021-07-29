import urllib.request
import json
 
ip = '8.8.8.8'
whois_key = '2021070217171054876809'
 
query = "http://whois.kisa.or.kr/openapi/whois.jsp?query=" + ip + "&key="+ whois_key + "&answer=json";
request = urllib.request.urlopen(query).read().decode("utf-8")

jsonObject = json.loads(request)

print(jsonObject.get("whois").get("countryCode"))


