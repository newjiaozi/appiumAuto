#coding = utf-8

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


By.ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR


class BasePage():

    JUMP = (By.ID,"com.naver.linewebtoon.cn:id/jump") ## 倒数跳过
    JUMPPAGE = (By.ID,"com.naver.linewebtoon.cn:id/tutorial_banner_bg") ##
    JUMPCLOSE = (By.ID,"com.naver.linewebtoon.cn:id/webview_btn_close") ## 闪屏页打开后，右上角的close
    UPDATE = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("更新")') ## 更新
    DISCOVERY = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("发现")')## 发现
    MYCARTOON = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("我的漫画")')## 我的漫画
    MY = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("MY")') ## MY
    PERMISSION = (By.ID,"com.android.packageinstaller:id/permission_allow_button")






