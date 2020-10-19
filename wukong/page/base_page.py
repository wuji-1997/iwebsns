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
urldata =ReadExcel('登录页面')
class BasePage(object):


    def __init__(self,driver,url = urldata.getExcelValue(2,4)):

        self.base_url = url
        self.base_driver = driver


    def __open(self,test_url):
        """

        :param test_url:
        :return:
        """
        try:
            self.base_driver.get(test_url)
            self.base_driver.implicitly_wait(5)
        except Exception:
            base_log.name.exception(f'打开网址{test_url}失败')
            raise
        else:
            base_log.name.info(f'打开网址{test_url}成功')

    def open(self):
        """

        :return:
        """
        self.__open(self.base_url)
        base_log.name.info('登录网址成功')

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



    #窗口最大化
    def max_page(self):
        """

        :return:
        """
        self.base_driver.maximize_window()

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


    #输入值
    def input_value(self,loc,value):
        """
        定位元素后输入测试数据
        :param loc:
        :return:
        """
        element = self.get_element(*loc)
        try:
            element.send_keys(value)
        except Exception:
            base_log.name.exception(f'元素{loc}输入测试数据{value}失败')
            raise
        else:
            base_log.name.info(f'元素{loc}输入测试数据{value}成功')

    #点击元素
    def click_element(self,loc):
        """
        成功定位元素后在进行点击操作
        :param loc:
        :return:
        """
        element = self.get_element(*loc)
        try:
            element.click()
        except Exception as e:
            base_log.name.exception(f'点击元素{loc}失败')
            raise e
        else:
            base_log.name.info(f'点击元素{loc}成功')



    #处理下拉框
    def action_select(self,loc,value,select_value):
        """

        :param value:内嵌表单的id或者name属性
        :return:
        """
        element = self.get_element(*loc)
        try:
            if value=='1':
                Select(element).select_by_value(select_value)
            elif value=='2':
                Select(element).select_by_index(select_value)
            elif value == '3':
                Select(element).select_by_visible_text(select_value)

        except Exception:
            base_log.name.exception(f'{loc}不是selec属性下拉框')
            raise
        else:
            base_log.name.info(f'下拉框{loc}处理成功')

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
        try:
            assert test_url == self.get_url()
        except Exception:
            return False
        else:
            base_log.name.info(f'打开的网页{test_url}正确')
            return True


    #获取定位元素的文本值
    def get_element_value(self,*loc):
        """

        :param loc:
        :return:
        """
        element = self.get_element(loc)
        try:
            value = element.text

        except Exception:
            base_log.name.exception(f'元素{element}是不可见的获取文本值失败')
            raise
        else:
            base_log.name.info(f'获取元素{loc}文本值成功')
            return value

    #清空输入框
    def clear_value(self,*loc):
        """

        :param loc:
        :return:
        """
        element = self.get_element(loc)
        try:
            element.clear()
        except Exception:
            base_log.name.exception(f'元素{loc}文本值清除失败')
            raise
        else:
            base_log.name.info(f'元素{loc}文本值清除成功')

    #获取页面源码
    def getpagecode(self):
        """
        获取当前页面的源码
        :return:
        """
        value = self.base_driver.page_source
        base_log.name.info('获取当前页面源码成功')
        return value

    #断言目标字符串是否在页面源码中
    def assert_string(self, value):
        """

        :return:
        """
        try:
            assert value in self.getpagecode()
        except Exception:
            base_log.name.exception(f'{value} 不在当前页面中')
            raise
        else:
            base_log.name.info(f'{value} 在当前页面中 ')
    #断言页面是否存在提示框
    def assert_alert(self):
        """

        :return:
        """
        try:

            WebDriverWait(self.base_driver,10,0.5).until(EC.alert_is_present())
        except Exception:
            base_log.name.exception('当前页面不存在提示框')
        else:
            base_log.name.info('当前页面存在提示框')

    #点击提示框确认按钮
    def action_alert_yes(self):
        """

        :return:
        """
        try:
            find_alert  = self.base_driver.switch_to.alert()
            find_alert.accept()
        except Exception:
            base_log.name.exception('确认提示框失败')
            raise
        else:
            base_log.name.info('确认提示框成功')


    #点击处理框取消按钮
    def action_alert_no(self):
        """

        :return:
        """
        try:
            find_alert  = self.base_driver.switch_to.alert
            find_alert.dismiss()
        except Exception:
            base_log.name.exception('取消提示框失败')
            raise
        else:
            base_log.name.info('取消提示框成功')

    #向提示框输入值
    def input_alert_value(self,value):
        """

        :return:
        """
        try:
            find_alert  = self.base_driver.switch_to.alert
            find_alert.send_keys(value)
        except Exception:
            base_log.name.exception(f'向提示框输入值{value}失败')
            raise
        else:
            base_log.name.info(f'向提示框输入值{value}成功')

    #关闭浏览器
    def close_driver(self):
        """

        :return:
        """
        self.base_driver.quit()
        base_log.name.info('------------关闭浏览器成功--------------')
















if __name__=="__main__":

   from selenium import webdriver
   import time
   m = BasePage(webdriver.Chrome())
   m.open()
   m.input_value((By.NAME,'login_email'),value='113128804@qq.com')
   m.input_value((By.NAME,'login_pws'),value='wuji0121')
   m.click_element((By.NAME,'loginsubm'))
   time.sleep(10)

   if m.assert_string('登录帐号误，请重试'):
       print('wuji')

   else:
       print('l')

