import requests
import re
import os

class doutu():
    def qingqiu(self, page):
        url = 'https://www.doutula.com/article/list/?page={}'.format(page)
        head = {
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 56.0.2924.90Safari / 537.362345Explorer / 9.6.0.18627'
        }
        xiangying = requests.get(url=url,headers=head)
        html = xiangying.content.decode('utf-8')
        return html

    def guolv(self,qwe):
        abc = re.compile(r'</div> <div class="col-sm-9">(.*?)<div class="text-center">',re.S)
        item = abc.findall(qwe)
        taotu = []
        for i in item:
            patt = re.compile('href="(.*?)"class',re.S)
            zzz = patt.findall(i)
            taotu.append(zzz)
        tu = taotu[0]

        tuming = []
        for j in item:
            patt = re.compile('<div class="random_title">"(.*?)"<div class="date">',re.S)
            yyy = patt.findall(j)
            tuming.append(yyy)
        ming = tuming[0]

        dange = []
        for k in taotu[0]:
            head = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
            }
            wo = requests.get(k, headers=head)
            html = wo.content.decode('utf-8')
            s = re.compile(r"this.src='(.*?)'")
            u = s.findall(html)
            dange.append(u)

            for x in ming:
                os.mkdir(r'C:\Users\haihao\Desktop\gaoxiao文件\{}'.format(x))

            for s, y in enumerate(dange):
                os.chdir(r'C:\Users\haihao\Desktop\gaoxiao文件\{}'.format(ming[s]))
                for o in y:
                    res = requests.get(o)
                    ht = res.content
                    if '.gif' in o:
                        with open('{}.gif'.format(s), 'wb') as f:
                            f.write(ht)
                            s += 1
                    else:
                        with open('{}.jpg'.format(s), 'wb') as f:
                            f.write(ht)
                            s += 1
a = doutu()
b = a.qingqiu(1)
a.guolv(b)





# import requests
# import re
# import os
# class dou(object):
#     def fasong(self,page):
#         url = 'https://www.doutula.com/article/list/?page={}.format(page)'
#         head = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
#         }
#         xiang = requests.get(url, headers=head)
#         html = xiang.content.decode('utf-8')
#         return html
#
#     def guolv(self,abc):
#         patt = re.compile(r'</div> <div class="col-sm-9">(.*?)<div class="text-center">',re.S)
#         items = patt.findall(abc)
#
#         zutu=[]
#         for i in items:
#             pat = re.compile(r'href="(.*?)" class')
#             ite = pat.findall(i)
#             zutu.append(ite)
#         zu=zutu[0]
#
#         mingzi=[]
#         for j in items:
#             pa = re.compile(r'<div class="random_title">(.*?)<div class="date">')
#             it = pa.findall(j)
#             mingzi.append(it)
#         ming=mingzi[0]
#
#         dantu=[]
#         for q in zutu[0]:
#             head = {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
#             }
#             xiang = requests.get(q, headers=head)
#             html = xiang.content.decode('utf-8')
#             p = re.compile(r"this.src='(.*?)'")
#             t = p.findall(html)
#             dantu.append(t)
#
#         for e in ming:
#             os.mkdir(r'C:\Users\haihao\Desktop\doutu文件\{}'.format(e))
#
#         for p,r in enumerate(dantu):
#             os.chdir(r'C:\Users\haihao\Desktop\doutu文件\{}'.format(ming[p]))
#             for o in r:
#                 res=requests.get(o)
#                 ht=res.content
#                 if '.gif' in o:
#                     with open('{}.gif'.format(p),'wb') as f:
#                         f.write(ht)
#                         p+=1
#                 else:
#                     with open('{}.jpg'.format(p),'wb') as f:
#                         f.write(ht)
#                         p+=1
# a=dou()
# b=a.fasong(1)
# a.guolv(b)