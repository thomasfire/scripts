#!/usr/bin/python3

#this script gets article from URL

import sys
import urllib
import urllib.request
import re
import os
import shutil

def findtag(texthtml,tag):
    return texthtml.find(tag)

def removetags(somestrin):
    fg=open(".listoftags","r")
    tags=fg.read().split()
    fg.close()
    for x in tags:
        somestrin=somestrin.replace(x," ")
    somestrin=somestrin.replace("<br>","\n")
    return somestrin

def removethis(somestrin,tag):
    for x in range(len(somestrin)):
        if somestrin[x:x+len(tag)]==tag:
            i=0
            while somestrin[x+i]!=">":
                i+=1
            somestrin=somestrin.replace(somestrin[x:x+i+1]," ")
    return somestrin

def findimg(texthtml):
    a=re.compile(r"""<img.*?src="(.+?)".*?>""", re.DOTALL)
    listofimg=re.findall(a,texthtml)
    return listofimg

def deletetrash(texthtml,num):
    newstr=texthtml[findtag(texthtml,"""<span class="post_title">"""):]
    newstr=newstr[:findtag(newstr,"""<div class="clear">""")]
    newstr=newstr[:findtag(newstr,"""<div class="hubs">""")]+newstr[findtag(newstr,"""<div class="content html_format">"""):]
    newstr=removetags(newstr)
    newstr=removethis(newstr,"class=")
    newstr=newstr.replace("<b","")

    listofimg=findimg(newstr)
    a=re.compile(r"""<img.*?src=".+?".*?>""", re.DOTALL)
    newstr=re.sub(a," ",newstr)

    b=re.compile(r"""href="(.*?)">""", re.DOTALL)
    listoflinks=re.findall(b,newstr)
    newstr=re.sub(b," ",newstr)

    f=open(num+".images","w")
    f.write("\n".join(listofimg))
    f.close()

    g=open(num+".links","w")
    g.write("\n".join(listoflinks))
    g.close()
    #newstr=re.sub(r'\s+', ' ', newstr)
    newstr=re.sub(r'\t+', '\n', newstr)
    newstr=re.sub(r'\r+', '\n', newstr)
    newstr=re.sub(r'\n+', '\n', newstr)
    re.sub("^\s+|\n|\r|\s+$", '', newstr)
    return newstr

def download_images(num):
    f=open(num+".images","r")
    img_urls=f.read().split()
    if not os.path.exists(num):
        os.mkdir(num)
    for x in img_urls:
        st=" ".join(list(re.findall(r"\w+?/(\w+?\.\w{3})",x)))
        if not st:
            continue
        urllib.request.urlretrieve(x, num+"/"+st)

def main():
    if len(sys.argv)!=2:
        print("URL is needed to parse.")
        sys.exit(1)

    f=urllib.request.urlopen(sys.argv[1])
    toparse=str(f.read(),encoding='utf8')
    a=re.compile(r"""/(\d+?)/""")
    num=" ".join(list(re.findall(a,sys.argv[1])))
    f.close()
    g=open(num+".parsed","w")
    g.write(deletetrash(toparse,num))
    g.close()
    download_images(num)
    shutil.move(num+".parsed", num+'/'+num+".parsed")
    shutil.move(num+".images", num+'/'+num+".images")
    shutil.move(num+".links", num+'/'+num+".links")
    
if __name__=="__main__":
    main()
