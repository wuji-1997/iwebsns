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
    clickelement = (By.NAME,data.getExcelValue(8,3))  #点击登录按钮
    email = (By.NAME,data.getExcelValue(4,3))         #用户名元素
    password = (By.NAME,data.getExcelValue(6,3))      #密码元素
    loginout = (By.LINK_TEXT,data.getExcelValue(8,3)) #登陆后退出登录按钮

    #测试数据
    test_date = [data.getExcelValue(4,4),             #正确的用户名
                 data.getExcelValue(5,4),             #错误的用户名
                 data.getExcelValue(2,4),             #登录网址
                 data.getExcelValue(6,4),             #正确的密码
                 data.getExcelValue(7,4),             #错误的密码
                 data.getExcelValue(9,4)]             #登陆后页面网址



    #点击登录按钮
    def clickbotton(self):
        """

        :return:
        """
        self.click_element(self.clickelement)
        login_log.name.info('点击登录成功---loding')

    def clear_email(self):
        """
        清楚用户名输入框数据
        :return:
        """
        self.clear_value(self.email)

    def clear_password(self):
        """
        清除密码数据
        :return:
        """
        self.click_element(self.password)


    def login(self,user='1131228804@qq.com',password='wuji0121'):
        """

        :param login_email:
        :param login_password:
        :return:
        """
        self.input_value(self.email,user)
        self.input_value(self.password,password)
        self.clickbotton()

    def login_out(self):
        """
        退出登录
        :return:
        """
        self.click_element(self.loginout)
        login_log.name.info('-------quit---------')

if __name__=='__main__':
    pass
