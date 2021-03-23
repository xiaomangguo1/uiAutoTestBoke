from time import sleep

import page
from base.web_base import WebBase
from tools.get_logger import GetLogger

log = GetLogger().get_logger()
class PageMpArticle(WebBase):
    # 1、点击写博
    def page_click_write_boke(self):

        self.base_click(page.mp_write_boke_link)

    # 2、点击添加新随笔
    def page_click_add_content(self):
        sleep(5)
        # 切换到新窗口
        self.web_switch_handle("博客后台 - 博客园")

        self.base_click(page.mp_add_article_text)

    # 3、输入标题
    def page_input_title(self, value):
        sleep(1)
        self.base_input(page.mp_title, value)

    # 4、输入内容
    def page_input_content(self, value):
        # 切换iframe
        iframe = self.base_find_element(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        # 输入内容
        sleep(1)
        self.base_input(page.mp_content, value)
        # 回到主目录
        self.driver.switch_to.default_content()

    # 6、选择文字类型
    def page_click_word_type(self):
        # 调用WebBase封装方法
        sleep(1)
        self.web_base_click_element(placeholder_text="", click_text="幼圆")

    # 5、移动随笔
    def page_click_move_pic(self):
        sleep(1)
        self.base_click(page.mp_move_arcital)

    # 7、点击发布按钮
    def page_click_publish(self):
        sleep(1)
        self.base_click(page.mp_publish_btn)

    # 获取发表文章信息,测试层断言用
    def page_get_info(self):
        sleep(5)
        self.base_get_text(page.mp_article_result)

    # 组合发布文章业务方法
    def page_mp_publish_article(self,title,content):
        log.info("正在调用发布文章业务方法--标题{}".format(title))
        self.page_click_write_boke()
        self.page_click_add_content()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_word_type()
        self.page_click_move_pic()
        self.page_click_publish()
