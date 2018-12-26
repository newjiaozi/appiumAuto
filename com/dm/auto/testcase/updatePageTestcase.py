#coding=utf-8


from .baseTestcase import BaseTestcase
from .tools import getTestData
from ddt import ddt,data,unpack

@ddt
class UpdatePageTestcase(BaseTestcase):
    ## 通过excel读取测试数据，通过case中数据来进行跳转判断
    @data(*getTestData("testdata/RegressionTesting.xlsx","更新",exec=9))
    @unpack
    def test_update(self,user,passwd,loginType,checkSplash,checkMsg,checkNickname,checkUserId,backInit,quickLogin,desc):
        if checkSplash:
            self.assertTrue(self.BPA.checkSplash(backInit))
        else:
            self.assertTrue(self.MPA.getInMyPage())  ## 进入MY页面
            self.assertTrue(self.MPA.clickPersonInfo()) ## 点击登录
            if loginType and loginType.strip().lower() == "mobilepassword":
                self.assertTrue(self.MPA.loginByPasswd(user=user,passwd=passwd,checkMsg=checkMsg,checkNickname=checkNickname,checkUserId=checkUserId,backInit=backInit,quickLogin=quickLogin,desc=desc))
            elif loginType and loginType.strip().lower() == "wechat":
                self.assertTrue(self.MPA.loginByWechat(checkMsg,checkNickname,checkUserId,backInit,quickLogin,desc))
            elif loginType and loginType.strip().lower() == "weibo":
                self.assertTrue(self.MPA.loginByWeibo(checkMsg, checkNickname, checkUserId, backInit, quickLogin, desc))
            elif loginType and loginType.strip().lower() == "email":
                self.assertTrue(self.MPA.loginByPasswd(user,passwd,checkMsg, checkNickname, checkUserId, backInit, quickLogin, desc))
            elif loginType and loginType.strip().lower() == "mobilecode":
                self.assertTrue(self.MPA.loginByCode())
            else:
                print("暂不支持的登录类型")


