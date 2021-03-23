from selenium.webdriver.common.by import By

"""以下数据为自媒体 、后台的 url"""
# 自媒体url
url_mp = "https://account.cnblogs.com/signin"  # "https://dsshop.csdeshang.com/home/Login/login.html"
# 后台url
url_msi = "https://dsshop.csdeshang.com/admin/Login/index.html"
"""以下数据为自媒体模块数据"""
# 用户名
mp_username = (By.CSS_SELECTOR, "#mat-input-0")  # (By.CSS_SELECTOR, "#member_name")
# 验证码
mp_code = (By.CSS_SELECTOR, "#mat-input-1")  # (By.CSS_SELECTOR, "#member_password")
# 昵称
mp_nickname = (By.CSS_SELECTOR, "div#header_user_right>a:nth-child(2)")  # (By.CSS_SELECTOR, "ul.login-regin li.line a")
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, ".action-button")  # (By.CSS_SELECTOR, ".login-btn")

"""发布文章"""
# 写博链接
mp_write_boke_link = (By.LINK_TEXT, "写博")
# 添加新随笔链接,不能选span,必须选a
mp_add_article_text = By.XPATH, "//span[text()='添加新随笔']/.."
# 添加文字标题
mp_title = By.CSS_SELECTOR, "#post-title"
# iframe
mp_iframe = By.CSS_SELECTOR, "#Editor_Edit_EditorBody_ifr"
# 添加内容,文章内容，定位到body,勿定位到p
mp_content = By.CSS_SELECTOR, "#tinymce"

# 移动随笔
mp_move_arcital = By.XPATH, "//span[text()='文章']"
# 发布
mp_publish_btn = By.XPATH, "//button[contains(text(),'发布')]"
# 结果信息
mp_article_result = By.XPATH, "//*[contains(text(),'操作成功')]"

"""以下为app应用元素配置信息"""
# 包名
appPackage = "com.cnblogs.xamarinandroid"
# 启动名
appActivity = "crc64c2c99c61e0e508d5.MainActivity"
# 启动名
# 手机号
app_phone = By.XPATH, "//*[ @index='1' and @class= 'android。widget.EditText']"
# 验证码
app_code = By.XPATH, "//*[@index='2' and @class= 'android.widget.EditText']"
# 登录
app_login_btn = By.XPATH, "//*[@text='登录' and @class='android.widget.Button'"
"""登录信息没做暂放"""
# 博客底部页签
app_boke = By.XPATH,"//*[@index='0' and contains(@content-text,'博客')]"
#频道区域
app_channel_area = By.XPATH,"//*[@class='android.widget.HorizontalScrollView']"
# 文章区域
app_article=By.XPATH,"//*[@class ='android.support.v7.widget.RecyclerView' and @bounds='[0,532][1440,2560]']"


