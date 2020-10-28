from wukong.common.my_log import CRM_log
from selenium import webdriver
import logging
from wukong.page.base_page import BasePage
from wukong.common.readexcel import ReadExcel
blog_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)
from selenium.webdriver.common.by import By

read_blog = ReadExcel('日志页面')

class Blog_page(BasePage):

    blog_button = (read_blog.getExcelValue(1,3),read_blog.getExcelValue(1,4))             #点击日志按钮
    switchid = read_blog.getExcelValue(2,4)                                              #切换日志的内置表单
    newblog = (read_blog.getExcelValue(3,3),read_blog.getExcelValue(3,4))                 #点击新建日志按钮
    title = (read_blog.getExcelValue(4,3),read_blog.getExcelValue(4,4),read_blog.getExcelValue(4,5))  #输入日志标题
    blog_select = (read_blog.getExcelValue(5,3),read_blog.getExcelValue(5,4),read_blog.getExcelValue(5,5))   #操作默认分类下拉框
    add_list = (read_blog.getExcelValue(6,3),read_blog.getExcelValue(6,4))  #点击添加分类
    new_list = (read_blog.getExcelValue(7,3),read_blog.getExcelValue(7,4),read_blog.getExcelValue(7,5))  #输入新的分类
    hold_button = (read_blog.getExcelValue(8,3),read_blog.getExcelValue(8,4))  #点击保存按钮
    cancel_button = (read_blog.getExcelValue(9,3),read_blog.getExcelValue(9,4))  #点击取消按钮
    bolg_tag = (read_blog.getExcelValue(10,3),read_blog.getExcelValue(10,4),read_blog.getExcelValue(10,5))  #输入日志标签
    power = (read_blog.getExcelValue(11,3),read_blog.getExcelValue(11,4))  #点击设置访问权限按钮
    myself = (read_blog.getExcelValue(12,3),read_blog.getExcelValue(12,4))  #点击仅自己查看
    friend = (read_blog.getExcelValue(13,3),read_blog.getExcelValue(13,4))  #点击好友可以查看
    powerhold = (read_blog.getExcelValue(14,3),read_blog.getExcelValue(14,4))  #点击选择访问权限确认按钮
    powercacel=(read_blog.getExcelValue(15,3),read_blog.getExcelValue(15,4))   #点击选择访问权限取消按钮
    switchid2 =read_blog.getExcelValue(16,4)
    blog_msg = (read_blog.getExcelValue(17,3),read_blog.getExcelValue(17,4),read_blog.getExcelValue(17,5))  #输入日志内容
    photo_select = (read_blog.getExcelValue(19,3),read_blog.getExcelValue(19,4))  #操作选择相册下拉框
    new_create = (read_blog.getExcelValue(20,3),read_blog.getExcelValue(20,4))  #点击确认新建日志按钮
    clicknewblog = (read_blog.getExcelValue(22,3),read_blog.getExcelValue(22,4))  #点击新建的日志
    deletebutton = (read_blog.getExcelValue(23,3),read_blog.getExcelValue(23,4),read_blog.getExcelValue(23,5))  #删除新建的日志
    update = (read_blog.getExcelValue(24,3),read_blog.getExcelValue(24,4))  #更新新建的日志
    update_tag = (read_blog.getExcelValue(25,3),read_blog.getExcelValue(25,4),read_blog.getExcelValue(25,5))  #编辑页面标签
    blogreply =(read_blog.getExcelValue(26,3),read_blog.getExcelValue(26,4),read_blog.getExcelValue(26,5))
    replybutton = (read_blog.getExcelValue(27,3),read_blog.getExcelValue(27,4))

    def intoform(self):
        """
        进入新建日志内置表单
        :return:
        """
        self.click_element(self.blog_button[0],self.blog_button[1])
        self.switch_frame(self.switchid)

    def create_new_blog(self):
        """
        新建日志
        :return:
        """
        self.intoform()
        self.click_element(self.newblog[0],self.newblog[1])   #点击新建日志按钮
        self.input_value(self.title[0],self.title[1],self.title[2])  #输入新建的日志标题
        self.click_element(self.add_list[0],self.add_list[1])     #点击添加新的分类按钮
        self.input_value(self.new_list[0],self.new_list[1],self.new_list[2])  #输入新的分类
        self.click_element(self.hold_button[0],self.hold_button[1])    #点击保存按钮
        self.make_sleep(10)
        self.action_select(self.blog_select[0],self.blog_select[1],select_value=self.blog_select[2])  #选择日志分类
        self.input_value(self.bolg_tag[0],self.bolg_tag[1],self.bolg_tag[2])  #输入新建的日志标签
        self.click_element(self.power[0],self.power[1])                       #点击设置访问权限按钮
        self.click_element(self.myself[0],self.myself[1])                    #设置为仅自己看见
        self.click_element(self.powerhold[0],self.powerhold[1])              ##点击选择访问权限确认按钮
        self.switch_frame(self.switchid2)
        self.input_value(self.blog_msg[0],self.blog_msg[1],self.blog_msg[2])  #输入新建的日志内容
        self.switch_parentframe()
        self.click_element(self.new_create[0],self.new_create[1])      ##点击新建的日志

    def into_blog_page(self):
        """

        :return:
        """
        self.intoform()
        self.click_element(self.clicknewblog[0], self.clicknewblog[1])




    def delete_blog(self):
        """
        删除日志功能
        :return:
        """
        self.into_blog_page()
        self.click_element(self.deletebutton[0], self.deletebutton[1])
        self.action_alert_yes()

    def update_blog(self):
        """
        更新日志
        :return:
        """
        self.into_blog_page()
        self.click_element(self.update[0],self.update[1])
        self.clear_value(self.update_tag[0],self.update_tag[1])
        self.input_value(self.update_tag[0],self.update_tag[1],self.update_tag[2])
        self.click_element(self.new_create[0],self.new_create[1])

    def reply_blog(self):
        """
        回复日志功能
        :return:
        """
        self.into_blog_page()
        self.input_value(self.blogreply[0],self.blogreply[1],self.blogreply[2])
        self.click_element(self.replybutton[0],self.replybutton[1])



if __name__ == "__main__":
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.common.alert import Alert
    from selenium.webdriver.support.ui import  WebDriverWait
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost/iwebsns/index.php")
    driver.find_element_by_name('login_email').send_keys('1131228804@qq.com')
    driver.find_element_by_name('login_pws').send_keys('wuji0121')
    driver.find_element_by_name('loginsubm').click()
    driver.find_element_by_class_name('app_vote').click()
    driver.switch_to.frame(0)
    driver.find_element_by_link_text('1').click()
    driver.find_element_by_link_text('删除本投票').click()
    result = WebDriverWait(driver,10,1).until(ec.alert_is_present())

    if result:
        print(result.text)
        result.accept()
    else:
        print("alert未弹出")

        driver.switch_to.default_content()
        driver.find_element_by_css_selector('#_DialogTable_0 > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(5) > td > input:nth-child(1)').click()








    