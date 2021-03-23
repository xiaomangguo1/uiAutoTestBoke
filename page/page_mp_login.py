# 媒体登录
from time import sleep

import page
from base.base import Base
from base.web_base import WebBase
from tools.get_logger import GetLogger
# 初始化日志信息
log = GetLogger().get_logger()
# 子类没有定义__init__方法时，默认引用父类的__init__
class PageMpLogin(WebBase):
    # 输入用户名
    def page_input_username(self,username):
        # 调用父类输入方法
        self.base_input(page.mp_username,username)

    # 输入验证码
    def page_input_code(self,code):
        # 调用父类输入方法
        self.base_input(page.mp_code,code)

    # 点击登录
    def page_click_login_btn(self):
        # 调用父类点击方法
        self.base_click(page.mp_login_btn)

    # 获取昵称封装-->测试脚本层断言使用
    def page_get_nickname(self):
        # 调用父类获取文本方法
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法-->测试脚本层调用
    def page_mp_login(self,username,code):
        """提示:调用相同页面操作步骤，跨页面暂时不考虑"""
        log.info("正在调用自媒体登录业务方法，用户名{}，密码{}".format(username,code))
        # 输入用户名
        self.page_input_username(username)
        # 输入验证码
        self.page_input_code(code)
        sleep(1) #防止电脑加载太快
        # 点击登录
        self.page_click_login_btn()

    # 组合业务方法-->发布文章依赖使用
    def page_mp_login_success(self,username="小芒果香香",code="5776590XIAO"):
        """提示:调用相同页面操作步骤，跨页面暂时不考虑"""
        log.info("正在调用自媒体登录业务方法，用户名{}，密码{}".format(username,code))
        # 输入用户名
        self.page_input_username(username)
        # 输入验证码
        self.page_input_code(code)
        sleep(1) #防止电脑加载太快
        # 点击登录
        self.page_click_login_btn()

