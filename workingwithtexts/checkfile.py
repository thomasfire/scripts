#!/usr/bin/python3

#This script check if your text from file is correct.Python3 is needed

import sys

def getdict(somestrin):
    somestrin=somestrin.lower()
    wenk=[',', '.', ':' ,'-','!', '?', ';' , '"',')', '(','+','*','/','=','@','#','$','%','^','&','_','–','…','№','„','“','»','«']
    somestrin=somestrin.replace("ё","е")
    for x in wenk:
        somestrin=somestrin.replace(x,' ')
    somestrin=set(somestrin.split())
    return sorted(list(somestrin))

def loaddict():
    f=open(".dictionary",'r')
    st=f.read().split()
    f.close()
    return st

def checksyn(somestrins):
    dicti=loaddict()
    listmis=[]
    for x in somestrins:
        if not x in dicti:
            listmis.append(x)
    return listmis

def addfrom(somelist):
    f=open(".dictionary","a")
    f.write(' '+" ".join(somelist)+' ')
    f.close()
    return "OK"

def main():
    if len(sys.argv) <2 :
        print('usage: ./checkfile.py filename')
        sys.exit(1)
    filename=sys.argv[1]
    f=open(filename,"r")
    smstr=getdict(f.read())
    listofwrongs=checksyn(smstr)
    if listofwrongs:
        print("Incorrect words: "+"; ".join(listofwrongs)+"\n\n")
        choice=input("Do you want to add this words to the dict?(Y,N): ")
    else:
        print("OK")
        sys.exit(1)
    if choice.lower()=="y":
        print(addfrom(listofwrongs))

main()
