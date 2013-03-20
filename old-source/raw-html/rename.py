#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import string, re, glob, json, sys
from pprint import pprint


# resave json file
files = sorted(glob.glob("*.html"))
for file in files:
	print file
	
	with open (file, "r") as myfile:
		data=myfile.read()
		
		desc = data
		desc = data[desc.find('small_descr\">'):]
		desc = desc[13:desc.find('</p>')]
		#print desc
		
        yt = data
        yt = yt[yt.find('.youtube.com/embed/'):]
        yt = yt[19:30]
        #print yt
         		
        rt = data
        rt = rt[rt.find(' flashvars=\"name='):]
        rt = rt[17:rt.find('&')+1]
        print yt+" "+rt
		
		
		
	#print "\n\n\n---------\n\n\n"
	
	"""
	json_data=open(file)
	data = json.load(json_data)
	json_data.close()

	#change data object here
	data["number_in_playlist"] = str(data["number_in_playlist"])
	data["raw_audio"] = u"Бизнес-секреты/"+data["number_in_playlist"].zfill(3)+" "+data["short_title"]+".m4a"
	#end of change data object

	res = json.dumps(data, ensure_ascii=False, indent=4, separators=(',', ': '), encoding="utf-8", sort_keys=True)
	f = open(file, 'w')
	f.write(res.encode("utf-8"))
	f.close()
	
	"""

	#print filename
# end resave json file
