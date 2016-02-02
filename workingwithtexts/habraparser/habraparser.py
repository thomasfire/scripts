#!/usr/bin/python3

#this script converts *.html file of articles to text of this articles 

import sys


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
#This bad functions,they work badly

#def removeimages(somestrin):
    #while somestrin.find("<img src=")!=-1:
        #somestrin=somestrin[:somestrin.find("<img src=")]+somestrin[somestrin.find(""""alt="image">""")+len(""""alt="image">"""):]
    #while somestrin.find("<img src")!=-1:
    #    somestrin=somestrin.replace(somestrin[somestrin.find("<img src"):somestrin.find("""alt="image">""")+len("""alt="image">""")],"image")
#    return somestrin
#def removelinks(somestrin):
    #while somestrin.find("href=")!=-1:
    #    somestrin=somestrin.replace(somestrin[somestrin.find("href="):somestrin.find("""">""")+len("""">""")]," ")
#    return somestrin

def removethis(somestrin,tag):
    for x in range(len(somestrin)):
        if somestrin[x:x+len(tag)]==tag:
            i=0
            while somestrin[x+i]!=">":
                i+=1
            somestrin=somestrin.replace(somestrin[x:x+i+1]," ")
    return somestrin

def deletetrash(texthtml):
    newstr=texthtml[findtag(texthtml,"""<span class="post_title">"""):]
    newstr=newstr[:findtag(newstr,"""<div class="clear">""")]
    newstr=newstr[:findtag(newstr,"""<div class="hubs">""")]+newstr[findtag(newstr,"""<div class="content html_format">"""):]
    newstr=removetags(newstr)
    newstr=removethis(newstr,"<img src=")
    newstr=removethis(newstr,"href=")
    newstr=removethis(newstr,"class=")
    newstr=newstr.replace("<b","")


    return newstr


def main():
    if len(sys.argv)!=2:
        print("File *.html is needed to parse.")
        sys.exit(1)

    f=open(sys.argv[1],"r")
    toparse=f.read()
    f.close()
    g=open(sys.argv[1]+".parsed","w")
    g.write(deletetrash(toparse))
    g.close()
main()
