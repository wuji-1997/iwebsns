from wukong.common.my_log import CRM_log
from selenium import webdriver
import logging
from wukong.page.base_page import BasePage
from wukong.common.readexcel import ReadExcel
blog_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)
from selenium.webdriver.common.by import By

read_event = ReadExcel('活动页面')

class Event_page(BasePage):

    event_button = (read_event.getExcelValue(1,3),read_event.getExcelValue(1,4))  #活动按钮
    newevent = (read_event.getExcelValue(32,3),read_event.getExcelValue(32,4))  #点击发起活动
    event_name = (read_event.getExcelValue(2,3),read_event.getExcelValue(2,4),read_event.getExcelValue(2,5))#活动名称
    s1 =(read_event.getExcelValue(3,3),read_event.getExcelValue(3,4),read_event.getExcelValue(3,5))  #省份
    s2 = (read_event.getExcelValue(4,3),read_event.getExcelValue(4,4),read_event.getExcelValue(4,5))#城市
    event_address = (read_event.getExcelValue(5,3),read_event.getExcelValue(5,4),read_event.getExcelValue(5,5)) #活动地点
    start_jsp = read_event.getExcelValue(6,5)  #开始时间jsp
    end_jsp = read_event.getExcelValue(7,5)    #结束时间jsp
    deadline = read_event.getExcelValue(8,5)   #截止时间jsp
    start_time = (read_event.getExcelValue(9,3),read_event.getExcelValue(9,4),read_event.getExcelValue(9,5)) #活动开始时间
    end_time =(read_event.getExcelValue(10,3),read_event.getExcelValue(10,4),read_event.getExcelValue(10,5))  #活动结束时间
    deadline_time = (read_event.getExcelValue(11,3),read_event.getExcelValue(11,4),read_event.getExcelValue(11,5))#活动截止时间
    select1 =(read_event.getExcelValue(12,3),read_event.getExcelValue(12,4),read_event.getExcelValue(12,5))  #活动分类下拉框处理
    form1 = read_event.getExcelValue(15,5)
    from2 = read_event.getExcelValue(16,5)

    money_msg = (read_event.getExcelValue(17,3),read_event.getExcelValue(17,4),read_event.getExcelValue(17,5)) #输入费用说明
    adress_msg = (read_event.getExcelValue(18,3),read_event.getExcelValue(18,4),read_event.getExcelValue(18,5)) #输入集合地点
    clothes_msg = (read_event.getExcelValue(19,3),read_event.getExcelValue(19,4),read_event.getExcelValue(19,5)) #输入着装要求
    phone_msg = (read_event.getExcelValue(20,3),read_event.getExcelValue(20,4),read_event.getExcelValue(20,5)) #输入联系方式
    ation_msg = (read_event.getExcelValue(21,3),read_event.getExcelValue(21,4),read_event.getExcelValue(21,5)) #输入注意事项
    newspaper = (read_event.getExcelValue(23,3),read_event.getExcelValue(23,4),read_event.getExcelValue(23,5)) #上传活动海报
    public = (read_event.getExcelValue(24,3),read_event.getExcelValue(24,4),read_event.getExcelValue(24,5)) #活动隐私下拉框处理
    verify = (read_event.getExcelValue(25,3),read_event.getExcelValue(25,4))  #选择参加活动需要审批
    event_msg = (read_event.getExcelValue(26,3),read_event.getExcelValue(26,4),read_event.getExcelValue(26,5)) #输入活动信息
    sumbit = (read_event.getExcelValue(27,3),read_event.getExcelValue(27,4)) #点击提交按钮
    cancel = (read_event.getExcelValue(28,3),read_event.getExcelValue(28,4)) #点击取消活动按钮
    manage = (read_event.getExcelValue(29,3),read_event.getExcelValue(29,4)) #点击管理活动按钮
    clear_name = (read_event.getExcelValue(30,3),read_event.getExcelValue(30,4))  #清楚活动名称文本框


    def intoevntform(self):
        """
        进入活动内置表单
        :return:
        """
        self.click_element(self.event_button[0],self.event_button[1])
        self.switch_frame(0)


    def new_event(self):
        """

        :return:
        """
        self.intoevntform()
        self.click_element(self.newevent[0],self.newevent[1])
        self.input_value(self.event_name[0],self.event_name[1],self.event_name[2])
        self.action_select(self.s1[0],self.s1[1],self.s1[2])
        self.action_select(self.s2[0],self.s2[1],self.s2[2])
        self.input_value(self.event_address[0],self.event_address[1],self.event_address[2])
        self.js(self.start_jsp)
        self.input_value(self.start_time[0],self.start_time[1],'2020-10-27 22:30')
        self.js(self.end_jsp)
        self.input_value(self.end_time[0],self.end_time[1],'2020-10-29 22:30')
        self.js(self.deadline)
        self.input_value(self.deadline_time[0],self.deadline_time[1],'2020-10-28 22:30')
        self.action_select(self.select1[0],self.select1[1],self.select1[2])
        #self.switch_defaultcontent()
        self.action_alert_yes()
        self.input_value(self.newspaper[0],self.newspaper[1],self.newspaper[2])
        self.action_select(self.public[0],self.public[1],self.public[2])
        self.input_value(self.event_msg[0],self.event_msg[1],self.event_msg[2])
        self.click_element(self.sumbit[0],self.sumbit[1])


    def cancel_event(self):
        """

        :return:
        """
        self.intoevntform()
        self.click_element(self.cancel[0],self.cancel[1])



if __name__=='__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost/iwebsns/index.php")
    driver.find_element_by_name('login_email').send_keys('1131228804@qq.com')
    driver.find_element_by_name('login_pws').send_keys('wuji0121')
    driver.find_element_by_name('loginsubm').click()
    driver.find_element_by_class_name('app_event').click()
    driver.switch_to.frame(0)
    driver.find_element_by_link_text('取消活动').click()







    