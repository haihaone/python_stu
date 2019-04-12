# !/usr/bin/python
# -*- coding:utf-8 -*-

from appium import webdriver
from time import sleep

desired_caps = {'platformName':'Android',
                # 'platformVersion':'6.0',
                'deviceName':'127.0.0.1:62001',
                'appPackage':'com.netease.cloudmusic',
                'appActivity':'.activity.LoadingActivity'}
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
sleep(15)
driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
sleep(3)
driver.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('17550682678')
sleep(3)
driver.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('haihao0701.1')
sleep(3)
driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
sleep(3)
driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()
sleep(3)
aa = driver.find_element_by_id('com.netease.cloudmusic:id/af4').text
if aa== 'Suyushuo_':
    print('pass')
else:
    print('fail')

#driver.quit()