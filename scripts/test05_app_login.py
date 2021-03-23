import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_logger import GetLogger
from tools.read_yaml import read_yaml

log = GetLogger().get_logger()


class TestAppLogin:
    # 初始化

    def setup_class(self):
        # 获取driver
        app_driver = GetDriver().get_app_driver()
        # 获取PageAppLogin对象
        self.app_login = PageIn(app_driver).page_get_PageAppLogin()

    def teardown_class(self):
        # 关闭driver
        GetDriver().quit_app_driver()

    # 测试app登录类
    @pytest.mark.parametrize("phone,code",read_yaml("app_login.yaml"))
    def test_app_login(self,phone,code):
        # 调用登录类
        self.app_login.page_app_login(phone, code)
        # 调试断言
        try:
            assert self.app_login.page_is_login_success(page.app_boke)
        except Exception as e:
            print("app登录失败-->", e)
            # 日志
            log.error("登录失败,失败原因----->", e)
            #           #截图
            self.app_login.base_get_image()
            # 抛异常
            raise
