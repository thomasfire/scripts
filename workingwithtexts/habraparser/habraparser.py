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

def videolink(texthtml):
    a=re.compile(r"""<iframe.*?src="(.+?)".*?>.*?</iframe>""",re.DOTALL)
    b=re.compile(r"""(<iframe.*?src=".+?".*?>.*?</iframe>)""",re.DOTALL)
    listoftags=re.findall(b,texthtml)
    listoflinks=re.findall(a,texthtml)
    for x in range(len(listoftags)):
    #    print(listoftags[x],listoflinks[x])
        texthtml=texthtml.replace(listoftags[x],listoflinks[x])
    return texthtml


def delpoll(text):
    a=re.compile(r"""(<div class="polling">.*</div>)""",re.DOTALL)
    #print(re.findall(a,text))
    for x in re.findall(a,text):
        text=text.replace(x,'')
    #text=re.sub(a,'',text)
    #print(text)
    return text

def deletetrash(texthtml,num):
    newstr=texthtml[findtag(texthtml,"""<span class="post_title">"""):]
    newstr=delpoll(newstr)
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
    newstr=videolink(newstr)
    newstr=re.sub(r'\v+', '', newstr)
    newstr=re.sub(r'\t+', '', newstr)
    newstr=re.sub(r'\f+', '', newstr)
    newstr=re.sub(r'\r+', '\n', newstr)
    newstr=re.sub(r'\n+', '\n', newstr)
    #newstr=re.sub(r"^\n+|\r+|\t+$", '\n', newstr)

    return newstr

def formatext(lines):
    x=0
    while x<len(lines):
        #print(x,len(lines))
        if lines[x].isspace():
            i=0
            while lines[x+i].isspace() and x+i<len(lines)-1:
                i+=1
            if i>0:
                del lines[x:i]
            if x+1==len(lines):
                break
        x+=1
    return "".join(lines)

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

def main(resource):

    f=urllib.request.urlopen(resource)
    toparse=str(f.read(),encoding='utf8')
    a=re.compile(r"""/(\d+?)/""")
    num=" ".join(list(re.findall(a,resource)))
    f.close()
    g=open(num+".parsed","w")
    g.write(deletetrash(toparse,num))
    g.close()
    g=open(num+".parsed","r")
    lines=list(g.readlines())
    #print(lines)
    g.close()
    g=open(num+".parsed","w")
    g.write(formatext(lines))
    g.close()
    download_images(num)
    shutil.move(num+".parsed", num+'/'+num+".parsed")
    shutil.move(num+".images", num+'/'+num+".images")
    shutil.move(num+".links", num+'/'+num+".links")

if __name__=="__main__":
    main(sys.argv[1])

def parsearts(resource):

    main(resource)
