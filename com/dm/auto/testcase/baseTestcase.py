#coding=utf-8

import unittest
import warnings
import os
from appium import webdriver
from ..action.myPageAction import MyPageAction as MPA
from ..action.basePageAction import BasePageAction as BPA

class BaseTestcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore",ResourceWarning)
        # from com.dm.auto.testcase.tools import getTestData
        # print(getTestData("testdata/RegressionTesting.xlsx", "login"))
        desired_caps = {}
        # cls.appPath = os.path.abspath(os.path.join(os.path.curdir,"app","dongman-qa-1.4.9_qa_1128.apk"))
        cls.appPath = r"c:\Users\test12\Downloads\dongman-qa-1.4.9_qa_1128.apk" #windows下app的路径
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '5.1'

        # desired_caps['deviceName'] = '28d15221'
        desired_caps['deviceName'] = '5f22ee3a'

        desired_caps['platformVersion'] = '6.0'
        # desired_caps['deviceName'] = 'Android Simulator'
        desired_caps['app'] = cls.appPath
        desired_caps["appPackage"] = "com.naver.linewebtoon.cn"
        desired_caps["appActivity"] = "com.naver.linewebtoon.splash.SplashActivity"

        desired_caps['noReset'] = False
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        desired_caps["automationName"] = "uiautomator2"
        cls.driver = webdriver.Remote('http://10.35.33.196:4723/wd/hub', desired_caps)
        cls.BPA = BPA(cls.driver)
        cls.MPA = MPA(cls.driver)
        cls.BPA.allowPermission()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()