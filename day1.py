# !/usr/bin/python
# -*- coding:utf-8 -*-
# a=input('请输入成绩:')
# a=float(a)
# if a>90:
# 	print('优秀')
# elif 80<a<=90:
# 	print('良好')
# elif 70<a<=80:
# 	print('一般')
# elif 60<a<=70:
# 	print('渣渣')


# !/usr/bin/python
# -*- coding:utf-8 -*-
# a=input('请手动输入字符串：')
# if a.startswith('a') and a.endswith('c'):
# 	print('hello')
# else:
# 	print(123)


# !/usr/bin/python
# -*- coding:utf-8 -*-
# a=input('请输入:')
# if a.startswith('a') and a.endswith('c'):
# 	print('hello world')
# else:
# 	if a.startswith('a'):
# 		print('hello')
# 	elif a.endswith('c'):
# 		print('world')
# 	else:
# 		print(123)



# a=['abc','Abc','sab']
# for i in a:
# 	if i.startswith('a') or i.startswith('A'):
# 		if i.endswith('c'):
# 			print(i)


# !/usr/bin/python
# -*- coding:utf-8 -*-
# import random
# b = random.randint(1,10)
# for i in range(0,3):
# 	a = input('请输入内容:')
# 	a = int(a)
# 	if  a>b:
# 		print('大了')
# 	elif a<b:
# 		print('小了')
# 	elif a==b:
# 		print('喝')
# 		break
# else:
# 	print('庄家喝')
# 从1-10随机选中一个数，复制给a



# !/usr/bin/python
# -*- coding:utf-8 -*-
# a = int(input("请输入第一条边:"))
# b = int(input("请输入第二条边:"))
# c = int(input("请输入第三条边:"))
# if (a+b>c) and (a+c>b) and (b+c>a):
# 	if a==b==c:
# 		print("等边三角形")
# 	elif (a==b or a==c or b==c):
# 		print("等腰三角形")
# 	elif (a*a+b*b==c*c) or (a*a+b*b==c*c) or (a*a+b*b==c*c):
# 		print("直角三角形")
# 	else:
# 		print("不规则三角形")
# else:
# 	print("不是三角形")


# !/usr/bin/python
# -*- coding:utf-8 -*-
# abc = input('请输入三个数字，以逗号隔开:')
# abc = abc.split(',')
# abc = [int(abc[0]),int(abc[1]),int(abc[2])]
# abc.sort()
# if abc[0]+abc[1]>abc[2]:
# 	if abc[0]**2+abc[1]**2==abc[-1]**2:
# 		print('直角')
# 	elif abc[0]**2+abc[1]**2>abc[-1]**2:
# 		print('锐角')
# 	else:
# 		print('钝角')
# else:
# 	print('不是三角形')



# !/usr/bin/python
# -*- coding:utf-8 -*-
# for i in range(100,1000):
# 	a=i//100
# 	b=(i%100)//10
# 	c=(i%100)%10
#     if a**3+b**3+c**3==i:
#     	print(i)



# 1-2+3-4+5....-98+99
# !/usr/bin/python
# -*- coding:utf-8 -*-
# abc=0
# for i in range(1,100):
# 	if i%2==0:
# 		abc = abc - i
# 	else:
# 		abc = abc + i
# print(abc)



# 99乘法表
# !/usr/bin/python
# -*- coding:utf-8 -*-
# for i in range(1,10):
# 	print()
# 	for j in range(1,i+1):
# 		a = '{}*{}={}'
# 		print(a.format(i,j,i*j),end='\t')



# !/usr/bin/python
# -*- coding:utf-8 -*-
# a=input('请输入一字符串:')
# for i in range(len(a)//2):
# 	if a[i]!=a[-i-1]:
# 		print('不是回文字符串')
# 		break
# else:
# 	print('是回文字符串')



# !/usr/bin/python
# -*- coding:utf-8 -*-
# a = ['猫','狗','龙猫','兔']
# for i,j in enumerate(a):
# 	print(i+1,j)
# while True:
# 	b = int(input('请输入需要购买的动物:'))
# 	if b=='exit':
# 		break
# 	else:
# 		print(a[b-1])

# 从一加到100的和
# !/usr/bin/python
# -*- coding:utf-8 -*-
# a = 0
# for i in range(1,101):
# 	a = a + i
# print(a)

# !/usr/bin/python
# -*- coding:utf-8 -*-
# count = 0
# c = 0
# while count < 100:
#     count = count + 1
#     c = c + count
# print(c)




# !/usr/bin/python
# -*- coding:utf-8 -*-
# while True:
# 	b = input('请输入成绩：')
# 	if len(b) != 2:
# 		a = b.split(',')
# 		sum = 0
# 		for i in a:
# 			sum +=int(i)
# 		print('平均数为:',sum / len(a))
# 		for j in a:
# 			if int(j) <= splitum / len(a):
# 				print('低于平均分的分数',j)



# 冒泡排序法：
# !/usr/bin/python
# -*- coding:utf-8 -*-
# a = input('请输入一组数:')
# c = a.split(',')
# b = len(c)
# for i in range(b-1):
# 	for j in range(b-1):
# 		if int(c[j]) > int(c[j+1]):
# 			c[j],c[j+1] = c[j+1],c[j]
# print(c)



# 选择排序法
# !/usr/bin/python
# -*- coding:utf-8 -*-
# a = input('请输入一组数:')
# c = a.split(',')
# b = len(c)
# for i in range(b-1):
# 	for j in range(i+1,b):
# 		if int(c[i]) > int(c[j]):
# 			c[i],c[j] = c[j],c[i]
# print(c)




# 去重
# a=input('请输入一字符串:')
# a=a.split(',')
# b = []
# for i in range(len(a)):
# 	if a[i] not in b:
# 		b.append(a[i])
# print(b)



# 100元钱买鸡，公鸡2块，母鸡1块，小鸡五毛，问：怎样买100只鸡，又刚好把钱花完
# for i in range(50):
# 	for j in range(40):
# 		a= 100-i-j
# 		if (a % 0.5 == 0) and (i*2+j*1+a*0.5 == 100):
# 			print('公鸡:{} 母鸡:{} 小鸡:{}'.format(i,j,a))

# a=100
# for i in range(100):
#     for j in range(100):
#         for k in range(100):
#             if a==i+j+k:
#              if a==2*i+1*j+0.5*k:
#                 abc='公鸡{},母鸡{},小鸡{}'
#                 f=abc.format(i,j,k)
#                 print(f)



# 质数之和
# sum = 0
# for i in range(2,100):
# 	for j in range(2,i+1):
# 		if i % j == 0:
# 			break
# 	if i==j:
# 		sum = sum+i
# 		print(m)

# sum = 0
# for i in range(2,100):
# 	for j in range(2,i):
# 		if i%j == 0:
# 			break
# 	else:
# 		sum += i
# print(sum)



# 去重
# a = input('shuru:')
# a = a.split(',')
# b=[]
# for i in range(len(a)):
# 	if a[i] not in b:
# 		b.append(a[i])
# print(b)



# 阶乘
# a = input('shuru:')
# a = int(a)
# sum = 0
# b = 1
# for i in range(1,a+1):
# 	b = b * i
# 	sum = sum + b
# print(sum)



# 打印列表中所有第一大和第二大的数
# a = [1,2,3,4,5,6,7,8,9]
# b = a.copy()
# b = list(set(b))
# b.sort()
# for i in a:
# 	if i == b[-1] or i == b[-2]:
# 		print(i)



# 1000以内，因数之和。
# for i in range(1,1000):
# 	s = 0
# 	for j in range(1,i):
# 		if i % j == 0:
# 			s = s + j
# 	if i == s:
# 		print(s)

	
# for i in range(1,1000):
# 	s = []
# 	for j in range(1,i):
# 		if i % j == 0:
# 			s.append(j)
# 	if sum(s) == i:
# 		print(i)
# 		print(s)
		


# a = [
#    ('椒麻鸡',500),
#    ('炸带鱼',1000),
#    ('红烧肉',300),
#    ('可乐鸡翅',10600),
#    ('汉堡',3152),
#     ('咖啡',12000),
# ]
# z = []#购物车
# b = input("请输入资产:")
# b = int(b)
# while True:
#         for i,j in enumerate(a):
#             print(i,j)#打印商品列表
#         x= input("选择商品>>>:")
#         if x.isdigit():#判断用户输入是否为数字
#             x = int(x)
#             if x < len(a) and x >=0:#判断用户输入的商品编号是否在下标范围之内，len()-取列表下标长度
#                 p = a[x]#通过下标获取商品价格
#                 if p[1] <= b:#买的起
#                     z.append(p)#将该商品加到购物车
#                     b-= p[1]#扣钱
#                     print("添加成功,按exit结算")
#                 else:#买不起
#                     print("余额不足,添加失败，按exit结算")
#             else:#输入编号不存在
#                 print("商品不存在")
#         elif x == 'exit':
#             print("z")#打印商品清单
#             for p in z:
#                 print(p)
#             print("你的资产余额。。。",b)
#             exit()
#         else:
#             print("错误输入")



# 任意4个数字，组成不相同的三位数
# a = input('shuru:')
# a = a.split(',')
# y=[]
# l=[]
# for i in range(len(a)):
# 	for j in range(len(a)):
# 		for o in range(len(a)):
# 			s = a[i] + a[j] + a[o]
# 			y.append(s)
# for t in y:
# 	if t not in l:
# 		l.append(t)
# 		print(t)


# 将列表中的元素向左挪一位
# a = input('shuru:')
# a =a.split(',')
# x = a[0]
# a.pop(0)
# a.append(x)
# print(a)


# 一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# a = [1,2,3,4,5,6]
# x = 
# a.append(x)
# a.sort()
# print(a)



# 不用int将字符串变成整数
# a = input('shuru:')
# a = a[::-1]
# sum = 0
# for i in range(len(a)):
# 	for j in range(10):
# 		if str(j) == a[i]:
# 			sum += j*10**i
# print(sum)


# 十进制转十六进制
# b = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# a = input('qingshuru:')
# a = int(a)
# s = []
# while True:
# 	y = a%16
# 	a = a//16
# 	s.append(b[y])
# 	if a == 0:
# 		break
# s.reverse()
# m = s[0]
# for i in range(1,len(s)):
# 	m = m+s[i]
# print(m)


# 两个数的和等于的数
# def sum(x,y):
# 	for i in x:
# 		for j in x:
# 			if i+j == y:
# 				print(i)
# sum ([12,3,11,11,4,7,8],15)



# def yhsj(max):
#     n = 0
#     row = [1]
#     while (n<max):
#         n+=1
#         yield (row)
#         row = [1]+[row[k]+row[k+1] for k in range(len(row)-1)]+[1]
#
#
# y = yhsj(30)
#
#
# for i in y:
#     print(i)


# import day2
# print(day2.a(29,1,'+'))


# from day5 import sum

# print(sum())


# import day2
# # print(day2.qqq(day2.qwe([1,1,1,2,5,8,2,7])))


# # client  tcp客户端
# import socket
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 连接服务器
# sock.connect(('192.168.0.64',8888))
# while True:
#     # send 发送请求
#     reg = input('输入:')
#     if  reg != 'exit':
#         sock.send('hei'.encode('utf-8'))
#     # 接收数据
#         msg = sock.recv(1024)
#         print(msg.decode('utf-8'))
#     else:
#         break
#     # 断开连接
# sock.close()


# # client udp  客户端
# import socket
# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # 发送请求
# host = ('127.0.0.7',8888)
# while True:
#     a = input('输入:')
#     if a != 'exit':
#         sock.sendto('发送请求'.encode('utf-8'),host)
#         # 接收数据
#         msg = sock.recv(1024)
#         print(msg.decode('utf-8'))
#     else:
#         break
# sock.close()


# from tkinter import *
# from tkinter import messagebox
# from PIL import Image
# from PIL import ImageTk
#
# def haihao():
#     # 创建一个顶级窗口，依赖于原始窗口存在
#     messagebox.showinfo(title='秋意浓', message='我心难安')
#     haihao = Tk()
#     haihao.title('enenen')
#     haihao.geometry('700x700')
#     haihao.geometry('+400+80')
#     haihao.protocol('WM_DELETE_WINDOW', closewindow)
#     label = Label(haihao, text='只要你乖给你买条gai，只要你不乖头给你打歪', font=("微软雅黑", 20))
#     label.grid()
#     photo = Image.open('y.jpg')
#     phot = ImageTk.PhotoImage(photo)
#     pho = Label(haihao, image=phot)
#     pho.grid(row=2, columnspan=2)
#     botten = Button(haihao, text='点', width=5, height=3, command=chuangkou)
#     botten.grid(row=2, column=2, sticky=W)
#     haihao.mainloop()
#
# def closewindow():
#     # 设置提示信息
#     messagebox.showinfo(title='你打不过我吧,我就是那么强大',message='爱的魔力转圈圈，想你想到心花怒放黑夜白天')
#     # 关闭窗口
#     # chuangkou.destroy()
#     # return
# # 创建一个窗口
# chuangkou = Tk()
# # 命名窗口的标题
# chuangkou.title('Ss')
# # 设置窗口的大小
# chuangkou.geometry('700x700')
# # 设置窗口的位置
# chuangkou.geometry('+400+80')
# # 当用户关闭窗口时触发
# chuangkou.protocol('WM_DELETE_WINDOW',closewindow)
# # 添加文本标签(控件)
# label = Label(chuangkou,text='你害怕大雨吗,是不是还留短头发',font=("微软雅黑",20))
# # 显示标签
# label.grid()
# # 添加图片控件
# # imag = PhotoImage(file='su.JPG')
# # image = Label(chuangkou,image=imag)
# # image = Image.grid(row=2，columnspan=2)
# photo = Image.open('su.JPG')
# phot = ImageTk.PhotoImage(photo)
# pho = Label(chuangkou,image=phot)
# pho.grid(row=2,columnspan=2)
# # 添加一个按钮控件
# botten = Button(chuangkou,text='爱我',width=5,height=3,command=haihao)
# botten.grid(row=2,column=2,sticky=W)
# # 显示窗口
# chuangkou.mainloop()

a = 0
if a :
    print('asdad')