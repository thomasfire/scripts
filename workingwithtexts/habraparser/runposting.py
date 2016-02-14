#!/usr/bin/python3
import vkupload as vup
import habraparser as hper
import parsehabrlinks as phlinks
import time
import random


def main():
    f=open('vk.settings','r')
    resource=f.read().split()[0]
    f.close()
    links=open(resource+".links",'r').read().split()
    while True:
        phlinks.parselinks(resource)
        for x in links:
            hper.parsearts(x)
        vup.startuploading(resource)
        sltime=3600 + random.randint(1,3600)
        print("Sleeping for ",sltime)
        time.sleep(sltime)
        print("\n")

if __name__=="__main__":
    main()
