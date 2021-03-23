import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_logger import GetLogger
from tools.read_yaml import read_yaml

log = GetLogger().get_logger()
class TestMpArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver().get_web_driver(page.url_mp)
        # 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 获取PageMpLogin对象并调用成功登录依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        # 获取PageMpArticle页面对象
        self.mp_article = self.page_in.page_get_PageMpArticle()
        #

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver().quit_web_driver()

    # 发表文章测试方法
    @pytest.mark.parametrize("title,content,expect",read_yaml("mp_article.yaml"))
    def test_mp_article(self,title,content,expect):
        # 调用发布文章业务
        self.mp_article.page_mp_publish_article(title,content)
        #       #获取结果信息
        info = self.mp_article.page_get_info()
        print("文章发布结果：",info)
        # 断言
        try:
            assert info == expect
        except Exception as e:
            log.error("发布文章错误原因",e)
            print("发表文章错误信息：", e)
            self.mp_article.base_get_image()
            raise
