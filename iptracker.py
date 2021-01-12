#Author:iFanpS
#Credit:Thx to GuckTubeYT
import os
import urllib.request as urllib2
import json

while True:
	print('[+] ==================')
	ip = input('Put ur target: ')
	os.system('cls')
	url = "http://ip-api.com/json/"
	konz = urllib2.urlopen(url + ip)
	data = konz.read()
	irfan = json.loads(data)

	print("IP: " + irfan['query'])
	print("City: " + irfan['city'])
	print("Status: " + irfan['region'])
	print("ISP: " + irfan['isp'])
	print("TimeZone: " + irfan['timezone'])
	print('[+] ==================')

	break
