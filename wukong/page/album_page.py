from wukong.common.my_log import CRM_log
from selenium import webdriver
import logging
from wukong.page.base_page import BasePage
from wukong.common.readexcel import ReadExcel
album_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)
from selenium.webdriver.common.by import By

read_album = ReadExcel('相册页面')


class Album_page(BasePage):

    albumbutton = (read_album.getExcelValue(1, 3), read_album.getExcelValue(1, 4))  # 相册按钮
    switchid1 = read_album.getExcelValue(2, 4)  # 切换至相册内置表单的id属性值
    newalbumbutton = (read_album.getExcelValue(3, 3), read_album.getExcelValue(3, 4))  # 新建相册按钮
    album_name = (read_album.getExcelValue(4, 3), read_album.getExcelValue(4, 4), read_album.getExcelValue(4, 5))  # 输入相册名称
    album_msg = (read_album.getExcelValue(5, 3), read_album.getExcelValue(5, 4), read_album.getExcelValue(5, 5))  # 输入相册描述
    album_tag = (read_album.getExcelValue(6, 3), read_album.getExcelValue(6, 4), read_album.getExcelValue(6, 5))  # 输入相册标签
    album_sercet = (read_album.getExcelValue(7, 3), read_album.getExcelValue(7, 4), read_album.getExcelValue(8, 3),
                    read_album.getExcelValue(8, 4),
                    read_album.getExcelValue(10, 3), read_album.getExcelValue(10, 4))  # 设置隐私，选择仅自己，确定
    holdalbum = (read_album.getExcelValue(12, 3), read_album.getExcelValue(12, 4))  # 点击创建日志

    getphoto = (read_album.getExcelValue(13, 3), read_album.getExcelValue(13, 4))  # 点击上传相片
    albumselect = (read_album.getExcelValue(14, 3), read_album.getExcelValue(14, 4))  # 处理选择相册下拉框

    way = (read_album.getExcelValue(15, 3), read_album.getExcelValue(15, 4))  # 切换上传方式
    photo = (
    read_album.getExcelValue(16, 3), read_album.getExcelValue(16, 4), read_album.getExcelValue(16, 5))  # 开始上传相片
    hold = (read_album.getExcelValue(17, 3), read_album.getExcelValue(17, 4))  # 点击确认上传
    updatealbum = (read_album.getExcelValue(18, 3), read_album.getExcelValue(18, 4))  # 点击编辑相册

    updatetag = (read_album.getExcelValue(20, 3), read_album.getExcelValue(20, 4), read_album.getExcelValue(20, 5))  # 输入新的标签
    updatebutton = (read_album.getExcelValue(21, 3), read_album.getExcelValue(21, 4))  # 点击确认更新按钮
    datelealbum = (read_album.getExcelValue(22, 3), read_album.getExcelValue(22, 4))  # 点击删除相册按钮



    def intoalbumform(self):
        """

        :return:
        """
        self.click_element(loc=self.albumbutton[0],element_value=self.albumbutton[1])
        self.switch_frame(0)



    def new_album(self):
        """

        :return:
        """
        self.intoalbumform()
        self.click_element(self.newalbumbutton[0],self.newalbumbutton[1])
        self.input_value(self.album_name[0],self.album_name[1],self.album_name[2])
        self.input_value(self.album_msg[0],self.album_msg[1],self.album_msg[2])
        self.input_value(self.album_tag[0],self.album_tag[1],self.album_tag[2])
        self.click_element(self.album_sercet[0],self.album_sercet[1])
        self.click_element(self.album_sercet[2],self.album_sercet[3])
        self.click_element(self.album_sercet[4],self.album_sercet[5])
        self.click_element(self.holdalbum[0],self.holdalbum[1])

    def delete_album(self):
        """"""
        self.intoalbumform()
        self.click_element(self.datelealbum[0],self.datelealbum[1])
        self.action_alert_yes()

    def update_album(self):
        """

        :return:
        """
        self.intoalbumform()
        self.click_element(self.updatealbum[0],self.updatealbum[1])
        self.clear_value(self.album_name[0],self.album_name[1])
        self.input_value(self.album_name[0],self.album_name[1],self.updatetag[-1])
        self.click_element(self.updatebutton[0],self.updatebutton[1])




if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost/iwebsns/index.php")
    driver.find_element_by_name('login_email').send_keys('1131228804@qq.com')
    driver.find_element_by_name('login_pws').send_keys('wuji0121')
    driver.find_element_by_name('loginsubm').click()

    m = Album_page(driver)
    m.new_album()




