
import os

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
# from tools.get_log import get_logging
# log = get_logging()
from config import BASE_PATH
from tools.get_logger import GetLogger

# 单例模式
log = GetLogger().get_logger()


class Base:
    # 初始化方法
    def __init__(self, driver):
        log.info("正在初始化driver{}".format(driver))
        self.driver = driver

    # 定位元素方法
    # 单星号（ * ）：*agrs
    # 将所有参数以元组(tuple)
    # 的形式导入：
    def base_find_element(self, loc, timeout=30, poll=0.5):
        """
        :param loc:格式为列表或元祖，内容:元素定位信息使用By类
        :param timeout:查找元素超时时间，默认30秒
        :param poll:查找元素频率默认为0.5
        :return:元素
        """
        log.info("正在查找元素:{}".format(loc))
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))

    # 点击元素方法

    def base_click(self, loc):
        """
        :param loc: 元素定位信息
        """
        log.info("正在点击元素:{}".format(loc))
        self.base_find_element(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        """
        :param loc: 元素定位信息
        :param value:输入的值
        """
        log.info("正在给元素:{}，输入内容{}".format(loc, value))
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        log.info("正在给元素{}在清空".format(loc))
        # 输入
        el.send_keys(value)
        log.info("正在给元素:输入内容{}".format(value))

    # 获取文本方法
    def base_get_text(self, loc):
        """
        :param loc: 元素定位信息
        :return:返回元素文本值
        """
        log.info("正在获取元素文本:{}".format(self.base_find_element(loc).text))
        return self.base_find_element(loc).text

    # 鼠标悬停
    def base_move_to_link(self, loc):
        """
        :param loc: 元素定位信息
        """
        log.info("正在鼠标悬停:{}".format(loc))
        ActionChains(self.driver).move_to_element(self.base_find_element(loc)).perform()

    # 截图方法
    def base_get_image(self):
        log.error("断言出错，正在截图操作...")
        # 调用截图方法
        screen_path = BASE_PATH + os.sep + "image" + os.sep + "error.png"
        self.driver.get_screenshot_as_file(screen_path)
        # 调用图片写入报告方法
        self.__base_write_img(screen_path)

    # 将图片写入报告方法(私有)
    def __base_write_img(self,screen_path):
        # 获取图片文件流
        with open(screen_path, "rb") as f:
            # 调用allure.attach附加方法
            allure.attach(f.read(),"错误图片截图",allure.attachment_type.PNG)


    # 判断元素是否存在
    def base_element_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            log.info("判断元素{}存在".format(loc))
            # 找到元素
            return True
        except:
            # 没找到元素
            log.info("判断元素{}不存在！".format(loc))
            return False
