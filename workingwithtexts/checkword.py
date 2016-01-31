#!/usr/bin/python3

#This script check if your text from stdin is correct.Python3 is needed

def getdict(somestrin):
    somestrin=somestrin.lower()
    wenk=[',', '.', ':' ,'-','!', '?', ';' , '"',')', '(','+','*','/','=','@','#','$','%','^','&','_','–','…','№','„','“','»','«']
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
    for x in somestrins:
        if not x in dicti:
            return "Incorrect text"
    return "It`s correct text"

def main():
    stin=getdict(input())
    print(checksyn(stin))


main()