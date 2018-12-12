import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os
import warnings
from selenium.common.exceptions import TimeoutException

class MyTestCase(unittest.TestCase):
    appPath = ""


    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore",ResourceWarning)
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

    def test1_loginByPasswd(self,first=True):
        if first:
            loc = ("id", "com.android.packageinstaller:id/permission_allow_button")
            try:
                e = WebDriverWait(self.wd,10).until(EC.presence_of_element_located(loc))
                e.click()
                time.sleep(2)
            except TimeoutException as e:
                print(e)
            self.wd.save_screenshot("首页.png")
            my = self.wd.find_element_by_android_uiautomator('new UiSelector().text("MY")')
            my.click()
            login_btn = self.wd.find_element_by_android_uiautomator('new UiSelector().text("登录")')
            login_btn.click()
        switch_login = self.wd.find_element_by_id("com.naver.linewebtoon.cn:id/login_page_login_type")
        switch_login_text = switch_login.get_attribute("text")
        if switch_login_text == "验证码登录":
            print("当前为密码登录状态")
            input_id = self.wd.find_element_by_id("com.naver.linewebtoon.cn:id/input_id")
            input_password = self.wd.find_element_by_id("com.naver.linewebtoon.cn:id/input_password")
            input_id.clear()
            input_password.clear()
            input_id.send_keys("newjiaozi@163.com")
            input_password.send_keys("qwe123")
            login_btn = self.wd.find_element_by_id("com.naver.linewebtoon.cn:id/btn_log_in")
            login_btn.click()
            try:
                WebDriverWait(self.wd,10).until(lambda x:"登录成功" in x.page_source)
                print("登录成功")
                self.wd.save_screenshot("登录成功.png")
                WebDriverWait(self.wd, 10).until(lambda x: "登录成功" not in x.page_source)
                self.wd.save_screenshot("登录成功消失.png")
                nickname = self.wd.find_element_by_id("com.naver.linewebtoon.cn:id/personNickname")
                self.assertEqual("hehehe睡觉睡觉",nickname.get_attribute("text"))
                return True
            except Exception as e:
                print(e)
                return False

        elif switch_login_text == "密码登录":
            print("当前为验证码登录状态")
            switch_login.click()
            self.test1_loginByPasswd(first=False)

        else:
            print("有错误！")


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
    def tearDownClass(cls):
        cls.wd.quit()

if __name__ == '__main__':
    unittest.main()
