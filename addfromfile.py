#!/usr/bin/python3
#Adds new words to the dictionary from text file
import sys

def sortdict():
    f=open(".dictionary",'r')
    st=set(f.read().split())
    f.close()
    f=open(".dictionary",'w')
    f.write(" ".join(sorted(list(st))))
    f.close()
    return True

def getdict(filename):
    f=open(filename,'r')
    somestrin=f.read().lower()
    wenk=[',', '.', ':' ,'-','!', '?', ';' , '"',')', '(','+','*','/','=','@','#','$','%','^','&','_','–','…','№','„','“','»','«','[',']']
    for x in wenk:
        somestrin=somestrin.replace(x,' ')
    somestrin=set(somestrin.split())
    f.close()
    return sorted(list(somestrin))

def addfrom(file):
    toadd=getdict(file)
    f=open(".dictionary","a")
    f.write(" ".join(sorted(toadd)))
    f.close()


def main():
    if len(sys.argv) <2 :
        print('usage: ./addfromfile.py filename {|--nosort}')
        sys.exit(1)
    filename=sys.argv[1]
    addfrom(filename)
    if len(sys.argv) == 2 or sys.argv[2]!="--nosort":
        isok=sortdict()
    if isok:
        print("OK")

main()
