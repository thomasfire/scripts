#!/usr/bin/python3
import vkupload as vup
import habraparser as hper
import parsehabrlinks as phlinks
import makeseq as mkseq
import shutil
import time
import random
import os


def main():
    f=open('vk.settings','r')
    resource=f.read().split()[0]
    f.close()
    links=open(resource+".links",'r').read().split()
    while True:
        #deleting trash
        print("Deleteing old files....")
        dirs=os.listdir(".")
        for x in dirs:
            if x.isdigit():
                shutil.rmtree(x)

        try:
            phlinks.parselinks(resource)
        except:
            print("Somethings wrong,maybe it's bad connection\n")
            print("Retrying in 30 srconds...")
            time.sleep(30)
            continue
        try:
            for x in links:
                hper.parsearts(x)
        except:
            print("Somethings wrong,maybe it's bad connection\n")
            print("Retrying in 30 seconds...")
            time.sleep(30)
            continue
        mkseq.makeseq(resource)
        vup.startuploading(resource)
        sltime=3600 + random.randint(1,3600)
        print("Sleeping for ",sltime)
        time.sleep(sltime)



        print("\n")

if __name__=="__main__":
    main()
