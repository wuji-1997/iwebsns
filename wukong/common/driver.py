from wukong.common.my_log import CRM_log
from selenium import webdriver
import logging
driver_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)

class WebDriver(object):


    def chorme(self):
        """

        :return:
        """
        try:
            self.driver = webdriver.Chrome()
        except Exception:
            driver_log.name.exception('请先安装chorme驱动')
            raise
        else:
            driver_log.name.info(f'启动{self.driver}驱动成功')
            return self.driver

    def iE(self):
        """

        :return:
        """
        try:
            self.driver = webdriver.Ie()
        except Exception:
            driver_log.name.exception('请先安装ie驱动')
            raise
        else:
            driver_log.name.info(f'启动{self.driver}驱动成功')
            return self.driver

    def firefox(self):
        """

        :return:
        """
        try:
            self.driver = webdriver.Ie()
        except Exception:
            driver_log.name.exception('请先安装firefox驱动')
            raise
        else:
            driver_log.name.info(f'启动{self.driver}驱动成功')
            return self.driver

    def oprea(self):
        """

        :return:
        """
        try:
            self.driver = webdriver.Opera()
        except Exception:
            driver_log.name.exception('请先安装opera驱动')
            raise
        else:
            driver_log.name.info(f'启动{self.driver}驱动成功')
            return self.driver

if __name__=='__main__':
    from selenium import webdriver
    driver = WebDriver().chorme()