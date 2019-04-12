#!/usr/bin/python
#-*- coding:utf-8 -*-
#user:sys

# f=open('q.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         f.write('{}*{}={}\t'.format(i,j,i*j))
#     f.write('\n')



# import pymysql
# conn = pymysql.connect(host = '192.168.0.115',
#                        port = 56151,
#                        user = 'root',
#                        password = '123456',
#                        charset = 'utf8')
#创建游标(控制器)
# abc = conn.cursor()
#执行sql语句
# while True:
#     try:
#         a = input('>>>')
#         if a!= 'exit':
#                 abc.execute(a)
#                 print(abc.fetchall())
#         else:
#             break
#     except:
#         continue
# conn.close()
# # abc.execute('show databases;')
# # abc.execute('create database haihao7;')
# abc.execute('use haihao;')
# # abc.execute('create table hai(name char(20),age int,sex char (10));')
# abc.execute('show tables;')
# abc.execute('insert into hai values("xiaowang",20,"nan"),("li",21,"nv");')
# abc.execute('select*from hai;')
# #任何结果都需要有容器来接收
# print(abc.fetchall())#接收上一个sql语句的结果



# import json
# a = {'name':123}
# #将字典变成json数据
# json_data = json.dumps(a)
# print(json_data)
# #将json数据变成字典
# abc = json.loads(json_data)
# print(abc['name'])


class doutu:
    def xiangying(self,x):
        url = 'https://www.doutula.com/article/list/?page={}'.format(x)
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
        }
        xiangying=requests.get(url=url,headers=head)
        fenxi=xiangying.content.decode('UTF-8')
        return fenxi
    def pipei(self,x):
        wjm=[]
        klb=[]
        wenjian=[]
        nr=self.xiangying(x)
        b=re.compile(r'</div> <div class="col-sm-9">(.*?)<div class="text-center">',re.S)
        d=b.findall(nr)
        for k in d:
            aa = re.compile(r'<div class="list-group-item random_list">.*?</div>',re.S)
            wj = aa.findall(k)
            for i in wj:
                k = k.replace(i,'')
            wjm.append(k)
        for i in wjm:
            zz=re.compile(r'<a href="(.*?)" class=',re.S)
            wz=zz.findall(i)
            klb.append(wz)
        for i in wjm:
            wjm = re.compile(r'<div class="random_title">(.*?)<div class="date">',re.S)
            mz = wjm.findall(i)
            wenjian.append(mz)
        return klb[0],wenjian[0]
    def xieru(self,x):
        lb=[]
        tiaojian=self.pipei(x)
        for i in tiaojian[0]:
            head = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
            }
            xy=requests.get(url=i,headers=head)
            jx=xy.content.decode('utf-8')
            tj=re.compile(r"this.src='(.*?)'",re.S)
            tp=tj.findall(jx)
            lb.append(tp)
        for j in tiaojian[1]:
            os.mkdir(r'C:\Users\zk\Desktop\python学习\{}'.format(j))
        for i in range(len(lb)):
            for m,k in enumerate(lb[i]):
                os.chdir(r'C:\Users\zk\Desktop\python学习\{}'.format(tiaojian[1][i]))
                head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
                xy = requests.get(url=k, headers=head)
                erjinzhi=xy.content
                if '.jpg' in k:
                    with open('{}.jpg'.format(m),'wb') as f:
                        f.write(erjinzhi)
                elif '.gif' in k:
                    with open('{}.gif'.format(m),'wb') as f:
                        f.write(erjinzhi)




import requests
import re
import os
class dou(object):
    def fasong(self,page):
        url = 'https://www.doutula.com/article/list/?page={}.format(page)'
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        xiang = requests.get(url, headers=head)
        html = xiang.content.decode('utf-8')
        return html

    def guolv(self,abc):
        patt = re.compile(r'</div> <div class="col-sm-9">(.*?)<div class="text-center">',re.S)
        items = patt.findall(abc)

        zutu=[]
        for i in items:
            pat = re.compile(r'href="(.*?)" class')
            ite = pat.findall(i)
            zutu.append(ite)
        zu=zutu[0]

        mingzi=[]
        for j in items:
            pa = re.compile(r'<div class="random_title">(.*?)<div class="date">')
            it = pa.findall(j)
            mingzi.append(it)
        ming=mingzi[0]

        dantu=[]
        for q in zutu[0]:
            head = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
            }
            xiang = requests.get(q, headers=head)
            html = xiang.content.decode('utf-8')
            p = re.compile(r"this.src='(.*?)'")
            t = p.findall(html)
            dantu.append(t)

        for e in ming:
            os.mkdir(r'D:\python文件\.idea\{}'.format(e))

        for p,r in enumerate(dantu):
            os.chdir(r'D:\python文件\.idea\{}'.format(ming[p]))
            for o in r:
                res=requests.get(o)
                ht=res.content
                if '.gif' in o:
                    with open('{}.gif'.format(p),'wb') as f:
                        f.write(ht)
                        p+=1
                else:
                    with open('{}.jpg'.format(p),'wb') as f:
                        f.write(ht)
                        p+=1
a=dou()
b=a.fasong(1)
a.guolv(b)