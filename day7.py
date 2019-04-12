#把九九乘法表导入a.txt文件
f = open('a.txt','w',encoding = 'utf-8')
for i in range(1,10):
    for j in range(1,i+1):
        f.write('{}*{}={}\t'.format(i,j,i*j))
    f.write('\n')
f.close()


#文件写入表格
import xlwt
import xlrd
f = xlwt.Workbook()
sheet=f.add_sheet('99')
s = open('a.txt','r',encoding='utf-8')
a = s.readlines()
print(a)
for i,j in enumerate(a):
    j=j.replace('\n','').split(',')
    for k in range(len(j)):
        sheet.write(i,k,j[k])
f.save('99乘法表.xls')



#表格写入表格
import xlwt
import xlrd
from xlutils.copy import copy
f = xlrd.open_workbook('软件测试工程师.xls')
new_f = copy(f)
sheet = new_f.get_sheet(0)
sheet.write(10,10)
new_f.save('软件测试工程师1.xls')


#表格写入文件
import xlwt
import xlrd
f=xlrd.open_workbook('电影.xls')
k=open('aa.txt','w',encoding='utf-8')
sheet=f.sheets()[0]
for i in range(sheet.nrows):
    a=(sheet.row_values(i))
    a=''.join(a)
    k.write('{}\n'.format(a))



#发送邮件
import smtplib  # 链接邮件服务器
import email .mime.multipart  #  处理邮件的组成
import email.mime.text  #  处理邮件正文
server = 'smtp.163.com' # 邮件服务器
fasong = '17550682678@163.com'
jieshou = '18438513345@163.com'
passwd = 'haihao0701' # 授权吗 允许登录客户端的密码
#创建一个空的邮件
message = email.mime.multipart.MIMEMultipart()
message['From'] = fasong #邮件的发件人
message['To'] = jieshou  #邮件的接受者
message['Subject'] = '你快乐吗' #邮件主题
text = "你是不是真正的快乐"
# 对正文进行编码
tet = email.mime.text.MIMEText(text,'plain','utf-8')
#将正文添加到邮件中
message.attach(tet)
# 带附件的
# 对附件进行读取和编码
ooo = email.mime.text.MIMEText(open('y.txt','rb').read(),'base64','utf-8')
# 给附件添加头部信息
ooo["Content-Type"] = 'application/octet-strem'
ooo["Content-Disposition"] = 'attachment;filenme = "y.txt"'
message.attach(ooo)
# 链接服务器
smtp123 = smtplib.SMTP_SSL(server,465)
# 登录服务器
smtp123.login(fasong,passwd)
smtp123.sendmail(fasong,jieshou,message.as_string())
# 断开连接
smtp123.close()


#输入一个日期,打印是否为闰年,星期几,一年中的第几天
import time
a=input('输入一个日期')
b=[]
for i in range(4):
    b.append(a[i])
b=b[::-1]
sum=0
for z in range(len(b)):
    for j in range(10):
        if str(j)==b[z]:
            sum=sum+j*10**z
if sum%4==0:
    print('是闰年')
else:
    print('不是闰年')
t=time.strptime(a,'%Y-%m-%d')
print('星期{},一年中的第{}天'.format(t[6]+1,t[7]))


#读取数据库到TXT文件
import pymysql
def ku():
    shujuku=pymysql.connect(host='192.168.0.60',
                            port=3306,
                            user='root',
                            password='123456',
                            charset='utf8')
    gb=shujuku.cursor()
    gb.execute('use py;')
    gb.execute('select * from douban;')
    a=gb.fetchall()
    gb.execute('desc douban')
    b=gb.fetchall()
    shujuku.close()
    with open('a.txt','w',encoding='utf-8') as f:
        for k in b:
            if k != b[-1]:
                f.write(k[0]+',')
            else:
                f.write(k[0]+'\n')
        for i in a:
            for j in range(len(i)):
                if i[j] != i[-1]:
                    f.write(i[j]+',')
                else:
                    f.write(i[j]+'\n')



import paramiko
#创建一个远程客户端
ssh123 = paramiko.SSHClient()
#第一次连接主机，known_hosts 存放的主机地址，跳过查找
#  允许连接不在 known_hosts 文件中的主机
ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#链接主机
ssh123.connect(hostname='192.168.0.86',
               port=22,
               username='root',
               password='123456')
#exec_command 执行命令  直接具有结果的命令
# a,b,c = ssh123.exec_command('ls -al /etc')
# 第一个变量：表示输入的命令
# 第二个变量：表示执行的结果
# 第三个变量： 命令的报错
while True:
    try:
        a = input('>>>')
        if a!= 'exit':
            a,b,c=ssh123.exec_command(a)
            print(b.read().decode())
        else:
            break
    except:
        continue
ssh123.close()


# 传输文件
# 建立一个传输通道
ssh123 = paramiko.Transport('192.168.0.86',22)
# 连接linux
ssh123.connect(username='root',password='123456')
# 创建一个传输文件的对象
sftp = paramiko.SFTPClient.from_transport(ssh123)
# 从linux 到 windows传文件
# 第一个参数：表示要传的文件
# 第二个参数：表示要存放的本机位置
sftp.get('install.log',r'.\install.log')
ssh123.close()
# 从windows 到 linux
sftp.put('day1.py',r'/home/day7.py')
ssh123.close()


# socket 自带
# socket :套接字，是实现最底层的一种通信方式  接收  发送
# 采用的是 cs 架构
# 通过 tcp 协议进行通信  socket
# server端（服务器端）
import socket
# 创建一个套接字,规定使用tcp协议 .ip版本ipv4
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定ip，端口号
s.bind(('192.168.0.64',8888))
# 监听服务是否开启，数字指的是最大等待数
# netstart
s.listen(3)
while True:
    #  接收请求  第一个变量：是连接信息  第二变量：客户端的ip和端口号
    conn,addr = s.accept()
    # 接收数据  1024表示一次性最大能接收1024字节的数据
    reg = conn.recv(1024)
    print(reg.decode('utf-8'))
    # 发送数据
    msg = input('输入:')
    conn.send(msg.encode('utf-8'))