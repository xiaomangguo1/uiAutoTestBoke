from time import sleep

import page
from base.app_base import AppBase
from tools.get_logger import GetLogger

log = GetLogger().get_logger()
class PageAppLogin(AppBase):
    # 1.输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.app_phone, phone)

    # 2.输入验证码
    def page_inputcode(self, code):
        self.base_input(page.app_code, code)
        pass

    # 3.点击登录按钮
    def page_click_login_btn(self):
        # 建议等待1-2秒
        sleep(2)
        self.base_click(page.app_login_btn)

    # 4.判断页面是否存在‘博客’菜单
    def page_is_login_success(self, loc):
        self.app_base_is_exists(loc)

    # 5.组合登录业务方法
    def page_app_login(self,phone,code):
        log.info("正在调用app应用登录方法，手机号{}，验证码{}".format(phone,code))
        self.page_input_phone(phone)
        self.page_inputcode(code)
        self.page_click_login_btn()

    # 5.组合登录成功依赖业务方法
    def page_app_login_success(self, phone="13666666", code="77777"):
        log.info("正在调用app应用登录方法，手机号{}，验证码{}".format(phone, code))
        self.page_input_phone(phone)
        self.page_inputcode(code)
        self.page_click_login_btn()