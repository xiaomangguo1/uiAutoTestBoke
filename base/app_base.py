from time import sleep

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import page
from base.base import Base
from tools.get_logger import GetLogger

log = GetLogger().get_logger()


class AppBase(Base):
    # 查找页面是否有指定元素
    def app_base_is_exists(self, loc):

        try:
            # 调用查找方法->3
            self.base_find_element(loc, timeout=3)
            log.info("在app找到指定元素--{}".format(loc))
            # 返回信息
            print("找到-->元素{}")
            return True
        except Exception as e:
            log.error("app未找到指定元素--{}".format(loc))
            print("未找到-->元素{}")
            return False

    # 2.从右向左滑动屏幕
    def app_base_right_wipe_left(self, click_text):
        """

        :param loc_area: 区域元素定位信息
        :param click_text: 点击文本
        :return:
        """
        log.info("正在调用从右到左的滑动方法")
        # 1.查找区域元素
        el = self.base_find_element(page.app_channel_area)
        # 2.获取区域元素的位置y坐标点
        y = el.location.get("y")
        # 3.获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 4.计算start_X，starty,end_X,end_y
        start_x = width * 0.8
        start_y = y + y * 0.5
        end_x = width * 0.2
        end_y = y + y * 0.5
        # 组合频道元素配置信息android.widget.LinearLayout
        # loc = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']//*[contains(@text,'{}')]".format(click_text)
        loc = By.XPATH, "//android.widget.HorizontalScrollView//*[contains(@text,'{}')]".format(click_text)
        #       #循环操作
        while True:
            # 获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 捕获异常
            try:
                # 1、查找元素
                el = self.base_find_element(loc, timeout=3)
                # 2、输出提示信息
                print("找到元素{}啦".format(loc))
                # 3、点击元素
                self.base_click(loc)
                # 4、跳出循环
                break
            # 处理异常
            except:
                # 输出提示信息
                print("未找到元素{}".format(loc))
                # 没找到就滑动屏幕
                self.driver.swipe(start_x,start_y,end_x,end_y,duration=2000)
                # 判断是否最后一页
                if page_source == self.driver.page_source:
                    # 输出提示信息
                    print("滑到最后一页，未找到元素")
                    # 抛出未找到元素异常
                    raise NoSuchElementException

    # 3.从下向上滑动屏幕
    def app_base_down_wipe_up(self, click_text):
        """

        :param loc_area: 区域元素定位信息
        :param click_text: 点击文本
        :return:
        """
        log.info("正在调用从下到上的滑动方法")
        # 1.查找区域元素
        el = self.base_find_element(page.app_article)
        # 2.获取区域元素的位置y坐标点
        y = el.location.get("y")
        # 3.获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 4.计算start_X，starty,end_X,end_y
        start_x = width * 0.5
        start_y =y * 0.8
        end_x = width * 0.5
        end_y = y * 0.2
        # 组合文章元素配置信息android.widget.LinearLayout
        loc = By.XPATH, "//*[@index='0' and @bounds='[12,552][1428,1128]']//*[contains(@text,'{}')]".format(click_text)

        #循环操作
        while True:
            # 获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 捕获异常
            try:
                sleep(5)
                # 1、查找元素
                el = self.base_find_element(loc, timeout=3)
                # 2、输出提示信息
                print("找到元素{}啦".format(loc))
                sleep(2)
                # 3、点击元素
                self.base_click(loc)
                # 4、跳出循环
                break
            # 处理异常
            except:
                # 输出提示信息
                print("未找到元素{}".format(loc))
                # 没找到就滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
                # 判断是否最后一页
                if page_source == self.driver.page_source:
                    # 输出提示信息
                    print("滑到最后一页，未找到元素")
                    # 抛出未找到元素异常
                    raise NoSuchElementException