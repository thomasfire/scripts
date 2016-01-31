#!/usr/bin/python3
#adds words to the dictionary from the stdin(console or terminal);no sorting

def getdict(somestrin):
    somestrin=somestrin.lower()
    wenk=[',', '.', ':' ,'-','!', '?', ';' , '"',')', '(','+','*','/','=','@','#','$','%','^','&','_','–','…','№','„','“','»','«']
    somestrin=somestrin.replace("ё","е")
    for x in wenk:
        somestrin=somestrin.replace(x,' ')
    somestrin=set(somestrin.split())
    return sorted(list(somestrin))


def addfrom(somestrin):
    toadd=getdict(somestrin)
    f=open(".dictionary","a")
    f.write(' '+" ".join(sorted(toadd))+' ')
    f.close()
    return "OK"

def main():
    print(addfrom(input()))


main()
