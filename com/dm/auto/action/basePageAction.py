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


    def waitPresents(self,loc,seconds=10):
        try:
            ele = WebDriverWait(self.driver,seconds).until(EC.presence_of_element_located(loc))
            return ele
        except TimeoutException as e:
            print(e)
            print(loc)
            return False

    def waitTextInPage(self,text,screenshot="",seconds=10):
        try:
            WebDriverWait(self.driver,seconds).until(lambda x:text in x.page_source)
            if not screenshot:
                screenshot =text
            self.savePNG(screenshot)
            return True
        except TimeoutException as e:
            print(e)
            print(text)
            return False

    def waitClick(self,loc,seconds=10):
        try:
            ele = WebDriverWait(self.driver,seconds).until(EC.presence_of_element_located(loc))
            ele.click()
            return ele
        except TimeoutException as e:
            print(e)
            print(loc)
            return False

    def switchPage(self,loc,seconds=10):
        try:
            ele = WebDriverWait(self.driver,seconds).until(EC.presence_of_element_located(loc))
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
        if printPng:
            print(
                r'''<img src="%(pathfilename)s"  alt="%(filename)s"  title="%(filename)s" width="30" height="20"  onclick="window.open('%(pathfilename)s')"/>%(filename)s''' %
                {'filename':name,"pathfilename":_name})



    def allowPermission(self):
        print("允许获取权限")
        return self.waitClick(BP.PERMISSION,seconds=8)

    def waitStaleness(self,ele,seconds=5):
        try:
            WebDriverWait(self.driver,seconds).until(EC.staleness_of(ele))
            return True
        except TimeoutException as e:
            print(e)
            return False

    def passJump(self,seconds=30):
        _jump = self.waitPresents(BP.JUMP,seconds=seconds)
        if _jump:
            self.savePNG("跳过出现")
            self.waitStaleness(_jump)
            self.savePNG("跳过消失")
        return True

    def checkSplash(self,text,bachInit,seconds=20):
        _splash = self.waitPresents(BP.JUMPPAGE,seconds=seconds)
        if _splash:
            self.savePNG("开屏页截屏")
            _splash.click()
            if text:
                _text = self.waitTextInPage(text)
                if _text:
                    self.savePNG("开屏页跳转页面截屏:%s" % text)
                    if bachInit:
                        self.waitClick(BP.JUMPCLOSE)
                        self.savePNG("开屏页跳转页面关闭:%s" % text)
                    return True
                else:
                    return False
            return True
        else:
            print("未发现开屏页")
            return False #

    def switchApp(self):
        print(self.driver.contexts)





