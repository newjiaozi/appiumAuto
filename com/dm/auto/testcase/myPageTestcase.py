#coding=utf-8


from .baseTestcase import BaseTestcase
from .tools import getTestData
from ddt import ddt,data,unpack

@ddt
class MyPageTestcase(BaseTestcase):

    ## 通过excel读取测试数据，通过case中数据来进行跳转判断

    @data(*getTestData("testdata/RegressionTesting.xlsx","login"))
    @unpack
    def test1_loginByPasswd(self,user,passwd,loginType,checkSplash,checkMsg,checkNickname,checkUserId,backInit,quickLogin,desc,whetherExecute):
        if whetherExecute:
            if checkSplash:
                # if self.driver.is_app_installed("com.naver.linewebtoon.cn"):
                #     self.driver.remove_app("com.naver.linewebtoon.cn")
                #     self.driver.install_app(r"c:\Users\test12\Downloads\dongman-qa-1.4.9_qa_1128.apk")
                # else:
                #     self.driver.install_app(r"c:\Users\test12\Downloads\dongman-qa-1.4.9_qa_1128.apk")
                self.assertTrue(self.BPA.checkSplash(checkMsg,backInit))
            else:
                self.assertTrue(self.MPA.getInMyPage())  ## 进入MY页面
                self.assertTrue(self.MPA.checkMyPageUI(desc)) ## 未登录检查页面元素UI
                self.assertTrue(self.MPA.clickPersonInfo()) ## 点击登录
                self.assertTrue(self.MPA.loginByPasswd(user=user,passwd=passwd,loginType=loginType,checkMsg=checkMsg,checkNickname=checkNickname,checkUserId=checkUserId,backInit=backInit,quickLogin=quickLogin,desc=desc))


