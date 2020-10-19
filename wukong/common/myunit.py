from selenium import webdriver
import unittest
import logging
from wukong.common.my_log import CRM_log
from wukong.common.driver import WebDriver
from wukong.page.login_page import LoginPage
unit_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)

class MyUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = WebDriver().chorme()
        cls.driver.maximize_window()
        unit_log.name.info('打开谷歌浏览器成功')

    def setUp(self) -> None:
        self.login = LoginPage(self.driver)
        self.login.open()
        unit_log.name.info('------------------执行案例开始-----------------')

    def tearDown(self) -> None:
        """

        :return:
        """
        self.driver.refresh()
        unit_log.name.info('------------------执行案例完成-----------------')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        unit_log.name.info('关闭谷歌驱动驱动成功')
if __name__=='__main__':
    unittest.main()
