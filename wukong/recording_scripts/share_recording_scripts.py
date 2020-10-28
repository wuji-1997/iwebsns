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

class TestShare():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_share(self):
    self.driver.get("http://localhost/iwebsns/main.php")
    self.driver.set_window_size(1084, 738)
    self.driver.find_element(By.CSS_SELECTOR, ".app_share span").click()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.ID, "add_outer_share").click()
    self.driver.find_element(By.ID, "add_outer_share").send_keys("http://www.baidu.com")
    self.driver.find_element(By.CSS_SELECTOR, ".share_button").click()
    self.driver.switch_to.default_content()
    self.driver.find_element(By.ID, "tag").click()
    self.driver.find_element(By.ID, "tag").send_keys("测试")
    self.driver.find_element(By.ID, "share_com").click()
    self.driver.find_element(By.ID, "share_com").send_keys("啊啊")
    self.driver.find_element(By.ID, "_ButtonOK_0").click()
    self.driver.find_element(By.ID, "_ButtonCancel_0").click()
  
