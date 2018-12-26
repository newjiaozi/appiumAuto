#coding=utf-8

from ..pageobject.myPage import MyPageWithoutLogin as MPWOL
from ..pageobject.myPage import LoginPage as LP
from ..pageobject.myPage import CodeLoginPage as CLP
from ..pageobject.myPage import AccountManage as AM
from ..pageobject.myPage import QuickLoginPage as QLP
from ..pageobject.myPage import MyPageWithLogin as MPWL

from .basePageAction import BasePageAction

class MyPageAction(BasePageAction):

    def checkMyPageUI(self,desc,nickname="登录"):
        person_info = self.waitPresents(MPWOL.PERSONINFO)
        person_info_text = self.waitPresents(MPWOL.PERSONINFO_TEXT)
        person_image = self.waitPresents(MPWOL.PERSONIMAGE)
        if person_info_text.get_attribute("text") == nickname:
            person_info_text = True
        else:
            person_info_text = False
        account_page = self.waitPresents(MPWOL.ACCOUNTMANAGE)
        account_page_text = self.waitPresents(MPWOL.ACCOUNTMANAGE_TEXT)
        message = self.waitPresents(MPWOL.MESSAGE)
        message_text1 = self.waitPresents(MPWOL.MESSAGE_TEXT1)
        message_text2 = self.waitPresents(MPWOL.MESSAGE_TEXT2)
        alarm = self.waitPresents(MPWOL.ALARM)
        alarm_text = self.waitPresents(MPWOL.ALARM_TEXT)
        feedback = self.waitPresents(MPWOL.FEEDBACK)
        feedback_text1 = self.waitPresents(MPWOL.FEEDBACK_TEXT1)
        feedback_text2 = self.waitPresents(MPWOL.FEEDBACK_TEXT2)
        app_info = self.waitPresents(MPWOL.APPINFO)
        app_info_text = self.waitPresents(MPWOL.APPINFO_TEXT)
        mybanner = self.waitPresents(MPWOL.MYBANNER)

        res = person_info and person_info_text and person_image and account_page and account_page_text and message and message_text1 and message_text2 and \
        alarm and alarm_text and feedback and feedback_text1 and feedback_text2 and app_info and app_info_text and mybanner
        if res:
            self.savePNG("MY页面检查通过，所有页面元素都正确_"+desc+"_"+nickname)
        else:
            self.savePNG("MY页面检查失败，页面元素不符合预期_"+desc+"_"+nickname)
        return res

    def clickPersonInfo(self):
        cb = self.waitPresents(LP.CLOSEBTN,seconds=5)
        if cb:
            return True ##
        return self.waitClick(MPWOL.PERSONINFO,seconds=2)

    def clickAccountManage(self):
        return self.waitClick(MPWOL.ACCOUNTMANAGE)

    def clickMessage(self):
        return self.waitClick(MPWOL.MESSAGE)

    def clickAlarm(self):
        return self.waitClick(MPWOL.ALARM)

    def clickFeedback(self):
        return self.waitClick(MPWOL.FEEDBACK)

    def clickAppInfo(self):
        return self.waitClick(MPWOL.APPINFO)

    def getInMyPage(self):
        cb = self.waitPresents(LP.CLOSEBTN,seconds=5)
        if cb:
            return True ##
        my = self.switchPage(MPWOL.MY)
        if my :
            if my.is_selected():
                return True
            else:
                my.click()
        else:
            print("找不到【MY】")
            return False

    def getInMyCartoon(self):
        myCartoon = self.switchPage(MPWOL.MYCARTOON)
        if myCartoon:
            if myCartoon.is_selected():
                return True
            else:
                myCartoon.click()
        else:
            print("找不到【我的漫画】")
            return False

    def getInDiscovery(self):
        discovery = self.switchPage(MPWOL.DISCOVERY)
        if discovery:
            if discovery.is_selected():
                return True
            else:
                discovery.click()
        else:
            print("找不到【发现】")
            return False

    def getInUpdate(self):
        update = self.switchPage(MPWOL.UPDATE)
        if update:
            if update.is_selected():
                return True
            else:
                update.click()
        else:
            print("找不到【更新】")
            return False

    def checkLoginPasswdUI(self,):
        switchBtn = self.waitPresents(CLP.SWITCHLOGIN)
        if switchBtn.get_attribute("text") == "验证码登录":
            return True
        elif switchBtn.get_attribute("text") == "密码登录":
            switchBtn.click()
            self.checkLoginPasswdUI()

    def checkLoginCodeUI(self,):
        switchBtn = self.waitPresents(CLP.SWITCHLOGIN)
        if switchBtn.get_attribute("text") == "验证码登录":
            switchBtn.click()
            self.checkLoginCodeUI()
        elif switchBtn.get_attribute("text") == "密码登录":
            return True

    def loginByPasswd(self,user,passwd,checkMsg,checkNickname,checkUserId,backInit,quickLogin,desc):
        if quickLogin and quickLogin.strip().lower() == "yes":
            self.waitClick(LP.CLOSEBTN)
            self.clickPersonInfo()
            self.waitClick(QLP.QUICKLOGIN)
            passwd = self.waitPresents(QLP.PASSWORD)
            passwd.clear()
            passwd.send_keys(passwd)
            self.waitClick(QLP.QUICKLOGIN)
            if checkMsg:
                self.waitTextInPage(text=checkMsg, screenshot=desc + checkMsg)
            if checkNickname:
                self.waitTextInPage(text=checkNickname, screenshot=desc + checkNickname)
                self.clickAccountManage()
                self.waitTextInPage(text=checkNickname, screenshot=desc + checkNickname)
            if checkUserId:
                self.waitTextInPage(text=checkNickname, screenshot=desc + checkUserId)
            if backInit:
                self.waitClick(AM.LOGOUT)
                self.waitClick(AM.OTHERLOGINMETHOD)
            return True
        else:
            close = self.waitPresents(QLP.CLOSE,seconds=3)
            if close:
                close.click()
            switchBtn = self.waitPresents(CLP.SWITCHLOGIN)
            if switchBtn:
                if switchBtn.get_attribute("text") == "验证码登录":
                    user_input = self.waitPresents(LP.MOBILEINPUT)
                    user_input.clear()
                    user_input.send_keys(user)
                    passwd_input = self.waitPresents(LP.PASSWDINPUT)
                    passwd_input.clear()
                    passwd_input.send_keys(passwd)
                    self.waitClick(LP.LOGINSUBMIT)
                    if checkMsg:
                        self.waitTextInPage(text=checkMsg,screenshot=desc+checkMsg)
                    if checkNickname:
                        self.waitTextInPage(text=checkNickname, screenshot=desc+checkNickname)
                        self.clickAccountManage()
                        self.waitTextInPage(text=checkNickname,screenshot=desc+checkNickname)
                    if checkUserId:
                        self.waitTextInPage(text=checkNickname, screenshot=desc + checkUserId)
                    if backInit:
                        self.waitClick(AM.LOGOUT)
                        self.waitClick(AM.OTHERLOGINMETHOD)
                    return True
                elif switchBtn.get_attribute("text") == "密码登录":
                    switchBtn.click()
                    return self.loginByPasswd(user,passwd,checkMsg,checkNickname,checkUserId,backInit,quickLogin,desc)
            else:
                print("未获取到元素：com.naver.linewebtoon.cn:id/login_page_login_type")
                return False

    def loginByCode(self,user,passwd,submit=True,msg=""):
        switchBtn = self.waitPresents(CLP.SWITCHLOGIN)
        if switchBtn:
            if switchBtn.get_attribute("text") == "密码登录":
                user_input = self.waitPresents(CLP.MOBILEINPUT)
                if user_input:
                    user_input.clear()
                    user_input.send_keys(user)
                passwd_input = self.waitPresents(CLP.CODEINPUT)
                if passwd_input:
                    passwd_input.clear()
                    passwd = input("请输入收到的手机验证码:")
                    passwd_input.send_keys(passwd)
                return True
            elif switchBtn.get_attribute("text") == "验证码登录":
                switchBtn.click()
                self.loginByPasswd()
        else:
            print("未获取到元素：com.naver.linewebtoon.cn:id/login_page_login_type")
            return False

    def loginByWechat(self,checkMsg,checkNickname,checkUserId,backInit,quickLogin,desc):
        if quickLogin and quickLogin.strip().lower() == "yes":
            ql = self.waitPresents(QLP.QUICKLOGIN)
            ql.click()
        else:
            close = self.waitPresents(QLP.CLOSE,seconds=3)
            if close:
                close.click()
            wl = self.waitPresents(CLP.WECHATLOGIN)
            wl.click()
        if checkMsg:
            self.waitTextInPage(text=checkMsg, screenshot=desc + checkMsg)
        if checkNickname:
            self.waitTextInPage(text=checkNickname, screenshot=desc + checkNickname)
            self.clickAccountManage()
            self.waitTextInPage(text=checkNickname, screenshot=desc + checkNickname)
        if checkUserId:
            self.waitTextInPage(text=checkNickname, screenshot=desc + checkUserId)
        if backInit:
            self.waitClick(AM.LOGOUT)
            self.waitClick(AM.OTHERLOGINMETHOD)

    def loginByWeibo(self,checkMsg,checkNickname,checkUserId,backInit,quickLogin,desc):
        if quickLogin and quickLogin.strip().lower() == "yes":
            ql = self.waitPresents(QLP.QUICKLOGIN)
            ql.click()
        else:
            close = self.waitPresents(QLP.CLOSE,seconds=3)
            if close:
                close.click()
            wl = self.waitPresents(CLP.WEIBOLOGIN)
            wl.click()
            wbc = self.waitPresents(LP.WEIBOLOGINCONFIRM)
            self.savePNG(desc+"微博确认登录")
            wbc.click()
        if checkMsg:
            self.waitTextInPage(text=checkMsg, screenshot=desc + checkMsg)
        if checkNickname:
            self.waitTextInPage(text=checkNickname, screenshot=desc + checkNickname)
            self.clickAccountManage()
            self.waitTextInPage(text=checkNickname, screenshot=desc + checkNickname)
        if checkUserId:
            self.waitTextInPage(text=checkNickname, screenshot=desc + checkUserId)
        if backInit:
            self.waitClick(AM.LOGOUT)
            self.waitClick(AM.OTHERLOGINMETHOD)
        return True

    def loginByQQ(self,checkMsg,checkNickname,checkUserId,backInit,quickLogin,desc):
        if quickLogin and quickLogin.strip().lower() == "yes":
            ql = self.waitPresents(QLP.QUICKLOGIN)
            ql.click()
        else:
            wl = self.waitPresents(CLP.QQLOGIN)
            wl.click()
        if checkMsg:
            self.waitTextInPage(text=checkMsg, screenshot=desc + checkMsg)
        if checkNickname:
            self.waitTextInPage(text=checkNickname, screenshot=desc + checkNickname)
            self.clickAccountManage()
            self.waitTextInPage(text=checkNickname, screenshot=desc + checkNickname)
        if checkUserId:
            self.waitTextInPage(text=checkNickname, screenshot=desc + checkUserId)
        if backInit:
            self.waitClick(AM.LOGOUT)
            self.waitClick(AM.OTHERLOGINMETHOD)

    def loginOut(self,desc):
        wl = self.waitPresents(AM.LOGOUT)
        wl.click()
