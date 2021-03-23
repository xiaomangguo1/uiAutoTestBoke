from time import sleep

from selenium import webdriver
# 导入app包
import appium.webdriver

import page


class GetDriver:
    # 声明变量
    __web_driver = None
    # 声明appdriver变量
    __app_driver = None

    # 获取webdriver
    @classmethod
    def get_web_driver(cls, url):
        if cls.__web_driver is None:
            # 初始化实例化对象
            cls.__web_driver = webdriver.Chrome()
            # 浏览器最大化
            cls.__web_driver.maximize_window()
            # 打开网页
            cls.__web_driver.get(url)
        return cls.__web_driver

    # 获取appdriver
    @classmethod
    def get_app_driver(cls):
        # 判断__app_driver是否为空
        if cls.__app_driver == None:
            # 获取设置
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = '192.168.241.102:5555'
            desired_caps['appPackage'] = page.appPackage
            desired_caps['appActivity'] = page.appActivity
            cls.__app_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            #adb shell am start -W -n com.cnblogs.xamarinandroid/crc64c2c99c61e0e508d5.MainActivity

        return cls.__app_driver

    # 退出driver
    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver:
            cls.__web_driver.quit()
            # 注意：此处有坑
            cls.__web_driver = None

    # 退出appdriver
    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None

if __name__ == '__main__':
    GetDriver().get_app_driver()
    sleep(5)
    GetDriver().quit_app_driver()