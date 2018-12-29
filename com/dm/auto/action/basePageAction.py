#coding=utf-8


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time
from ..pageobject.basePage import BasePage as BP


class BasePageAction():

    def __init__(self,driver):
        self.driver = driver


    def waitPresents(self,loc,seconds=10,poll_frequency=0.5):
        try:
            ele = WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.presence_of_element_located(loc))
            return ele
        except TimeoutException as e:
            print(e)
            print(loc)
            return False

    def waitTextInPage(self,text,screenshot="",seconds=10,poll_frequency=0.5):
        try:
            WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(lambda x:text in x.page_source)
            if not screenshot:
                screenshot =text
            self.savePNG(screenshot)
            return True
        except TimeoutException as e:
            print(e)
            print(text)
            return False

    def waitClick(self,loc,seconds=10,poll_frequency=0.5):
        try:
            ele = WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.presence_of_element_located(loc))
            ele.click()
            return ele
        except TimeoutException as e:
            print(e)
            print(loc)
            return False

    def switchPage(self,loc,seconds=10,poll_frequency=0.5):
        try:
            ele = WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.presence_of_element_located(loc))
            if ele.is_selected():
                return ele
            else:
                ele.click()
                return ele
        except TimeoutException as e:
            print(e)
            print(loc)
            return False


    # def savePNG(self,name):
    #     _name = os.path.abspath(os.path.join(os.path.curdir, "screenshots", name+".png"))
    #     print(_name)
    #     self.driver.save_screenshot(_name)

    def savePNG(self,name,printPng=True):
        _name = os.path.abspath(os.path.join(os.path.curdir, "screenshots", name+".png"))
        self.driver.get_screenshot_as_file(_name)
        src = "..\screenshots\%s" % name+".png"
        if printPng:
            print(r'''<img src="%(src)s"  alt="%(filename)s"  title="%(filename)s" height="100" width="100" class="pimg"  onclick="javascript:window.open(this.src);"/>%(filename)s''' % {'filename':name,"src":src})



    def allowPermission(self):
        print("允许获取权限")
        return self.waitClick(BP.PERMISSION,seconds=8)

    def waitStaleness(self,ele,seconds=5,poll_frequency=0.5):
        try:
            WebDriverWait(self.driver,seconds,poll_frequency=poll_frequency).until(EC.staleness_of(ele))
            return True
        except TimeoutException as e:
            print(e)
            return False

    def passJump(self,seconds=30,poll_frequency=0.1):
        _jump = self.waitPresents(BP.JUMP,seconds=seconds,poll_frequency=poll_frequency)
        if _jump:
            self.savePNG("跳过出现")
            self.waitStaleness(_jump)
            self.savePNG("跳过消失")
        return True

    def checkSplash(self,bachInit,seconds=20,poll_frequency=0.1):
        _jump = self.waitPresents(BP.JUMP,seconds=seconds,poll_frequency=poll_frequency)
        if _jump:
            _splash = self.waitClick(BP.JUMPPAGE,seconds=seconds,poll_frequency=poll_frequency)
            self.savePNG("开屏页截屏")
            if bachInit:
                wc = self.waitPresents(BP.WEBVIEWCLOSE)
                time.sleep(5)
                self.savePNG("开屏页跳转页面展示")
                wc.click()
                self.waitStaleness(wc)
                self.savePNG("开屏页跳转页面关闭")
                return True
            return True
        else:
            print("未发现开屏页")
            return False #

    def switchApp(self):
        print(self.driver.contexts)

    def popUpClose(self):
        popupWindow = self.waitPresents(BP.POPUPBANNER)
        self.savePNG("弹出活动页面")
        self.waitClick()






