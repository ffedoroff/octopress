#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import string, re, glob, json, sys
from pprint import pprint


# resave json file
files = sorted(glob.glob("*.html"))
filesmd = sorted(glob.glob("../crawled-markdown/*.markdown"))

for file in files:
    print file
    
    fmd = "";
    for filemd in filesmd:
        if filemd.find(file[0:-5]) > 0:
            fmd = filemd
            exit
    #print fmd
    data = ""
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
    rt = rt[17:rt.find('&')]
    #print yt+" "+rt
    
    #print str("../"+file[0:-5]+"")
    #with open (file[:-5], "r") as myfile:
    
    with open (fmd, "r+") as myfile:
        data=myfile.read()
        if yt: data = data.replace("date:", "youtube_id: \""+yt+"\"\ndate:")
        if rt: data = data.replace("date:", "russia_id: \""+rt+"\"\ndate:")
        data = data.replace("\"\n---", "\"\n---\n"+desc)
        myfile.seek(0)
        myfile.write(data)
        #print data
        
        
        
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
