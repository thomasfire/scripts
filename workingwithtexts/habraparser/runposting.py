#!/usr/bin/python3
import vkupload as vup
import habraparser as hper
import parsehabrlinks as phlinks
import makeseq as mkseq
import time
import random


def main():
    f=open('vk.settings','r')
    resource=f.read().split()[0]
    f.close()
    links=open(resource+".links",'r').read().split()
    while True:
    #    try:
    #        phlinks.parselinks(resource)
    #    except:
    #        print("Somethings wrong,maybe it's bad connection\n")
        try:
            for x in links:
                hper.parsearts(x)
        except:
            print("Somethings wrong,maybe it's bad connection\n")
        mkseq.makeseq(resource)
        vup.startuploading(resource)
        sltime=3600 + random.randint(1,3600)
        print("Sleeping for ",sltime)
        time.sleep(sltime)
        print("\n")

if __name__=="__main__":
    main()
