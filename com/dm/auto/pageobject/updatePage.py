#coding=utf-8

from selenium.webdriver.common.by import By
from .basePage import BasePage
from appium.webdriver.common.mobileby import MobileBy


By.ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR
By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID

class RenQi(BasePage):
    GUANZHU = (By.ID,"com.naver.linewebtoon.cn:id/cardhome_title_my")
    GUANZHUEMPTY = (By.ID,"com.naver.linewebtoon.cn:id/empty_text")
    GUANZUEMPTYTEXT = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("没有关注的漫画。 添加到我的关注 新的章节更新时，会提醒您。")')
    RENQI = (By.ID,"com.naver.linewebtoon.cn:id/cardhome_title_daily")
    SEARCH = (By.ID,"com.naver.linewebtoon.cn:id/cardhome_search")
    MONDAY = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("周一")')
    TUESDAY = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("周二")')
    WEDNESDAY = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("周三")')
    THURSDAY = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("周四")')
    FRIDAY = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("周五")')
    SATURDAY = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("周六")')
    SUNDAY = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("周日")')
    TODAY = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("今天")')
    FINISH = (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("完结")')
    SEARCHINPUT = (By.ID,"com.naver.linewebtoon.cn:id/search_edit_text")
    SEARCHRESULTITEM = (By.ID,"com.naver.linewebtoon.cn:id/search_result_item")
    SEARCHRESULTTITLE = (By.ID,"com.naver.linewebtoon.cn:id/search_result_title")
    SEARCHRESULTAUTHOR = (By.ID,"com.naver.linewebtoon.cn:id/search_result_author")
    SCROLLINTO = [By.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(True)).scrollIntoView(new UiSelector().text("%s"))']
    ##单个封面上，页面元素，注意，每个漫画都是同样的id，会有重复的
    KIND = (By.ID,"com.naver.linewebtoon.cn:id/card_home_genre") ## 种类
    TITLE = (By.ID,"com.naver.linewebtoon.cn:id/card_home_title") ## 标题
    EPISODETITLE = (By.ID,"com.naver.linewebtoon.cn:id/card_home_episode_title") ## 章节名称
    TITLELIST = (By.ID,"com.naver.linewebtoon.cn:id/card_home_title_list") ## 最新话
    TITLEAUTHOR = (By.ID,"com.naver.linewebtoon.cn:id/card_home_txt_author") ## 作者
    TITLELIKEIT = (By.ID,"com.naver.linewebtoon.cn:id/card_home_likeit")  ##未点赞或已点赞
    TITLEADDSUBSCRIBE = (By.ID,"com.naver.linewebtoon.cn:id/card_home_add_subscribe")  ## 关注或者已关注

    ### 关注页面里的漫画：
    TITLELIKEDITFAV = (By.ID, "com.naver.linewebtoon.cn:id/card_favorite_likeit")  ## 未点赞或已点赞
    TITLEADDSUBSCRIBEFAV = (By.ID,"com.naver.linewebtoon.cn:id/card_favorite_add_subscribe")  ## 关注或者已关注
    KINDFAV = (By.ID,"com.naver.linewebtoon.cn:id/card_favorite_genre") ## 种类
    TITLEFAV = (By.ID,"com.naver.linewebtoon.cn:id/card_favorite_title") ## 标题
    EPISODETITLEFAV = (By.ID,"com.naver.linewebtoon.cn:id/card_favorite_episode_title") ## 章节名称
    TITLELISTFAV = (By.ID,"com.naver.linewebtoon.cn:id/card_favorite_title_list") ## 全集
    TITLEAUTHORFAV = (By.ID,"com.naver.linewebtoon.cn:id/card_favorite_txt_author") ## 作者




