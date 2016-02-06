#!/usr/bin/python3

#this script parses links to the articles

import sys
import urllib
import urllib.request
import re
import os
import shutil

def extractlinks(texthtml):
    a=re.compile(r"""<a class="button habracut" href="(https://.*?)#habracut">""",re.DOTALL)
    listoflinks=re.findall(a,texthtml)
    return listoflinks

def main():
    if len(sys.argv)!=2:
        print("URL is needed to parse.")
        sys.exit(1)
    f=urllib.request.urlopen(sys.argv[1])
    toparse=str(f.read(),encoding='utf8')
    f.close()
    links=extractlinks(toparse)
    a=re.compile(r"""https://(\w+?).ru""")
    source=" ".join(list(re.findall(a,sys.argv[1])))
    g=open(source+".links","w")
    g.write("\n".join(links))
    g.close()

main()
