from wukong.common.my_log import CRM_log
from selenium import webdriver
import logging
from wukong.page.base_page import BasePage
from wukong.common.readexcel import ReadExcel
blog_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)
from selenium.webdriver.common.by import By

read_blog = ReadExcel('日志页面')

class Blog_page(BasePage):

    #元素定位
    blog_botton = (By.CLASS_NAME,read_blog.getExcelValue(1,3)) #点击日志按钮
    switch_id =read_blog.getExcelValue(2,3)                    #切换内置表单的id属性
    new_blog_botton = (By.LINK_TEXT,read_blog.getExcelValue(3,3)) #点击新建日志按钮
    blog_title = [(By.NAME,read_blog.getExcelValue(4,2)),[read_blog.getExcelValue(4,4)]]#输入日志标题  测试数据
    select_first = [(By.ID,read_blog.getExcelValue(5,3)),[read_blog.getExcelValue(5,4)]]  #定位到下拉框  选择值
    