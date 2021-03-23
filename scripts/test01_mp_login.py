from time import sleep

import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_logger import GetLogger
from tools.read_yaml import read_yaml

# 初始化日志
log = GetLogger().get_logger()
class TestMpLogin:
    # 初始化

    def setup_class(self):
        # 1、获取driver
        driver = GetDriver().get_web_driver(page.url_mp)
        # 2、通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("username,code,expect", read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, code, expect):
        # 调用登录方法
        self.mp.page_mp_login(username, code)
        # 断言
        sleep(3)  # 解决 还未跳转到成功页面，获取昵称错误的问题
        try:
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            log.error("自媒体登录断言出错，错误信息 ：{}".format(e))
            print("错误的原因：", e)
            #截图
            self.mp.base_get_image()
            # 抛异常
            raise
