# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestNewevent():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_newevent(self):
    self.driver.get("http://localhost/iwebsns/main.php")
    self.driver.set_window_size(1084, 738)
    self.driver.find_element(By.CSS_SELECTOR, ".app_event span").click()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.LINK_TEXT, "发起活动").click()
    self.driver.find_element(By.NAME, "title").click()
    self.driver.find_element(By.NAME, "title").send_keys("测试活动")
    self.driver.find_element(By.ID, "s1").click()
    dropdown = self.driver.find_element(By.ID, "s1")
    dropdown.find_element(By.XPATH, "//option[. = '安徽']").click()
    self.driver.find_element(By.ID, "s1").click()
    self.driver.find_element(By.NAME, "location").click()
    self.driver.find_element(By.NAME, "location").send_keys("上海")
    self.driver.find_element(By.ID, "start_time").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".DynarchCalendar-bottomBar > table > tbody > tr > td:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.ID, "KINDEDITORBODY").click()
    self.driver.switch_to.default_content()
    assert self.driver.switch_to.alert.text == "请确认是否加载此类型介绍模板"
    self.driver.switch_to.alert.accept()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
if __name__=='__main__':
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  driver = webdriver.Chrome()
  driver.implicitly_wait(10)
  driver.get("http://localhost/iwebsns/index.php")
  driver.find_element_by_name('login_email').send_keys('1131228804@qq.com')
  driver.find_element_by_name('login_pws').send_keys('wuji0121')
  driver.find_element_by_name('loginsubm').click()
  driver.find_element(By.CSS_SELECTOR, ".app_event span").click()
  driver.switch_to.frame(0)
  driver.find_element(By.LINK_TEXT, "发起活动").click()
  driver.find_element(By.ID, "start_time").click()
  element = driver.find_element(By.CSS_SELECTOR,
                                     ".DynarchCalendar-bottomBar > table > tbody > tr > td:nth-child(1)")
  actions = ActionChains(driver)
  actions.move_to_element(element).release().perform()
  driver.find_element(By.ID, "KINDEDITORBODY").click()

  driver.switch_to.frame(0)
  assert driver.switch_to.alert.text == "请确认是否加载此类型介绍模板"
  driver.switch_to.alert.accept()
  driver.switch_to.frame(0)
  driver.find_element(By.CSS_SELECTOR, "p").click()
  driver.find_element(By.CSS_SELECTOR, "p").click()
  driver.find_element(By.CSS_SELECTOR, "p").click()
  driver.find_element(By.CSS_SELECTOR, "p").click()
  driver.find_element(By.CSS_SELECTOR, "p").click()


