from wukong.common.my_log import CRM_log
from selenium import webdriver
import logging
from wukong.page.base_page import BasePage
from wukong.common.readexcel import ReadExcel
sharp_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)
from selenium.webdriver.common.by import By

read_share = ReadExcel('分享页面')

class Sharp_page(BasePage):

    share_button=(read_share.getExcelValue(1,3),read_share.getExcelValue(1,4))
    clear_input = (read_share.getExcelValue(2,3),read_share.getExcelValue(2,4))
    share_input = (read_share.getExcelValue(3,3),read_share.getExcelValue(3,4),read_share.getExcelValue(3,5))
    click_share = (read_share.getExcelValue(4,3),read_share.getExcelValue(4,4))

    share_title = (read_share.getExcelValue(6,3),read_share.getExcelValue(6,4),read_share.getExcelValue(6,5))
    sharetag = (read_share.getExcelValue(7,3),read_share.getExcelValue(7,4),read_share.getExcelValue(7,5))
    share_msg = (read_share.getExcelValue(8,3),read_share.getExcelValue(8,4),read_share.getExcelValue(8,5))

    click_button=(read_share.getExcelValue(9,3),read_share.getExcelValue(9,4))
    cancel = (read_share.getExcelValue(10,3),read_share.getExcelValue(10,4))
    deteleshare = (read_share.getExcelValue(11,3),read_share.getExcelValue(11,4))




    def intoshareform(self):
        """

        :return:
        """
        self.click_element(self.share_button[0],self.share_button[1])
        self.switch_frame(0)

    def new_share(self):
        """

        :return:
        """
        self.intoshareform()
        self.clear_value(self.clear_input[0],self.clear_input[1])
        self.input_value(self.share_input[0],self.share_input[1],self.share_input[2])
        self.click_element(self.click_share[0],self.click_share[1])
        self.make_sleep(30)
        self.switch_defaultcontent()
        self.input_value(self.share_title[0],self.share_title[1],self.share_title[2])
        self.input_value(self.sharetag[0],self.sharetag[1],self.sharetag[2])
        self.input_value(self.share_msg[0],self.share_msg[1],self.share_msg[2])
        self.click_element(self.click_button[0],self.click_button[1])

    def delete_share(self):
        """

        :return:
        """
        self.intoshareform()
        self.click_element(self.deteleshare[0],self.deteleshare[1])

if __name__=="__main__":
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost/iwebsns/index.php")
    driver.find_element_by_name('login_email').send_keys('1131228804@qq.com')
    driver.find_element_by_name('login_pws').send_keys('wuji0121')
    driver.find_element_by_name('loginsubm').click()
    driver.find_element_by_class_name('app_share').click()
    driver.switch_to.frame('frame_content')
    element = driver.find_element_by_id('add_outer_share')
    element.clear()
    element.send_keys('http://www.baidu.com')
    driver.find_element_by_class_name('share_button').click()
    driver.find_element_by_xpath('//*[@id="tag"]').send_keys('wuji')
    driver.find_element_by_id('share_com').send_keys('wuji')
    driver.find_element_by_xpath('//*[@id="_ButtonOK_0"]').click()