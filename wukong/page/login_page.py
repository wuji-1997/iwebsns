from wukong.common.my_log import CRM_log
from selenium import webdriver
import logging
from wukong.page.base_page import BasePage
from wukong.common.readexcel import ReadExcel
login_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)
from selenium.webdriver.common.by import By
data = ReadExcel('登录页面')


class LoginPage(BasePage):
    #元素定位
    clickelement = (data.getExcelValue(8,3),data.getExcelValue(8,4))  #点击登录按钮
    email = (data.getExcelValue(4,3),data.getExcelValue(4,4))         #用户名元素
    password = (data.getExcelValue(6,3),data.getExcelValue(6,4))      #密码元素
    loginout = (data.getExcelValue(10,3),data.getExcelValue(10,4)) #登陆后退出登录按钮

    #测试数据
    test_date = [data.getExcelValue(4,5),             #正确的用户名
                 data.getExcelValue(5,5),             #错误的用户名
                 data.getExcelValue(2,5),             #登录网址
                 data.getExcelValue(6,5),             #正确的密码
                 data.getExcelValue(7,5),             #错误的密码
                 data.getExcelValue(9,5)]             #登陆后页面网址



    #点击登录按钮
    def clickbotton(self):
        """

        :return:
        """
        self.click_element(self.clickelement[0],self.clickelement[1])
        login_log.name.info('正在登录中===================================================')

    def clear_email(self):
        """
        清楚用户名输入框数据
        :return:
        """
        self.clear_value(self.email[0],self.email[1])

    def clear_password(self):
        """
        清除密码数据
        :return:
        """
        self.click_element(self.password[0],self.password[1])


    def login(self,user='1131228804@qq.com',pws ='wuji0121'):
        """
        :param login_email:
        :param login_password:
        :return:
        """
        self.input_value(self.email[0],self.email[1],test_value=user)
        self.input_value(self.password[0],self.password[1],test_value=pws)
        self.clickbotton()


    def login_out(self):
        """
        退出登录
        :return:
        """
        self.click_element(self.loginout[0],self.loginout[1])
        login_log.name.info('-------正在退出中---------')

if __name__=='__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.find_elements_by_css_selector()
    login = LoginPage(driver)
    login.open()
    login.login()

