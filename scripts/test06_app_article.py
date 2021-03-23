import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_logger import GetLogger
from tools.read_yaml import read_yaml

log =GetLogger().get_logger()

class TestAppArticle:
    # 1.初始化
    def setup_class(self):
        # 1.获取driver
        app_driver = GetDriver().get_app_driver()
        # 2.获取统一入口对象
        page_in = PageIn(app_driver)
        # 3.调用登录方法,
        # page_in.page_get_PageAppLogin().page_app_login_success()
        # 4.获取发布文章页面对象
        self.app_article = page_in.page_get_PageAppArticle()

    # 2.结束
    def teardown_class(self):
        # 关闭drver
        GetDriver.quit_app_driver()

    # 3.发布文章测试方法
    @pytest.mark.parametrize("find_str,title",read_yaml("app_article.yaml"))
    def test_app_article(self,find_str,title):
        # 调用文章业务方法
        try:
            self.app_article.page_app_article(find_str,title)
        except Exception as e:
            #日志
            log.error("出错原因：",e)
            #截图
            self.app_article.base_get_image()
            #抛异常
            raise

