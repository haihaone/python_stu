#!/usr/bin/python
#-*- coding:utf-8 -*-
#user:sys

# import requests
# import re
#
# class 完美_Ss(object):
#
#     def qingqiu(self,yeshu):
#         url = 'https://www.32us.com/html/0/90/977{}.html'.format(yeshu)
#         head = {
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.6.0.18627'
#         }
#         xiangying = requests.get(url=url,headers=head)
#         duqu = xiangying.content.decode('gbk')
#         return duqu
#
#     def guolv(self,abc):
#         shuju = []
#         ooo = re.compile(r'<dd id="contents">(.*?)</dd>',re.S)
#         items = ooo.findall(abc)
#         for i in items:
#             i = i.replace('&nbsp;','').replace('<br />','').strip()
#             shuju.append(i)
#         return shuju
#     def save(self,qwe):
#         with open('o.py','a',encoding='utf-8') as f:
#             for i in qwe:
#                 f.write(i+'\n')
#
#
# qiu = 完美_Ss()
# for i in range(7,9):
#     duqu = qiu.qingqiu(i)
#     shuju = qiu.guolv(duqu)
#     qiu.save(shuju)






#爬取图片
# import requests
# import re
# import os
#
# class tupian():
#     def qingqiu(self, page):
#         url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
#         #伪装成浏览器
#         head = {
#             'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 56.0.2924.90Safari / 537.362345Explorer / 9.6.0.18627'
#         }
#         xiangying = requests.get(url=url,headers=head)
#         html = xiangying.content.decode('utf-8')
#         return html
#
#     def guolv(self,abc):
#         shuju = []
#         #  过滤的是图片的网址
#         ab = re.compile(r'<div class="thumb">(.*?)</a>',re.S)
#         item = ab.findall(abc)
#         for j in item:
#             patt = re.compile('src="(.*?)"',re.S)
#             hhh = patt.findall(j)
#             shuju.append(hhh[0])
#         return shuju
#
#     def save(self,qwe):
#         # 任何图片都是 二进制
#         # 请求图片的网址，得到图片的源码
#         for k,i in enumerate(qwe):
#             res = requests.get('https:'+i)
#             ht=res.content
#             with open('{}.jpg'.format(k),'wb') as f:
#                 f.write(ht)
#
# sss = tupian()
# html = sss.qingqiu(1)
# shuju = sss.guolv(html)
# sss.save(shuju)