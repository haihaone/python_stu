# from selenium import webdriver
# from time import sleep
# 定义使用什么浏览器
# dr = webdriver.Chrome()
# 打开网址
# dr.get('https://www.baidu.com')
# print(dr.title)   # # 获取网址的标题
# print(dr.current_url)  # # 获取打开网页的网址
# sleep(2)
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


# # QQ空间
# from selenium import webdriver
# from time import sleep
# dr = webdriver.Chrome()
# dr.get('https://qzone.qq.com/')
# # 处理框架  iframe（窗口）
# # dr.switch_to_frame() 框架的id或name或者，先定位到框架
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('985435261')
# dr.find_element_by_id('p').send_keys('haihao0701.0')
# dr.find_element_by_id('login_button').click()
# sleep(3)
# dr.find_element_by_css_selector('html.skin-dark.pg-profile body#QZ_Body.bg_body.mode_bg_opacity100 div.top-fix-bar div.top-fix-inner div#QZ_Toolbar_Container.top-fix-container div.top-fix-wrap ul.top-nav li#tb_app_li.nav-list div.nav-list-inner a#aAppstore.application-link.a-link span').click()
# sleep(3)




# 携程
# from selenium import webdriver
# from time import sleep
# dr = webdriver.Chrome()
# dr.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
# sleep(2)
# wd = dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_xpath('option')
# for i in wd:
#     i.click()
#     sleep(2)


# # 微博
# from selenium import webdriver
# from time import sleep
# dr = webdriver.Firefox()
# dr.get('https://www.baidu.com/')
# dr.find_element_by_id('kw').send_keys('微博')
# dr.find_element_by_id('su').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/h3/a[1]').click()
# sleep(2)
# ss = dr.window_handles
# dr.switch_to.window(ss[-1])
# sleep(2)







# 切换到某一个框架
# dr.switch_to.frame(ss)
# 回到最后开始的页面中
# dr.switch_to.default_content()
# 回到父框架页面中
# dr.switch_to.parent_frame()

# 处理浏览器窗口
# 获取当前窗口的字符串（句柄）
# dr.current_window_handle                                                                                  
# 获取所有窗口的句柄
# dr.window_handles
# 切换句柄  参数只能是句柄
# dr.switch_to.window([-1])



# # 京东购物车
# from selenium import webdriver
# from time import sleep
# dr = webdriver.Chrome()
# dr.get('https://www.baidu.com/')
# dr.find_element_by_id('kw').send_keys('京东')
# dr.find_element_by_id('su').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[4]/div[1]/div/div/div[1]/div/div[1]/div/h2/a[1]').click()
# sleep(2)
# ss = dr.window_handles
# dr.switch_to.window(ss[-1])
# sleep(2)
# dr.find_element_by_id('key').send_keys('python')
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div[2]/button/i').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[7]/a[3]').click()
# sleep(2)
# yy = dr.window_handles
# dr.switch_to.window(yy[-2])
# dr.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]/a').click()



# from selenium import webdriver
# from selenium.webdriver.common.keys import  Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from time import  sleep
# import selenium.webdriver.support.ui as ui
# dr = webdriver.Chrome()
# # 模拟鼠标的操作
# dr.maximize_window()
# dr.get('https://www.jd.com')
# sleep(2)
# s = dr.find_element_by_xpath('//*[@id="J_cate"]').find_element_by_class_name('/html/body/div[1]/div[5]/div[1]/div[1]/div/ul/li[2]')
# for i in s:
#     # 控制鼠标来移动到元素的位置上      执行
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)


# 京东拖动登录
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium import webdriver
# from selenium.webdriver.common.keys import  Keys
# from time import sleep
# dr = webdriver.Chrome()
# dr.get('https://www.baidu.com/')
# dr.find_element_by_id('kw').send_keys('京东')
# dr.find_element_by_id('su').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div[4]/div[1]/div/div/div[1]/div/div[1]/div/h2/a[1]').click()
# sleep(2)
# ss = dr.window_handles
# dr.switch_to.window(ss[-1])
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul[2]/li[1]/a[1]').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/a').click()
# dr.find_element_by_id('loginname').send_keys('123456')
# dr.find_element_by_id('nloginpwd').send_keys('123456')
# dr.find_element_by_id('loginsubmit').click()
# sleep(2)
# start = dr.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div[3]')
# # drag_and_drop(起始位置，结束位置)
# # drag_and_drop_by_offset(起始位置，x轴坐标，y轴坐标)
# ActionChains(dr).drag_and_drop_by_offset(start,99,0).perform()
# sleep(2)



# # 处理弹出框
# dr.get('http://www.lwfree.cn/yurenjie/yuerenjie1.html')
# sleep(2)
# # 切换到弹出框
# ww = dr.switch_to.alert
# # 获取弹出框上面的内容
# print(ww.text)
# #点击确定
# ww.accept()
# # 点击取消
# ww.dismiss()
# # 输入
# ww.send_keys('内容')


# # 处理页面滚动条 javascript代码
# dr.get('https://www.jd.com')
# for i in range(1,10000,2000):
#     js = "var q=document.documentElement.scrollTop={}".format(i)
#     # 执行JavaScript语句
#     dr.execute_script(js)
#     sleep(2)


# from selenium import webdriver
# from selenium.webdriver.common.keys import  Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from time import  sleep
# import selenium.webdriver.support.ui as ui
# dr = webdriver.Chrome()
# dr.get('https://www.jd.com')
# # 智能等待 设置一个最大的等待时间
# # 检测到某个元素出现，就不会继续等待
# # 设置最大等待时间
# unit = ui.WebDriverWait(dr,10)
# # 直到定位的元素出现，就不等待了
# unit.until(lambda dr: dr.find_element_by_xpath('//*[@id="key"]').is_displayed())
# print('hello')


# # 获取定位到的元素某个属性的值
# w = dr.find_element_by_xpath('')
# a = w.get_attribute('')


# import requests
# import unittest
# from selenium import webdriver
# from time import sleep
#
# class kongjian(unittest.TestCase):
#     def setup(self):
#         self.dr = webdriver.Chrome()
#         self.dr.maximize_window()
#     def login(self,s,y):
#         self.dr.get('https://qzone.qq.com/')
#         self.dr.switch_to.frame('login_frame')
#         sleep(2)
#         self.dr.find_element_by_id('switcher_plogin').click()
#         sleep(2)
#         self.dr.find_element_by_id('u').send_keys('s')
#         self.dr.find_element_by_id('p').send_keys('y')
#         self.dr.find_element_by_id('login_button').click()
#         sleep(3)
#     def test_login_success(self):
#         self.login('985435261', 'haihao0701.0')
#         sleep(3)
#         s = self.dr.find_element_by_id('title_2')
#         self.assertTrue(s['账号密码登录'],'主页')
#
# if __import__=="__main__":
#     unittest.main()


import unittest
from selenium import webdriver
from time import sleep
class Lon(unittest.TestCase):

    def  setUp(self):
        self.dr=webdriver.Firefox()
        self.dr.get('https://qzone.qq.com')
    def  test_Login(self):
        self.dr.switch_to.frame('login_frame')
        self.dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="u"]').send_keys(985435261)
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="p"]').send_keys('haihao0701.')
        sleep(2)
        self.dr.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(2)
        self.assertEqual(self.dr.title,'[http://985435261.qzone.qq.com]')
        self.dr.refresh()

    def tearDown(self):
        self.dr.quit()
if __name__=='__main__':
    unittest.main()