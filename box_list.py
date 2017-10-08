# -*- coding: utf-8 -*-
#encoding=utf-8

import urllib
import urllib2
import json

num = 1;
page_num = 1000;
url = 'https://www.vulbox.com/json/getCompanyInfoByName'
response = None;

while num < page_num:
	try:
		values = {"startDate":"2014-01-01","endDate":"2020-01-01","page": str(num),"search":""}
		fromData = urllib.urlencode(values)
		request = urllib2.Request(url,fromData)
		response = urllib2.urlopen(request);

		data = response.read();
		# dataDecode = data.decode();
		resJson = json.loads(data, encoding="utf-8")
		info = resJson['data']['info']
		# 成功返回success，失败返回error
		if resJson['status'] != 'success':
			break

		# 循环数据写入文件
		for key in info:
			file = open('list.txt','a+')
			content = key['bus_name'] + '----' + key['bus_trade'] + '-----' + key['bus_url'] + '\n'
			file.write(content.encode('gbk'))
			file.close(); 

		num = num + 1

	except urllib2.URLError as e:
		if hasattr(e, 'code'):
			print 'Error code:',e.code
		elif hasattr(e, 'reason'):
			print 'Reason:',e.reason
	finally:
		if response:
			response.close()
	
