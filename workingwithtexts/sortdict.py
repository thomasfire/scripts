#!/usr/bin/python3
#Sorts and optimizes dictionary
f=open(".dictionary",'r')
st=set(f.read().split())
f.close()
f=open(".dictionary",'w')
f.write(" ".join(sorted(list(st))))
f.close()
print("OK")
