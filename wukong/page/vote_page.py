from wukong.common.my_log import CRM_log
from selenium import webdriver
import logging
from wukong.page.base_page import BasePage
from wukong.common.readexcel import ReadExcel
login_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)
from selenium.webdriver.common.by import By
read_vote = ReadExcel('投票页面')

class Vote_page(BasePage):

    vote_button=(read_vote.getExcelValue(1,3),read_vote.getExcelValue(1,4))   #点击“投票”节点
    start_vote=(read_vote.getExcelValue(3,3),read_vote.getExcelValue(3,4))    #点击“发起投票”超链接
    vote_title = (read_vote.getExcelValue(4,3),read_vote.getExcelValue(4,4),read_vote.getExcelValue(4,5))  #输入“投票标题”
    vote_msg =[(read_vote.getExcelValue(5,3),read_vote.getExcelValue(5,4))  #点击“添加投票详细说明”超链接
        ,(read_vote.getExcelValue(6,3),read_vote.getExcelValue(6,4),read_vote.getExcelValue(6,5))]  #输入“详细说明”
    candidates=[(read_vote.getExcelValue(7,3),read_vote.getExcelValue(7,4),read_vote.getExcelValue(7,5)),     #输入“候选项一”
                (read_vote.getExcelValue(8,3),read_vote.getExcelValue(8,4),read_vote.getExcelValue(8,5)),     #输入“候选项二”
                (read_vote.getExcelValue(9,3),read_vote.getExcelValue(9,4),read_vote.getExcelValue(9,5))]     #输入“候选项三”
    select = (read_vote.getExcelValue(10,3),read_vote.getExcelValue(10,4),read_vote.getExcelValue(10,5))      #处理“可投选项”下拉框
    deadline_time = [read_vote.getExcelValue(11,4),   #处理“截止时间”时间控件
                     (read_vote.getExcelValue(12,3),read_vote.getExcelValue(12,4),read_vote.getExcelValue(12,5))]   #输入截止时间

    vote_range=(read_vote.getExcelValue(13,3),read_vote.getExcelValue(13,4)) #选择“投票限制”
    msg_range=(read_vote.getExcelValue(14,3),read_vote.getExcelValue(14,4))  #选择“评论限制”
    postreward = (read_vote.getExcelValue(15,3),read_vote.getExcelValue(15,4))  #选择“悬赏投票”
    dynamic_options=(read_vote.getExcelValue(16,3),read_vote.getExcelValue(16,4))  #选择“悬赏投票”
    comfirm_button=(read_vote.getExcelValue(17,3),read_vote.getExcelValue(17,4))  #点击“确认”按钮

    clicknewvote = (read_vote.getExcelValue(18,3),read_vote.getExcelValue(18,4))  #点击新建的投票
    detele = (read_vote.getExcelValue(19,3),read_vote.getExcelValue(19,4))        #点击“删除本投票”超链接

    alert1=(read_vote.getExcelValue(20,3),read_vote.getExcelValue(20,4))   #处理“确认删除”提示框

    more_candidates=[(read_vote.getExcelValue(23,3),read_vote.getExcelValue(23,4))  #点击增加候选项
        ,(read_vote.getExcelValue(24,3),read_vote.getExcelValue(24,4),read_vote.getExcelValue(24,5))]          #输入新增的候选项

    update_time = [(read_vote.getExcelValue(26,3),read_vote.getExcelValue(26,4)),#点击修改截至日期
                   (read_vote.getExcelValue(28,4),read_vote.getExcelValue(28,5)),#处理时间控制并且赋值
                   read_vote.getExcelValue(29,5)]

    vote_sumup = [(read_vote.getExcelValue(30,3),read_vote.getExcelValue(30,4)),  #点击投票总结
                  (read_vote.getExcelValue(31,3),read_vote.getExcelValue(31,4))]  #输入总结的内容

    reward = [(read_vote.getExcelValue(32,3),read_vote.getExcelValue(32,4)),     #点击追加悬赏
              (read_vote.getExcelValue(33,3),read_vote.getExcelValue(33,4),read_vote.getExcelValue(33,5)),     #输入悬赏总额
              (read_vote.getExcelValue(34,3),read_vote.getExcelValue(34,4)),read_vote.getExcelValue(34,5)]     #输入悬赏单额



    must= (read_vote.getExcelValue(25,3),read_vote.getExcelValue(25,4))         #点击确认按钮

    join=(read_vote.getExcelValue(21,3),read_vote.getExcelValue(21,4))         #点击“立即参与”
    looking = (read_vote.getExcelValue(20,3),read_vote.getExcelValue(20,4))    #点击“去看看”




    def intovoteform(self):
        """

        :return:
        """
        self.click_element(self.vote_button[0],self.vote_button[1])
        self.switch_frame(0)

    def new_vote(self):
        """
        新建一个投票
        :return:
        """
        self.intovoteform()
        self.click_element(self.start_vote[0],self.start_vote[1])
        self.input_value(self.vote_title[0],self.vote_title[1],self.vote_title[2])
        self.click_element(self.vote_msg[0][0],self.vote_msg[0][1])
        self.input_value(self.vote_msg[1][0],self.vote_msg[1][1],self.vote_msg[1][2])
        self.input_value(self.candidates[0][0],self.candidates[0][1],self.candidates[0][2])
        self.input_value(self.candidates[1][0], self.candidates[1][1], self.candidates[1][2])
        self.input_value(self.candidates[2][0], self.candidates[2][1], self.candidates[2][2])
        self.action_select(self.select[0],self.select[1],self.select[2])
        self.js(self.deadline_time[0])
        self.clear_value(self.deadline_time[1][0],self.deadline_time[1][1])
        self.input_value(self.deadline_time[1][0],self.deadline_time[1][1],self.deadline_time[1][2])
        self.click_element(self.comfirm_button[0],self.comfirm_button[1])

    def click_new_vote(self):
        """
        进入新建的投票
        :return:
        """
        self.intovoteform()
        self.click_element(self.clicknewvote[0],self.clicknewvote[1])


    def detele_vote(self):
        """
        删除投票
        :return:
        """
        self.click_new_vote()
        self.click_element(self.detele[0],self.detele[1])
        self.switch_defaultcontent()
        self.click_element(self.alert1[0],self.alert1[1])

    def update_candidates(self):
        """
        增加候选项
        :return:
        """
        self.click_new_vote()
        self.click_element(self.more_candidates[0][0],self.more_candidates[0][1])
        self.switch_defaultcontent()
        self.input_value(self.more_candidates[1][0],self.more_candidates[1][1],self.more_candidates[1][2])
        self.click_element(self.must[0], self.must[1])

    def update_dealine_time(self):
        """
        修改截止日期
        :return:
        """
        self.click_new_vote()
        self.click_element(self.update_time[0][0],self.update_time[0][1])
        self.switch_defaultcontent()
        self.make_sleep(4)
        self.new_js(self.update_time[1][0],self.update_time[1][1])
        self.click_element(self.must[0], self.must[1])


    def write_vote_sumup(self):
        """
        写投票总结
        :return:
        """
        self.click_new_vote()
        self.click_element(self.vote_sumup[0][0],self.vote_sumup[0][1])
        self.switch_defaultcontent()
        self.input_value(self.vote_sumup[1][0],self.vote_sumup[1][1],self.vote_sumup[1][2])
        self.click_element(self.must[0], self.must[1])

    def additional_reward(self):
        """
        追加悬赏
        :return:
        """
        self.click_new_vote()
        self.click_element(self.reward[0][0],self.reward[0][1])
        self.switch_defaultcontent()
        self.input_value(self.reward[1][0],self.reward[1][1],self.reward[1][2])
        self.input_value(self.reward[2][0],self.reward[2][1],self.reward[2][2])
        self.click_element(self.must[0], self.must[1])

    def jionin(self):
        """
        点击立即参与可进入投票详情页面
        :return:
        """
        self.intovoteform()
        self.click_element(self.join[0],self.join[1])

    def look(self):
        """
        点击去看看可进入投票详情页面
        :return:
        """
        self.intovoteform()
        self.click_element(self.looking[0], self.looking[1])








if __name__=='__main__':
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost/iwebsns/index.php")
    driver.find_element_by_name('login_email').send_keys('1131228804@qq.com')
    driver.find_element_by_name('login_pws').send_keys('wuji0121')
    driver.find_element_by_name('loginsubm').click()


    m = Vote_page(driver)
    m.update_dealine_time()

