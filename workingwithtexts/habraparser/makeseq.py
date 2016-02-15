#!/usr/bin/python3

#makes sequence from .keywords

import os

def loadkeys():
    f=open(".keywords","r")
    return f.read().split()

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
    for x in arts:
        if checkart(x,keys) and x not in posted:
            f.write(x+'\n')
    f.close()

if __name__ == '__main__':
    main()


def makeseq(resource):
    print("Making sequence....")
    main(resource)
