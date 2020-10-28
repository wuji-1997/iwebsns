from wukong.common.my_log import CRM_log
from selenium import webdriver
import logging
from wukong.page.base_page import BasePage
from wukong.common.readexcel import ReadExcel
sharp_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)
from selenium.webdriver.common.by import By

read_group = ReadExcel('群组页面')


class Group_page(BasePage):
    gruop_button = (read_group.getExcelValue(1,3),read_group.getExcelValue(1,4))   #点击分组按钮
    create_group = (read_group.getExcelValue(2,3),read_group.getExcelValue(2,4))    #点击创建群组
    gruopname = (read_group.getExcelValue(3,3),read_group.getExcelValue(3,4),read_group.getExcelValue(3,5))             #输入群组名称
    groupresume = (read_group.getExcelValue(4,3),read_group.getExcelValue(4,4),read_group.getExcelValue(4,5)) #输入群组介绍
    handle_jointype = (read_group.getExcelValue(5,3),read_group.getExcelValue(5,4),read_group.getExcelValue(5,5))  #操作加入方式下拉框
    grouptag = (read_group.getExcelValue(6,3),read_group.getExcelValue(6,4),read_group.getExcelValue(6,5)) #输入群组标签
    handle_typeid=(read_group.getExcelValue(7,3),read_group.getExcelValue(7,4),read_group.getExcelValue(7,5))  #操作群组分类下拉框
    gruop_logo = (read_group.getExcelValue(8,3),read_group.getExcelValue(8,4),read_group.getExcelValue(8,5))  #上传群组logo
    confirm = (read_group.getExcelValue(9,3),read_group.getExcelValue(9,4))    #点击确认创建分组按钮
    searchgroup = (read_group.getExcelValue(11,3),read_group.getExcelValue(11,4))#点击搜索群组按钮
    input_searchgroup=(read_group.getExcelValue(12,3),read_group.getExcelValue(12,4),read_group.getExcelValue(12,5))  #输入搜索的群组名称
    click_confirm = (read_group.getExcelValue(13,3),read_group.getExcelValue(13,4))  #点击确认搜索按钮



    def intogroupform(self):
        """

        :return:
        """
        self.click_element(self.gruop_button[0],self.gruop_button[1])
        self.switch_frame(0)

    def new_group(self):
        """

        :return:
        """
        self.intogroupform()
        self.click_element(self.create_group[0],self.create_group[1])
        self.input_value(self.gruopname[0],self.gruopname[1],self.gruopname[2])
        self.input_value(self.groupresume[0],self.groupresume[1],self.groupresume[2])

        self.action_select(self.handle_jointype[0],self.handle_jointype[1],self.handle_jointype[2])
        self.input_value(self.grouptag[0], self.grouptag[1],self.grouptag[2])
        self.action_select(self.handle_typeid[0],self.handle_typeid[1],self.handle_typeid[2])
        self.input_value(self.gruop_logo[0],self.gruop_logo[1],self.gruop_logo[2])
        self.click_element(self.confirm[0],self.confirm[1])
        self.action_alert_yes()

    def search_group(self):
        """

        :return:
        """
        self.intogroupform()
        self.click_element(self.searchgroup[0],self.searchgroup[1])
        self.input_value(self.input_searchgroup[0],self.input_searchgroup[1],self.input_searchgroup[2])
        self.click_element(self.click_confirm[0],self.click_confirm[1])

if __name__=="__name__":
    pass

