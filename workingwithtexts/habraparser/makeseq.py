#!/usr/bin/python3

#makes sequence from .keywords

import os
import re

def loadkeys():
    f=open(".keywords","r")
    res=re.findall(r":(\w+?){.*?}",f.read())
    f.close()
    return res

def getlistofarts():
    dirs=os.listdir(".")
    res=[]
    for x in dirs:
        if x.isdigit():
            res.append(x)
    return res

def checkart(num,keys):
    f=open(num+'/'+num+'.parsed','r')
    text=f.read().lower()
    for x in keys:
        if x in text:
            return True
    return False

def addtags(seq):
    f=open(".keywords","r")
    keys=f.read()
    f.close()
    res=re.findall(r":(.+?){(.*?)}",keys)
    auto=''.join(re.findall(r"::{(.*?)}",keys))
    hashtags=[]
    #hashtags.append(auto)
    for x in seq:
        g=open(x+'/'+x+'.parsed','r')
        buff=g.read()
        g.close()
        g=open(x+'/'+x+'.parsed','a')
        for y in res:
            if y[0] in buff:
                hashtags.append(y[1])
        #print(hashtags)
        g.write('\n'+' '.join(hashtags))
        g.close()

def main(resource):
    keys=loadkeys()
    arts=getlistofarts()
    g=open(resource+'.seq','r')
    nst=g.read()
    g.close()
    g=open(resource+'.posted','a')
    g.write("\n"+nst)
    g.close()
    f=open(resource+'.seq','w')
    g=open(resource+'.posted','r')
    posted=g.read().split()
    g.close()
    seq=[]
    for x in arts:
        if checkart(x,keys) and x not in posted:
            seq.append(x)
            f.write(x+'\n')
    f.close()
    addtags(seq)

if __name__ == '__main__':
    main()


def makeseq(resource):
    print("Making sequence....")
    main(resource)
