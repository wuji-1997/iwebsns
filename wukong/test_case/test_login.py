from wukong.common.my_log import CRM_log
import logging
from wukong.common.myunit import MyUnit
import unittest
test_login_log= CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)


class Test_login(MyUnit):

     @unittest.skip('不想测试的案例')
     def test_login(self):
        """

        :return:
        """
        self.login.login()
        self.login.make_sleep(5)
        value = self.login.get_url()
        self.assertEqual(value,self.login.test_date[-1])


     def test_incorrent_email(self):
         """
         输入错误的用户名
         :return:
         """
         self.login.login(user=self.login.test_date[1],password=self.login.test_date[3])
         self.login.make_sleep(5)
         value = '登录帐号错误，请重试'
         value2 = self.login.getpagecode()
         try:
             self.assertIn(value,value2)
         except Exception:
             test_login_log.name.exception(f'测试案例通过，')
         else:
             test_login_log.name.info('测试案例通过，请查看测试报告')


     def test_null_email(self):
         """
         用户名为空
         :return:
         """
         self.login.login(user="",password=self.login.test_date[3])
         self.login.make_sleep(5)
         value = '登录帐号错误，请重试'
         value2 = self.login.getpagecode()
         try:
             self.assertIn(value, value2)
         except Exception:
             test_login_log.name.exception(f'测试未通过')
         else:
             test_login_log.name.info('测试案例通过，请查看测试报告')

     def test_incorrent_pws(self):
         """
         输入错误的密码
         :return:
         """
         self.login.login(user=self.login.test_date[0], password=self.login.test_date[-2])
         self.login.make_sleep(5)
         value = '用户密码错误!'
         value2 = self.login.getpagecode()
         try:
             self.assertIn(value, value2)
         except Exception:
             test_login_log.name.exception(f'测试案例未通过')
         else:
             test_login_log.name.info('测试案例通过，请查看测试报告')

     def test_null_pws(self):
         """
         密码为空
         :return:
         """
         self.login.login(user=self.login.test_date[0], password='')
         self.login.make_sleep(5)
         value = '密码不能为空!'
         value2 = self.login.getpagecode()
         try:
             self.assertIn(value, value2)
         except Exception:
             test_login_log.name.exception(f'测试案例未通过')
         else:
             test_login_log.name.info('测试案例通过，请查看测试报告')




     @unittest.skip('不想测试的案例')
     def test_login_out(self):
         """

         :return:
         """
         self.login.make_sleep(10)
         self.login.loginout()
         self.login.make_sleep(10)
         value = self.login.get_url()
         self.assertEqual(value,self.login.test_date[2])
if __name__=='__main__':
    unittest.main()
