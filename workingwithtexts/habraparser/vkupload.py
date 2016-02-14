#!/usr/bin/python3
# -*- coding: utf-8 -*-
import vk_api
import os
import shutil
import sys
import re


def getimages(listoffiles):
    images=[".jpg","jpeg",".gif","png"]
    res=[]
    for x in listoffiles:
        for y in images:
            if y in x.lower():
                res.append(x)
    return res

def main():
    vset=open("vk.settings","r")
    settings=vset.read()
    vset.close()
    login="".join(re.findall(r"login=(.+)#endlogin",settings))
    password="".join(re.findall(r"password=(.+)#endpass",settings))
    group="".join(re.findall(r"grouptosend=(\d+)#endgroupid",settings))

    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    upload = vk_api.VkUpload(vk_session)
    seqfile=open(sys.argv[1]+".seq","r")
    seq=seqfile.read().split()

    vk = vk_session.get_api()


    for x in seq:
        listofatt=[]
        for y in getimages(os.listdir(x)):
            vkpost=upload.photo_wall(x+'/'+y,group_id=group)
            #dic[x].append({'media_id':vkpost['id'],'owner_id':vkpost['owner_id']})
            listofatt.append('photo'+str(vkpost[0]['owner_id'])+'_'+str(vkpost[0]['id']))
        f=open(x+"/"+x+".parsed","r")
        mes=f.read()
        f.close()
        posting=vk.wall.post(owner_id=-int(group),message=mes,attachments=','.join(listofatt))


if __name__ == '__main__':
    main()