import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from threading import Thread

import time,os

class MyTestCase(unittest.TestCase):
    appPath = ""

    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        cls.appPath = os.path.abspath(os.path.join(os.path.curdir,"app","dongman-qa-1.4.9_qa_1128.apk"))
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        # desired_caps['deviceName'] = '28d15221'
        desired_caps['deviceName'] = 'Android Simulator'
        desired_caps['app'] = cls.appPath
        desired_caps["appPackage"] = "com.naver.linewebtoon.cn"
        desired_caps["appActivity"] = "com.naver.linewebtoon.splash.SplashActivity"
        desired_caps['noReset'] = False
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        desired_caps["automationName"] = "uiautomator2"
        # desired_caps["avd"] = "Nexus_5X_API_24"
        # desired_caps["avd"] = "Nexus_6_API_23"
        cls.wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        cls.wd.implicitly_wait(20)
        cls.window_size = cls.wd.get_window_size()
        cls.width = cls.window_size["width"]
        cls.height = cls.window_size["height"]
    def test1_permission_allow(self):
        loc = ("id", "com.android.packageinstaller:id/permission_allow_button")
        e = WebDriverWait(self.wd,10).until(EC.presence_of_element_located(loc))
        e.click()
        time.sleep(2)
        self.wd.save_screenshot("首页.png")

    def test3_My(self):
        # banner_page = ("id","com.naver.linewebtoon.cn:id/banner_pager")
        # WebDriverWait(self.wd, 10).until(EC.presence_of_element_located(banner_page))
        my = self.wd.find_element_by_android_uiautomator('new UiSelector().text("MY")')
        my.click()
        dl = self.wd.find_element_by_android_uiautomator('new UiSelector().text("登录")')
        zhgl = self.wd.find_element_by_android_uiautomator('new UiSelector().text("账号管理")')
        dmxx = self.wd.find_element_by_android_uiautomator('new UiSelector().text("咚漫消息")')
        tssz = self.wd.find_element_by_android_uiautomator('new UiSelector().text("推送设置")')
        yjfk = self.wd.find_element_by_android_uiautomator('new UiSelector().text("意见反馈")')
        appxx = self.wd.find_element_by_android_uiautomator('new UiSelector().text("APP信息")')
        if dl and zhgl and dmxx and tssz and yjfk and appxx:
            return True

    def test4_login(self):
        dl = self.wd.find_element_by_android_uiautomator('new UiSelector().text("登录")')
        dl.click()
        phone_input = self.wd.find_element_by_android_uiautomator('new UiSelector().text("请输入手机号")')
        code_input = self.wd.find_element_by_android_uiautomator('new UiSelector().text("请输入短信验证码")')
        send_code = self.wd.find_element_by_android_uiautomator('new UiSelector().resourceId("com.naver.linewebtoon.cn:id/login_page_get_vc")')
        phone_input.clear()
        phone_input.send_keys("13683581996")
        send_code.click()
        code_input.clear()
        code = input("输入验证码：")
        code_input.send_keys(code)



    def swipeUp(self, n=5):
        '''定义向上滑动方法'''
        print("定义向上滑动方法")
        x1 = self.width * 0.5
        y1 = self.height * 0.9
        y2 = self.height * 0.25
        time.sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            time.sleep(3)
            self.wd.swipe(x1, y1, x1, y2)

    def swipeDown(self, n=5):
        '''定义向下滑动方法'''
        print("定义向下滑动方法")
        x1 = self.width * 0.5
        y1 = self.height * 0.25
        y2 = self.height * 0.9
        time.sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            time.sleep(3)
            self.wd.swipe(x1, y1, x1, y2)

    def swipeLeft(self, n=5):
        '''定义向左滑动方法'''
        print("定义向左滑动方法")
        x1 = self.width * 0.8
        x2 = self.width * 0.2
        y1 = self.height * 0.5

        time.sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            time.sleep(3)
            self.wd.swipe(x1, y1, x2, y1)

    def swipeRight(self, n=5):
        '''定义向右滑动方法'''
        print("定义向右滑动方法")
        x1 = self.width * 0.2
        x2 = self.width * 0.8
        y1 = self.height * 0.5

        time.sleep(3)
        print("滑动前")
        for i in range(n):
            print("第%d次滑屏" % i)
            time.sleep(3)
            self.wd.swipe(x1, y1, x2, y1)

    @classmethod
    def tearDown(cls):
        cls.wd.quit()

if __name__ == '__main__':
    unittest.main()
