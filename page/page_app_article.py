import page
from base.app_base import AppBase
from tools.get_logger import GetLogger

log = GetLogger().get_logger()
class PageAppArticle(AppBase) :
    # 1.查找频道
    def page_click_channel(self,click_text) :
        #调用从右向左滑动方法
        self.app_base_right_wipe_left(click_text)

    # 2.查找文章
    def page_click_article(self,title) :

        # 3.查找文章业务方法
        #调用从下往上滑动的方法
        self.app_base_down_wipe_up(click_text=title)

    def page_app_article(self,find_text,title) :
        log.info("正在调用查看文章业务方法，所属文章{},文章标题{}".format(find_text,title))
        # 1.调用查找频道
        self.page_click_channel(find_text)
        # 2.调用查找文章
        self.page_click_article(title)


