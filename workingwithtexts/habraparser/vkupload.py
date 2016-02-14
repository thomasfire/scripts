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
    #login, password = 'login', 'pass'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    upload = vk_api.VkUpload(vk_session)
    seqfile=open(sys.argv[1]+".seq","r")
    seq=seqfile.read().split()
    #dic={}
    vk = vk_session.get_api()
    #vkpost=vk.wall.post(owner_id=-int(group),message="Тестим тестим",attachments='photo96744416_402657769')
    for x in seq:
        #dic[x]=[]
        listofatt=[]
        for y in getimages(os.listdir(x)):
            vkpost=upload.photo_wall(x+'/'+y,group_id=group)
            #dic[x].append({'media_id':vkpost['id'],'owner_id':vkpost['owner_id']})
            listofatt.append('photo'+str(vkpost[0]['owner_id'])+'_'+str(vkpost[0]['id']))
        f=open(x+"/"+x+".parsed","r")
        mes=f.read()
        f.close()
        posting=vk.wall.post(owner_id=-int(group),message=mes,attachments=','.join(listofatt))
    #vkpost=upload.photo_wall('cat.png',message="Тестим тестим",group_id="54681902")
    #vkpost2=upload.photo_wall('cat.png',message="Тестим тестим",group_id="29831327")
    #with vk_api.VkRequestsPool(vk_session) as pool:
    #    vkpost=pool.method('wall.post',{'owner_id':'-54681902','message':u"Тестим тестим",'attachments':'photo96744416_402657769'})

    #print(vkpost)
    #print(vkpost2)
if __name__ == '__main__':
    main()
