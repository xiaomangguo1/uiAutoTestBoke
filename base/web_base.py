import math
from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base


class WebBase(Base):
    """以下为Web项目专属方法"""

    # 根据显示文本点击指定元素
    def web_base_click_element(self, placeholder_text, click_text):
        # 1、点击下拉框
        # loc = (By.CSS_SELECTOR, "[placeholder = '{}']".format(placeholder_text))
        loc =(By.CSS_SELECTOR,"#Editor_Edit_EditorBody_fontselect_text")
        self.base_click(loc)
        # 2、暂停
        sleep(1)  #暂停，因为是动态加载
        # 3、点击包含显示文本的 元素
        loc1 = (By.XPATH,"//*[text()='{}']".format(click_text))
        self.base_click(loc1)

    def web_switch_handle(self,title):
        # 切换到新窗口
        # 获取当前窗口句柄
        # current_handle = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if title == self.driver.title:
                break

        print('切换后的title：', self.driver.title)