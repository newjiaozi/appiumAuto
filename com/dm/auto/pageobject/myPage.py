#coding=utf-8

from selenium.webdriver.common.by import By
from .basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy


By.ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR

## 未登录状态，MY页面元素
class MyPageWithoutLogin(BasePage):

    PERSONIMAGE = (By.ID,"com.naver.linewebtoon.cn:id/personHeadImage")
    PERSONINFO = (By.ID,"com.naver.linewebtoon.cn:id/personInfo") ##
    PERSONINFO_TEXT = (By.ID,"com.naver.linewebtoon.cn:id/personNickname") ##
    ACCOUNTMANAGE = (By.ID,"com.naver.linewebtoon.cn:id/accountManage")
    ACCOUNTMANAGE_TEXT = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("账号管理")') ##
    MESSAGE = (By.ID,"com.naver.linewebtoon.cn:id/message")
    MESSAGE_TEXT1 = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("咚漫消息")')##
    MESSAGE_TEXT2= (By.ANDROID_UIAUTOMATOR,'new UiSelector().textContains("中奖名单")')##
    ALARM = (By.ID,"com.naver.linewebtoon.cn:id/alarm")
    ALARM_TEXT = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("推送设置")')##
    FEEDBACK = (By.ID,"com.naver.linewebtoon.cn:id/feedback")
    FEEDBACK_TEXT1 = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("意见反馈")') ##
    FEEDBACK_TEXT2 = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("写反馈")') ##
    APPINFO = (By.ID,"com.naver.linewebtoon.cn:id/appInfo")
    APPINFO_TEXT = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("APP信息")') ##
    MYBANNER = (By.ID,"com.naver.linewebtoon.cn:id/myBanner")

class MyPageWithLogin(MyPageWithoutLogin):
    pass


class CodeLoginPage(BasePage):

    SWITCHLOGIN = (By.ID,"com.naver.linewebtoon.cn:id/login_page_login_type")
    CLOSEBTN = (By.ID,"com.naver.linewebtoon.cn:id/id_pw_login_cn_close_btn")
    MOBILEINPUT = (By.ID,"com.naver.linewebtoon.cn:id/input_id")
    CODEINPUT = (By.ID,"com.naver.linewebtoon.cn:id/input_password")
    SENDCODE = (By.ID,"com.naver.linewebtoon.cn:id/login_page_get_vc")
    LOGINQUESTION = (By.ID,"com.naver.linewebtoon.cn:id/login_page_question")
    NAVERCORP = (By.ID,"com.naver.linewebtoon.cn:id/navercorp")
    TERMSOFSERVICE = (By.ID,"com.naver.linewebtoon.cn:id/btn_terms_of_service")
    NAVERCORPTEXT = (By.NAME,"Dongman Entertainment Corp")
    PRIVACYPOLICY = (By.ID,"com.naver.linewebtoon.cn:id/btn_privacy_policy")
    OTHERLOGIN = (By.ID,"com.naver.linewebtoon.cn:id/or")  ## 其他登录方式
    WEIBOLOGIN = (By.ID,"com.naver.linewebtoon.cn:id/btn_login_weibo")
    WECHATLOGIN = (By.ID,"com.naver.linewebtoon.cn:id/btn_login_wechat")
    QQLOGIN = (By.ID,"com.naver.linewebtoon.cn:id/btn_login_qq")


class PasswdLoginPage(BasePage):

    SWITCHLOGIN = (By.ID,"com.naver.linewebtoon.cn:id/login_page_login_type")
    CLOSEBTN = (By.ID,"com.naver.linewebtoon.cn:id/id_pw_login_cn_close_btn")
    MOBILEINPUT = (By.ID,"com.naver.linewebtoon.cn:id/input_id")
    MOBILEDELETE = (By.ID,"com.naver.linewebtoon.cn:id/login_page_delete")
    PASSWDINPUT = (By.ID,"com.naver.linewebtoon.cn:id/input_password") ## NAF=True,密码样式；
    RESETPASSWD = (By.ID,"com.naver.linewebtoon.cn:id/login_page_reset_password")
    LOGINSUBMIT = (By.ID,"com.naver.linewebtoon.cn:id/btn_log_in")
    AGREEMSG = (By.ID,"com.naver.linewebtoon.cn:id/login_page_term_and_private")
    LOGINQUESTION = (By.ID,"com.naver.linewebtoon.cn:id/login_page_question")
    NAVERCORP = (By.ID,"com.naver.linewebtoon.cn:id/navercorp")
    TERMSOFSERVICE = (By.ID,"com.naver.linewebtoon.cn:id/btn_terms_of_service")
    NAVERCORPTEXT = (By.NAME,"Dongman Entertainment Corp")
    PRIVACYPOLICY = (By.ID,"com.naver.linewebtoon.cn:id/btn_privacy_policy")
    ERRORMSG = (By.ID,"com.naver.linewebtoon.cn:id/txt_error_message") ## 左下角的提示message


class PasswdQuickLoginPage(BasePage):
    QUICKLOGIN = (By.ID,"com.naver.linewebtoon.cn:id/login_page_button")
    CLOSE = (By.ID,"com.naver.linewebtoon.cn:id/login_page_close")
    USER = (By.ID,"com.naver.linewebtoon.cn:id/login_page_username")

    ##nextPage:
    LOGINTYPE = (By.ID,"com.naver.linewebtoon.cn:id/login_page_login_type")
    PASSWORD = (By.ID,"com.naver.linewebtoon.cn:id/input_password")
    # LOGIN = (By.ID,"com.naver.linewebtoon.cn:id/login_page_button")

class AccountManage(BasePage):
    NICKNAME = (By.ID,"com.naver.linewebtoon.cn:id/account_nickname")
    USER = (By.ID,"com.naver.linewebtoon.cn:id/account_username")
    USERID = (By.ID,"com.naver.linewebtoon.cn:id/account_dongman_id")
    USEREMAIL = (By.ID,"com.naver.linewebtoon.cn:id/bind_email_text")
    USEREMAILAUTH = (By.ID,"com.naver.linewebtoon.cn:id/bind_email_auth")
    LOGOUT = (By.ID,"com.naver.linewebtoon.cn:id/login_account_logout_btn")
    ##nextPage:
    OTHERLOGINMETHOD = (By.ID,"com.naver.linewebtoon.cn:id/login_page_button_ohter")

















