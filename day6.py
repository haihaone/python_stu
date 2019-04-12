# import requests
# import re
# import xlwt
# import pymysql
# import xlrd
#
# class douban_Spider(object):
#
#  def qingqiu(self,page):
# 		ur = 'https://movie.douban.com/top250?start={}&filter='.format(page)
# 		# 伪装成浏览器
# 		# head = {
# 		# 	'User-Agent':'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.109Safari / 537.36'
# 		# }
#
# 		# 发送请求
# 		res = requests.get(url=ur)
# 		#  读取响应 1.text     以字符串的方式读取
# 		#          2.content  以字节的方式读取
# 		html = res.content.decode('utf-8')
# 		# 返回结果并赋值
# 		return html
#
 # def guolv(self,abc):
 #        shuju1 = []
 #        patt = re.compile(r'<span class="title">(.*?)</span>', re.S)
 #        items = patt.findall(abc)
 #        for i in items:
 #          i = i.replace('&nbsp;', '').replace('<br>', '').replace('<p>', '').strip()
 #          shuju1.append(i)
 #          return shuju1
 #
 # def guolv2(self,abc):
 #        shuju=[]
 #        patt=re.compile(r'<span class="inq">(.*?)</span>',re.S)
 #        items=patt.findall(abc)
 #        for i in items:
 #            i=i.replace('&nbsp;','').replace('<br>','').replace('<p>','').strip()
 #            shuju.append(i)
 #            return shuju
 #
 # def save(self,qwe):
	# 	with open('y.txt','a',encoding='utf-8') as f:
	# 		for i in qwe:
	# 			f.write(i+'\n')
# def t():
#  f=xlwt.Workbook()
#  sheet=f.add_sheet('电影')
#  k=open('y.txt','r',encoding='utf-8')
#  s=k.readlines()
#  print(s)
#  for i,j in enumerate(s):
#     j = j.replace('\n', '').split(',')
#     for k in range(len(j)):
#         sheet.write(i,k,j[k])
#  f.save('电影.xls')

# qiu = douban_Spider()
# for i in range(26):
#  html = qiu.qingqiu(page=i)
#  shuju1 = qiu.guolv(abc=html)
#  shuju = qiu.guolv2(abc=html)
#  qiu.save(shuju1)
#  qiu.save(shuju)
# # t()
#
# conn = pymysql.connect(host = '192.168.0.101',
#                        port = 3306,
#                        user = 'root',
#                        password = '123456',
#                        charset = 'utf8')
# abc = conn.cursor()
# # abc.execute('create database daoru1;')
# abc.execute('use daoru1')
# f = xlrd.open_workbook('电影.xls')
# sheet = f.sheets()[0]
# for i in range(sheet.nrows):
#     a = sheet.row_values(i)
#     if i == 0:
#         abc.execute('create table douban(电影 char(255));')
#     else:
#         abc.execute('insert into douban values("{}");'.format(a[0]))
#         conn.commit()
# abc.execute('select * from douban;')
# print(abc.fetchall())
# conn.close()
