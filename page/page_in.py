from page.page_app_article import PageAppArticle
from page.page_app_login import PageAppLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin


class PageIn:

    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpArticle对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

    # 获取PageAppLogin对象
    def page_get_PageAppLogin(self):
        return PageAppLogin(self.driver)

    # 获取PageAppArticle对象
    def page_get_PageAppArticle(self):
        return PageAppArticle(self.driver)
