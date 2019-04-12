#!/usr/bin/python
#-*- coding:utf-8 -*-
#user:sys



# 将列表中的元素向左挪一位
# a = input('shuru:')
# a =a.split(',')
# x = a[0]
# a.pop(0)
# a.append(x)
# print(a)



# aa = int(input("请输入要转换的十进制："))
# bb = 0
# flag = 1
# st = ""
# while flag ==1:
#     cc = aa % 16
#     if cc == 10:
#        cc = "a"
#     elif cc == 11:
#         cc = "b"
#     elif cc == 12:
#         cc = "c"
#     elif cc == 13:
#         cc = "d"
#     elif cc == 14:
#         cc = "e"
#     elif cc == 15:
#         cc = "f"
#     aa = aa//16
#     if aa == 0:
#         st = str(cc)+st
#         flag = 0
#     else:
#         st = str(cc)+st
# print(st)




# f=open(r'c:\Users\haihao\Desktop\a.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         if i != j :
#             f.write('{}*{}={}\t'.format(i,j,i*j))
#         else:
#             f.write('{}*{}={}\t\n'.format(i, j, i * j))
# f.close()


# f = open('b.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         f.write('{}*{}={}\t'.format(i,j,i*j))
#     f.write("\n")
# f.close()
# print(f)


# def a():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(i,j,i*j),end='\max
#         print()


# def qwe():
#     s = sum(range(101))
#     return s*2
# print(qwe()*2)


# f = open('b.txt','r',encoding='utf-8')
# a1 = f.readlines()
# f.close()
# for i in a1:
# 	if i.startswith('#'):
# 		a1.remove(i)
# 	elif i == '\n':
# 		a1.remove(i)
# print(len(a1))


# def abc(s,y,o):
# 	print(s+1,y+1,o+1)
#
# abc(10,20,30)



# def abc(s,y):
# 	sum = 0
# 	for i in range(s,y):
# 		for j in range(2,i+1):
# 			if i%j==0:
# 				break
# 		if i==j:
# 			sum += i
# 	print(sum)
#
# abc(2,100)



# def a(s,o):
# 	for i in range(s,o):
# 		sum= 0
# 		for j in range(1,i):
# 			if i % j == 0:
# 				sum = sum + j
# 		if sum == i:
# 				print(sum)
#
# a(s=1,o=1000)

# 计算器
# def a(i,o,s):
# 	sum = 0
# 	if s == '+':
# 		sum = i+o
# 	if s == '-':
# 		sum = i-o
# 	if s == '*':
# 		sum = i*o
# 	if s == '/':
# 		sum = i/o
# 	return sum
# if __name__ == '__main__':
# 	print('hello')


# sum = lambda q=10,w=10 : print(q+w)
# sum(19,2)


# a = [i for i in range(11)]
# print(a)

# print('\n'.join(['\t'.join(['{}*{}={}'.format(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))

# def a(c=100,i=100,j=100,k=100):
#     for i in range(100):
#         for j in range(100):
#             for k in range(100):
#                 if c==i+j+k:
#                     if c==2*i+1*j+0.5*k:
#                         abc='公鸡{},母鸡{},小鸡{}'
#                         f=abc.format(i,j,k)
#                         print(f)
# a()


# def a(s,y):
# 	sum = 0
# 	for i in range(s,y+1):
# 		if i >=2:
#         	for j in range(2,i):
#         		if i%j == 0:
#         			break
#         	else:
#         		sum = sum+i
#         else:
#         	continue
# 	return sum
#


# def sum(jieguo):
# 	print(jieguo+10)
#
# jieguo = a(2,5)
# sum()




# def qqq(a):
# #     b=len(a)
# #     for i in range(b):
# #         for j in range(i + 1, b):
# #             if int(a[i]) > int(a[j]):
# #                 a[i], a[j] = a[j], a[i]
# #     return a
# # def qwe(a):
# #     c=list(set(a))
# #     return c
# # print(qqq(qwe([1,1,1,2,5,8,2,7])))
# # print(qqq(qwe([2,2,2,1,1,3,4,5])))



# import xlwt
# f = xlwt.Workbook()
# sheet = f.add_sheet('excel学习')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'{}*{}={}'.format(i,j,i*j))
#     f.save('软件测试工程师.xls')


# 写入
# with open('b.txt','r',encoding='utf-8') as b:
#     abc = b.readlines()
# import xlwt
# f = xlwt.Workbook()
# sheet = f.add_sheet('txt数据')
# for i,j in enumerate(abc):
#     j = j.replace('\n','').split(',')
#     for o in range(len(j)):
#         sheet.write(i,o,j[o])
# f.save('软件测试工程师.xls')


# import xlrd
# f = xlrd.open_workbook('软件测试工程师.xls')
# print(f.nsheets)
# sheet = f.sheets()[0]
# print(f.sheet_names())
# new_sheet = f.sheet_by_name('txt数据')
# print(sheet.nrows)
# print(sheet.row_values(1))

# 获取某一列
# f = xlrd.open_workbook('软件测试工程师.xls')
# sheet = f.sheets()[0]
# print(sheet.ncols)
# print(sheet.col_values(0))

# 获取某个单元格的内容
# f = xlrd.open_workbook('软件测试工程师.xls')
# sheet = f.sheets()[0]
# print(sheet.cell(1,0).value)


#xlutil(追加)
# import xlrd
# from xlutils.copy import copy
# f = xlrd.open_workbook('软件测试工程师.xls')
# new_f = copy(f)
# sheet = new_f.get_sheet(0)
# sheet.write(5,5,'大吴')
# sheet.write(4,4,'菲菲')
# new_f.save('软件测试工程师1.xls')


# import xlrd
# f = xlrd.open_workbook('软件测试工程师.xls')
# sheet = f.sheets()[0]
# with open('b.txt','w',encoding='utf-8') as f:
#     for i in range(sheet.nrows):
#         j = ','.join(sheet.row_values(i))
#         if j[-1] == ',':
#             j = j.split(',')
#             j.pop(-1)
#             j = ','.join(j)
#             f.write(j+'\n')
#         elif i == (sheet.nrows-1):
#             f.write(j)
#         else:
#             f.write(j+'\n')


# import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('学生表')
# c=open('a.txt','r',encoding='utf-8')
# d=open('b.txt','r',encoding='utf-8')
# m=open('c.txt','r',encoding='utf-8')
# h=d.readlines()
# x=c.readlines()
# u=m.readlines()
# ii=h+x
# mm=ii+u
# print(ii)
# for i,j in enumerate(mm):
#     j=j.replace('\n','').split(',')
#     for k in range(len(j)):
#      sheet.write(i,k,j[k])
# f.save('软件测试工程师2.xls')


# import os
# a = os.getcwd()
# print(a)
# a = os.listdir(r'e:')
# print(a)
# os.rename('day1.2','day2.py')
# a = os.path.split(r'C:/Users/haihao/Desktop/python_学习/day2.py')
# print(a)

# print(os.listdir())
# for i in os.listdir():
#     if os.path.splitext(i)[1]=='.py':
#         print(i)
# a = (i for i in os.listdir() if os.path.splitext(i)[1] == '.py')
# print(a)


# for i in range(1,10):
# # #     os.rmdir('a{}'.format(i))

# import re
# a = 'asdfghjklsertyk'
# b = re.compile('s(.*)k')
# c = b.findall(a)
# print(c)

# import re
# a = 'abcdefgasdafasd'
# b = re.compile('a.*?f')
# c =b.findall(a)
# print(c)


# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()



# import xlrd
# f = xlrd.open_workbook('软件测试工程师.xls')
# sheet = f.sheets()[0]
# shuju = []
# for i in range(sheet.nrows):
#     i = sheet.row_values(i)
#     shuju.append(i)
# with open('a.txt','w',encoding='utf-8') as f:
#     for i in shuju:
#         for j in i:
#             if j == i[-1]:
#                 f.write(j+'\n')
#             else:
#                 f.write(j+',')

# import re
# with open('c.txt','r',encoding='utf-8') as f:
#     a = f.read()
# print(a)
# patt = re.compile('a(.*)s',re.I)
# c = patt.findall(a)
# print(c)


# import re
# with open('c.txt','r',encoding='utf-8') as f:
#     a = f.read()
# print()
# c = re.sub('as','1010',a)
# print(c)



# class siri:
#     def 打电话(self):
#         print('将字符串小写变大写')
#     def 发短信(self):
#         print('将字符串分割为列表')



# class haihao:
#     def weixin(self):
#         self.tengxunshiping()
#         print('liaotian')
#     def tengxunshiping(self):
#         self.siri()
#         print('kandianshi')
#     def siri(self):
#         print('gun')
#
# class shini(haihao):
#     pass
#
# a = shini()
# a.tengxunshiping()


# class shihaihao:
#     def __init__(self,s):
#         self.lol = s
#     def yi(self):
#         print('我心{}'.format(self.lol))
#     def nong(self):
#         print('秋{}'.format(self.lol))
# a = shihaihao('难安')
# b = shihaihao('意浓')
# a.yi()
# b.nong()
#
#
# class jiujiuchengfabiao:


# import os
# for i in os.listdir():
#     if os.path.splitext(i)[1]=='.py':
#         print(i)

# c = []
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i % j ==0:
#             break
#     if i ==j:
#             c.append(i)
# for i in range(6,100,2):
#     for j in range(len(c)):
#         for m in range(j+1,len(c)):
#             if c[m]+c[j] == i:
#                 print('{}={}+{}'.format(i,c[j],c[m]))
#                 break


# def abc(x='123456', y=5, z=1  ):
#     a = list(x)
#     for i in a:
#         if i == a[y]:
#             if z == 0:
#                 print(a)
#                 break
#             else:
#                 for j in range(z):
#                     a.pop(y)
#             print(a)
#
#
# abc()



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






# import requests
# # import re
# # import xlwt
# #
# # class 豆瓣_Spider(object):
# #
# #     def qingqiu(self,page):
# #         url = 'https://movie.douban.com/top250?start={}&filter='.format(page)
# #         #伪装成浏览器
# #         head = {
# #             'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 56.0.2924.90Safari / 537.362345Explorer / 9.6.0.18627'
# #         }
# #         #以下发送请求的代码
# #         xiangying = requests.get(url=url,headers=head)
# #         #读取响应 1.text以字符串的方式读取  2.content字节的方式读取
# #         html = xiangying.content.decode('utf-8')
# #         #f返回结果并且赋值
# #         return html
# #
# #     def guolv(self,abc):
# #         shuju = []
# #         patt = re.compile(r'<span class="title">(.*?)</span>',re.S)
# #         #将正则表达式编译
# #         items = patt.findall(abc)
# #         #将编译后的条件到字符串中取查找
# #         for i in items:
# #             i = i.replace('&nbsp;','').replace('<br>','').replace('<p>','').strip()
# #             shuju.append(i)
# #             return shuju
# #     def guolv1(self,abc):
# #         shuju2 = []
# #         patt = re.compile(r'<span class="inq">(.*?)</span>',re.S)
# #         #将正则表达式编译
# #         items = patt.findall(abc)
# #         #将编译后的条件到字符串中取查找
# #         for i in items:
# #             i = i.replace('&nbsp;','').replace('<br>','').replace('<p>','').strip()
# #             shuju.append(i)
# #             return shuju2
# #
# #     def save(self,qwe):
# #         with open('c.py','a',encoding='utf-8') as f:
# #             for i in qwe:
# #                 f.write(i+'\n')
# # def t():
# #  f=xlwt.Workbook()
# #  sheet=f.add_sheet('电影')
# #  k=open('c.py','r',encoding='utf-8')
# #  s=k.readlines()
# #  print(s)
# #  for i,j in enumerate(s):
# #     j = j.replace('\n', '').split(',')
# #     for k in range(len(j)):
# #         sheet.write(i,k,j[k])
# #  f.save('电影.xls')
# #
# #
# # qiu = 豆瓣_Spider()
# # for i in range(25):
# #     html = qiu.qingqiu(page=i)
# #     shuju = qiu.guolv(abc=html)
# #     shuju2 = qiu.guolv1(abc=html)
# #     qiu.save(shuju)
# #     qiu.save(shuju2)
# # t()


#爬取图片
# import requests
# import re
# import os
#
# class tupian():
#     a = 0
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
#         for i in qwe:
#             res = requests.get('https:'+i)
#             ht=res.content
#             with open('{}.jpg'.format(self.a),'wb') as f:
#                 f.write(ht)
#             self.a+=1
#
# sss = tupian()
# for i in range(1,3):
#     sss.save(sss.guolv(sss.qingqiu(i)))


# 删除图片
# for i in range(0,50):
#     os.remove('{}.jpg'.format(i))


# from time import sleep
# import threading
# def asd():
#     for i in range(3):
#         print('玩游戏')
#         sleep(3)
# def qwe():
#     for j in range(3):
#         print('吃饭')
#         sleep(3)
# threading.Thread(target=asd).start() #.start开启线程
# threading.Thread(target=qwe).start()

import time
# #显示本地时间，以元组的类型 默认显示当前时间
# abc = time.localtime()
# print(time.strftime('%Y-%m-%d  %H:%M:%S %A'))
#
# #时间戳  从公元1970年到现在所经过的秒数
# bb = time.time()
# print(bb)

# # 按照现代化格式显示时间 格式化时间  默认显示当前时间
# #print(time.strftime('%Y-%m-%d',time.localtime(100000)))
# #根据现代化时间，格式化成元组类型
# print(time.strptime('1970-01-02','%Y-%m-%d'))
# #将元组类型的时间变成时间戳
# abb = time.strptime('2019-02-22 08:55:55','%Y-%m-%d %H:%M:%S')
# print(abb)
# print(time.mktime((2019,2,22,0,0,0,0,0,0)))
# print(time.time())

#休息
# from time import *
# sleep(2)
# print(time())

# #输入一个日期,打印是否为闰年,星期几,一年中的第几天
# a=input('输入一个日期')
# b=[]
# for i in range(4):
#     b.append(a[i])
# b=b[::-1]
# sum=0
# for z in range(len(b)):
#     for j in range(10):
#         if str(j)==b[z]:
#             sum=sum+j*10**z
# if sum%4==0:
#     print('是闰年')
# else:
#     print('不是闰年')
# t=time.strptime(a,'%Y-%m-%d')
# print('星期{},一年中的第{}天'.format(t[6]+1,t[7]))



# import paramiko
# #创建一个远程客户端
# ssh123 = paramiko.SSHClient()
# #第一次连接主机，known_hosts 存放的主机地址，跳过查找
# #  允许连接不在 known_hosts 文件中的主机
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# #链接主机
# ssh123.connect(hostname='192.168.0.86',
#                port=22,
#                username='root',
#                password='123456')
# #exec_command 执行命令  直接具有结果的命令
# # a,b,c = ssh123.exec_command('ls -al /etc')
# # 第一个变量：表示输入的命令
# # 第二个变量：表示执行的结果
# # 第三个变量： 命令的报错
# while True:
#     try:
#         a = input('>>>')
#         if a!= 'exit':
#             a,b,c=ssh123.exec_command(a)
#             print(b.read().decode())
#         else:
#             break
#     except:
#         continue
# ssh123.close()



# # 传输文件
# # 建立一个传输通道
# ssh123 = paramiko.Transport('192.168.0.86',22)
# # 连接linux
# ssh123.connect(username='root',password='123456')
# # 创建一个传输文件的对象
# sftp = paramiko.SFTPClient.from_transport(ssh123)
# # 从linux 到 windows传文件
# # 第一个参数：表示要传的文件
# # 第二个参数：表示要存放的本机位置
# sftp.get('install.log',r'.\install.log')
# ssh123.close()
# # 从windows 到 linux
# sftp.put('day1.py',r'/home/day7.py')
# ssh123.close()



# # tcp 传输 （需要建立连接）
# # socket 自带
# # socket :套接字，是实现最底层的一种通信方式  接收  发送
# # 采用的是 cs 架构
# # 通过 tcp 协议进行通信  socket
# # server端（服务器端）
# import socket
# # 创建一个套接字,规定使用tcp协议 .ip版本ipv4
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 绑定ip，端口号
# s.bind(('192.168.0.64',8888))
# # 监听服务是否开启，数字指的是最大等待数
# # netstart
# s.listen(3)
# while True:
#     #  接收请求  第一个变量：是连接信息  第二变量：客户端的ip和端口号
#     conn,addr = s.accept()
#     # 接收数据  1024表示一次性最大能接收1024字节的数据
#     reg = conn.recv(1024)
#     print(reg.decode('utf-8'))
#     # 发送数据
#     msg = input('输入:')
#     conn.send(msg.encode('utf-8'))





# # udp 传输 （不需要建立连接）
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # 绑定主机
# s.bind(('127.0.0.7',8888))
# while True:
#     # 第一个：客户端发送的数据，第二个：是客户端的ip和端口号
#     conn,addr = s.recvfrom(1024)
#     print(conn.decode('utf-8'))
#     #　发送响应
#     s.sendto('响应的数据'.encode('utf-8'),addr)



# import xlrd
# import xlwt
# f = xlwt.Workbook()
# sheet = f.add_sheet('99')
# s = open('a.txt','r',encoding='utf-8')
# a = s.readlines()
# print(a)
# for i,j in enumerate(a):
#     j=j.replace('\n','').split(',')
#     for k in range(len(a)):
#         sheet.write(i,k,j[k])
# f.save('xls')
#
#
#
# import xlrd
# import xlwt
# f = xlrd.open_workbook('99.xls')
# a = open('a.txt','w',encoding='utf-8')
# sheet = f.sheets()[0]
# for i in range(sheet.nrows):
#     s = (sheet.row_values(i))
#     s = ''.join(s)
#     a.write('{}\n'.format(s))

# 面向过程：分析解决问题所需要的步骤，然后用函数将这些问题一步步实现，最后可以依次调用
#
# 面向对象：把构成问题的事务分解成各个对象，建立对象的目的不是为了完成一个步骤，而是描叙某个事物在整个解决问题的步骤中的行为
# s = 0
# for i in range(2,100):
#     for j in range(2,i+1):
#         if i%j == 0:
#             break
#     if i == j:
#         s = s+i
#         print(s)

#
# a = input('shuru:')
# a = a.split(',')
# b = []
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(b)


# for i in range(1,1000):
#     s = 0
#     for j in range(1,i):
#         if i%j == 0:
#             s = s+j
#     if i == s:
#         print(s)






from selenium import webdriver
from time import sleep
# 定义使用什么浏览器
dr = webdriver.Chrome()
# 打开网址
dr.get('https://www.baidu.com')
# print(dr.title)   # # 获取网址的标题
# print(dr.current_url)  # # 获取打开网页的网址
sleep(2)
# dr.get('https://www.weobo.com')
# sleep(2)
# dr.back() # 回退
# dr.forward() #前进
# dr.set_window_size(500,500)  # 设置浏览器的大小
# dr.set_window_position(500,300) # 设置浏览器的位置
# dr.maximize_window() # 设置浏览器最大化
# dr.minimize_window() # 设置浏览器最小化
# dr.find_element_by_id('kw').send_keys(985435261)  # 定位 核心 1. 通过 id 属性 来定位/ 通过id是kw的来定位
# dr.find_element_by_id('su').click()
# dr.find_element_by_class_name('s_ipt').send_keys('python')  # 通过class_name  标签的class属性   来定位
# dr.find_element_by_class_name('bg s_btn').click()
# dr.find_element_by_name('wd').send_keys('微博') # name定位  标签上的name属性
# dr.find_element_by_link_text('hao123').click()# text定位   标签的文本定位
# dr.find_element_by_partial_link_text('新闻').click() # partial_link_text()定位  标签页的模糊文本定位
#dr.find_elements_by_tag_name('') # tag_name定位 ，通过标签的名称来定位     最不唯一的一个定位，通常用来定位一组数据
#dr.find_element_by_css_selector('#kw').send_keys('微博')  # css_selector定位  css来定位
#dr.find_element_by_xpath('//*[@id="kw"]').send_keys('weibo') # xpath定位，路径定位  xpath路径标记语言  xml可扩展性标记语言
# id>css>xpath>name>class_name ...
# dr.quit() # 关闭浏览器，断开连接
#close() # 关闭浏览器，不断开连接

# wd = dr.find_elements_by_class_name('mnav')   # 定位一组数据   对多个数据进行操作
# qwe = dr.find_elements_by_class_name('option')    # 层级定位遇到复杂的元素时
dr.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
sleep(2)
wd = dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_xpath('option')
for i in wd:
    i.click()
    sleep(2)


# 模拟动作
# send_keys() 输入
# click()  点击
# text    获取定位到的元素的文本
# clear() 清空定位到的元素上面的数据