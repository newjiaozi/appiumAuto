#coding = utf-8

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


By.ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR
By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID

class BasePage():

    JUMP = (By.ID,"com.naver.linewebtoon.cn:id/jump") ## 倒数跳过
    JUMPPAGE = (By.ID,"com.naver.linewebtoon.cn:id/tutorial_banner_bg") ##
    JUMPCLOSE = (By.ID,"com.naver.linewebtoon.cn:id/webview_btn_close") ## 闪屏页打开后，右上角的close
    UPDATE = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("更新")') ## 更新
    DISCOVERY = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("发现")')## 发现
    MYCARTOON = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("我的漫画")')## 我的漫画
    MY = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("MY")') ## MY
    PERMISSION = (By.ID,"com.android.packageinstaller:id/permission_allow_button")
    WEBVIEWCLOSE = (By.ACCESSIBILITY_ID,"close")


    ## 活动弹窗
    POPUPBANNER = (By.ID,"com.naver.linewebtoon.cn:id/promotion_popup_banner")
    POPUPBANNERCLOSE = (By.ID, "com.naver.linewebtoon.cn:id/promotion_popup_close_btn")


    ##listview
    BACK = (By.ACCESSIBILITY_ID,"转到上一层级")
    SUBSCRIBE = (By.ID,"com.naver.linewebtoon.cn:id/add_subscribe")
    REMOVESUBSCRIBE = (By.ID,"com.naver.linewebtoon.cn:id/remove_subscribe")
    TITLENAME = (By.ID,"com.naver.linewebtoon.cn:id/title_name")
    XUANJI = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("选集")')
    JIESHAO = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("作品介绍")')
    LISTVIEW = (By.ID,"com.naver.linewebtoon.cn:id/episode_listview")
    FOOTERTITLE = (By.ID,"com.naver.linewebtoon.cn:id/episode_footer_title")
    FOOTERBTN = (By.ID,"com.naver.linewebtoon.cn:id/episode_footer_btn")
    CONTENT = (By.ID,"com.naver.linewebtoon.cn:id/summary_content")
    CREATERNAME = (By.ID,"com.naver.linewebtoon.cn:id/creator_name")

    ##viewer
    TOOLBAR = (By.ID,"com.naver.linewebtoon.cn:id/toolbar") ##顶部工具条
    TOOLBARTEXTVIEW1 = (By.CLASS_NAME,"android.widget.TextView") ## 工具条下的第一个textview，应该是第几话
    VIEWERBACK = (By.ACCESSIBILITY_ID,"转到上一层级") ##返回上一层
    LIKE = (By.ID,"com.naver.linewebtoon.cn:id/viewer_like_button")  ##点赞
    PREV = (By.ID,"com.naver.linewebtoon.cn:id/bt_episode_prev")  ##上一话
    NEXT = (By.ID,"com.naver.linewebtoon.cn:id/bt_episode_next")  ##下一话
    COMMENT = (By.ID,"com.naver.linewebtoon.cn:id/comment_editor") ##评论输入
    COMMENTSUBMIT = (By.ID,"com.naver.linewebtoon.cn:id/comment_submit") ##评论提交
    NIGHT = (By.ID,"com.naver.linewebtoon.cn:id/action_brightness") ## 切换阅读 光
    SHARE = (By.ID,"com.naver.linewebtoon.cn:id/action_share")  ## 分享
    EPISODENO = (By.ANDROID_UIAUTOMATOR,'new UiSelector().textMatches("^第.*?话$")') ##第几话





