#!/usr/bin/python
#-*- coding:utf-8 -*-
#user:sys

# import requests
# import re
#
# class 糗事_Spider(object):
#
#     def qingqiu(self,page):
#         url = 'https://www.qiushibaike.com/text/page/{}/'.format(page)
#         #伪装成浏览器
#         head = {
#             'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 56.0.2924.90Safari / 537.362345Explorer / 9.6.0.18627'
#         }
#         #以下发送请求的代码
#         xiangying = requests.get(url=url,headers=head)
#         #读取响应 1.text以字符串的方式读取  2.content字节的方式读取
#         html = xiangying.content.decode('utf-8')
#         #f返回结果并且赋值
#         return html
#
#     def guolv(self,abc):
#         shuju = []
#         patt = re.compile(r'<div class="content">(.*?)</span>',re.S)
#         #将正则表达式编译
#         items = patt.findall(abc)
#         #将编译后的条件到字符串中取查找
#         for i in items:
#             i = i.replace('<span>','').replace('<br/>','').strip()
#             shuju.append(i)
#         return shuju
#     def save(self,qwe):
#         with open('a.py','a',encoding='utf-8') as f:
#             for i in qwe:
#                 f.write(i+'\n')
#
# qiu = 糗事_Spider()
# for i in range(1,8):
#     html = qiu.qingqiu(page=1)
#     shuju = qiu.guolv(abc=html)
#     qiu.save(shuju)