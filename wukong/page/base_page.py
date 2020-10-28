from wukong.common.my_log import CRM_log
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from wukong.common.readexcel import ReadExcel
base_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)
class BasePage(object):


    def __init__(self,driver,url = "http://localhost/iwebsns/index.php"):

        self.base_url = url
        self.base_driver = driver


    def __open(self,test_url):
        """

        :param test_url:
        :return:
        """
        try:
            self.base_driver.get(test_url)
            self.base_driver.implicitly_wait(10)
        except Exception:
            base_log.name.exception(f'打开网址{test_url}失败')
            raise
        else:
            base_log.name.info(f'打开网址{test_url}成功')


    #打开浏览器
    def open(self):
        """

        :return:
        """
        self.__open(self.base_url)
        base_log.name.info('登录网址成功')

    # 窗口最大化
    def max_page(self):
        """

        :return:
        """
        self.base_driver.maximize_window()

    def get_element(self,*loc):
        """
        定位单个元素
        :param loc:
        :return:
        """
        try:
            WebDriverWait(self.base_driver,10,1).until(EC.visibility_of_element_located(loc))

        except Exception:
            base_log.name.exception(f'定位元素{loc}失败')
            raise
        else:
            base_log.name.info(f'定位元素{loc}成功')
            return self.base_driver.find_element(*loc)

    def get_elements(self,*loc):
        """
        定位一组元素
        :param loc:
        :return:
        """
        try:
            WebDriverWait(self.base_driver,10,1).until(EC.visibility_of_element_located(loc))
        except Exception:
            base_log.name.exception(f'定位元素{loc}失败')
            raise
        else:
            base_log.name.info(f'定位元素{loc}成功')
            return self.base_driver.find_elements(loc)

    #定位单个元素
    def find_element(self,nature,value):
        """
        定位单个元素
        :param nature: 选择定位方式的限制条件
        :param value: 元素属性表达式
        :return:
        """

        if nature=='id':
            element = (By.ID,value)
            try:
                WebDriverWait(self.base_driver, 10, 1).until(EC.visibility_of_element_located(element))

            except Exception:
                base_log.name.exception(f'定位元素 {element} 失败')
                raise
            else:
                base_log.name.info(f'定位元素 {element} 成功')
                return self.base_driver.find_element(*element)

        elif nature=='name':
            element = (By.NAME, value)
            try:
                WebDriverWait(self.base_driver, 10, 1).until(EC.visibility_of_element_located(element))

            except Exception:
                base_log.name.exception(f'定位元素 {element} 失败')
                raise
            else:
                base_log.name.info(f'定位元素 {element} 成功')
                return self.base_driver.find_element(*element)

        elif nature == 'class':
            element = (By.CLASS_NAME,value)
            try:
                WebDriverWait(self.base_driver, 10, 1).until(EC.visibility_of_element_located(element))

            except Exception:
                base_log.name.exception(f'定位元素 {element} 失败')
                raise
            else:
                base_log.name.info(f'定位元素 {element} 成功')
                return self.base_driver.find_element(*element)

        elif nature == 'link_text':
            element = (By.LINK_TEXT,value)
            try:
                WebDriverWait(self.base_driver, 10, 1).until(EC.visibility_of_element_located(element))

            except Exception:
                base_log.name.exception(f'定位元素 {element} 失败')
                raise
            else:
                base_log.name.info(f'定位元素 {element} 成功')
                return self.base_driver.find_element(*element)


        elif nature == 'xpath':
            element = (By.XPATH,value)
            try:
                WebDriverWait(self.base_driver, 10, 1).until(EC.visibility_of_element_located(element))

            except Exception:
                base_log.name.exception(f'定位元素 {element} 失败')
                raise
            else:
                base_log.name.info(f'定位元素 {element} 成功')
                return self.base_driver.find_element(*element)

        elif nature == 'css':
            element = (By.CSS_SELECTOR, value)
            try:
                WebDriverWait(self.base_driver, 10, 1).until(EC.visibility_of_element_located(element))

            except Exception:
                base_log.name.exception(f'定位元素 {element} 失败')
                raise
            else:
                base_log.name.info(f'定位元素{element}成功')
                return self.base_driver.find_element(*element)
        else:
            base_log.name.exception(f'“{nature}” 该操作元素的定位方式不在八种之中')


    #输入值
    def input_value(self, loc,element_value,test_value):
        """

        :param loc:
        :param element_value:
        :param test_value:
        :return:
        """


        element = self.find_element(nature=loc, value=element_value)
        try:
            element.send_keys(test_value)
        except Exception:
            base_log.name.exception(f'输入测试数据 “{test_value}” 失败')
            raise
        else:
            base_log.name.info(f'输入测试数据 “{test_value}” 成功')

    #清空输入框
    def clear_value(self,loc,element_value):
        """

        :param loc:
        :param element_value:
        :return:
        """

        element = self.find_element(nature=loc, value=element_value)
        try:
            element.clear()
        except Exception:
            base_log.name.exception(f'元素文本值清除失败')
            raise
        else:
            base_log.name.info(f'元素文本值清除成功')



    # 点击元素
    def click_element(self,loc,element_value):
        """
        定位元素后进行点击元素操作
        :param loc:
        :param element_value:
        :return:
        """

        element = self.find_element(nature=loc, value=element_value)
        try:
            element.click()
        except Exception as e:
            base_log.name.exception(f'点击元素失败')
            raise e
        else:
            base_log.name.info(f'点击元素成功')


    #强制等待
    def make_sleep(self,seconds):
        """

        :param seconds:
        :return:
        """
        try:
            import time
            time.sleep(seconds)

        except Exception as e:
            raise e
        else:
            base_log.name.info(f'现在开始需要强制等待{seconds}秒')


    #处理下拉框
    def action_select(self,loc,element_value,select_value):
        """

        :param loc:
        :param element_value:
        :param select_value:
        :return:
        """
        element = self.find_element(nature=loc, value=element_value)

        try:
            self.make_sleep(5)
            Select(element).select_by_visible_text(select_value)

        except Exception:
            base_log.name.exception('该元素不是 select 属性下拉框')
            raise
        else:
            base_log.name.info('下拉框处理成功')

    #表单切换
    def switch_frame(self,value):
        """

        :param value:表单的id或者name属性值
        :return:
        """
        try:
            self.base_driver.switch_to.frame(value)
        except Exception:
            base_log.name.exception("切换表单失败")
            raise
        else:
            base_log.name.info('切换表单成功')

    #返回上一层表单
    def switch_parentframe(self):
        """

        :param value:
        :return:
        """
        try:
            self.base_driver.switch_to.parent_frame()
        except Exception:
            base_log.name.exception("返回上一层表单失败")
            raise
        else:
            base_log.name.info('返回上一层表单成功')

    #切回最外层表单
    def switch_defaultcontent(self):
        """

        :return:
        """
        try:
            self.base_driver.switch_to.default_content()
        except Exception:
            base_log.name.exception("返回最外层表单失败")
            raise
        else:
            base_log.name.info('返回最外层表单成功')

    # 点击提示框确认按钮
    def action_alert_yes(self,loc,value):
        """

        :return:
        """
        element = self.base_driver.switch_to.alert
        try:
            element.accept()
        except Exception:
            base_log.name.exception(f'{element} 不是alert')
        else:
            base_log.name.info(f'{element} 是alert 处理成功')

    # 点击处理框取消按钮
    def action_alert_no(self):
        """

        :return:
        """
        element = self.base_driver.switch_to.alert
        try:
            element.dismiss()
        except Exception:
            base_log.name.exception(f'{element} 不是alert')
        else:
            base_log.name.info(f'{element} 是alert 处理成功')

    # 向提示框输入值
    def input_alert_value(self, value):
        """

        :return:
        """
        try:
            find_alert = self.base_driver.switch_to.alert
            find_alert.send_keys(value)
        except Exception:
            base_log.name.exception(f'向提示框输入值{value}失败')
            raise
        else:
            base_log.name.info(f'向提示框输入值{value}成功')

    # 获取定位元素的文本值
    def get_element_value(self, loc,element_value):
        """

        :param loc:
        :param element_value:
        :return:
        """
        element = self.find_element(nature=loc,value=element_value)
        try:
            value = element.text
        except Exception:
            base_log.name.exception(f'元素是不可见的获取文本值失败')
            raise
        else:
            base_log.name.info(f'获取元素文本值 {value} 成功')
            return value

    # 执行js脚本
    def js(self, js_value):

        try:
            self.base_driver.execute_script(js_value)
        except Exception:
            base_log.name.exception(f'执行jsp脚本{js_value}失败')
            raise
        else:
            base_log.name.info(f'执行jsp脚本{js_value}成功')

    #获取当前页面标题
    def get_title(self):
        """

        :return:
        """
        value = self.base_driver.title
        base_log.name.info(f'获取标题{value}成功')
        return value

    #断言标题
    def assert_title(self,test_title):
        """

        :param test_title:
        :return:
        """
        try:
            WebDriverWait(self.base_driver,10,0.5).until(EC.title_is(test_title))

        except Exception:
            return False
        else:
            return True

    #获取当前页面网址
    def get_url(self):
        """

        :return:
        """
        now_url = self.base_driver.current_url
        base_log.name.info(f'获取当前页面网址{now_url}成功')
        return now_url

    #断言当前页面网址
    def assert_url(self,test_url):
        """

        :param test_url:
        :return:
        """
        if test_url == self.get_url():
            base_log.name.info(f'{test_url} 与当前页面网址一致')
            return True
        else:
            base_log.name.exception(f'{test_url} 与当前页面网址不一致')
            return False

    #获取页面源码
    def getpagecode(self):
        """
        获取当前页面的源码
        :return:
        """
        value = self.base_driver.page_source
        base_log.name.info('获取当前页面源码成功')
        return value

    #判断目标字符串是否在页面源码中返回布尔值
    def assert_string(self, value):
        """

        :return:
        """
        if value in self.getpagecode():
            base_log.name.info(f'{value} 在当前页面')
            return True
        else:
            base_log.name.exception(f"{value} 不在当前页面")
            return False

    #断言页面是否存在提示框
    def assert_alert(self):
        """

        :return:
        """
        EC.alert_is_present()



    #关闭浏览器
    def close_driver(self):
        """

        :return:
        """
        self.base_driver.quit()
        base_log.name.info('------------关闭浏览器成功--------------')


    def new_js(self,js,jsvalue):
        """

        :param js:
        :param jsvalue:
        :return:
        """

        try:
            jsp = js
            self.base_driver.execute_script(jsp)
            jsp_value = jsvalue
            self.base_driver.execute_script(jsp_value)
        except Exception:
            base_log.name.exception(f'执行jsp脚本失败')
            raise
        else:
            base_log.name.info(f'执行jsp脚本成功')

















if __name__=="__main__":

   from selenium import webdriver
   driver = webdriver.Chrome()
   driver.implicitly_wait(10)
   driver.get('http://localhost/iwebsns/index.php')
   m = BasePage(driver)
   m.input_value('name','login_email','1131228804@qq.com')
   m.input_value('name','login_pws','wuji0121')
   m.click_element('name','loginsubm')
   m.click_element('class')




