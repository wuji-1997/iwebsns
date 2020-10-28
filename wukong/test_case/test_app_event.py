from wukong.common.my_log import CRM_log
import logging
from wukong.common.myunit import MyUnit
import unittest
from wukong.page.event_page import Event_page
test_event_log= CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)

class Test_event(MyUnit):


    def test_aa_new_event(self):
        """

        :return:
        """
        self.login.login()
        self.event = Event_page(self.driver)


        try:
            self.event.new_event()
            self.event.click_element(self.event.event_button[0],self.event.event_button[1])
        except Exception:
            test_event_log.name.exception(f'新建活动 “{self.event.event_name[-1]}  失败”')
            raise
        else:
            test_event_log.name.info(f'新建活动 “{self.event.event_name[-1]}  成功”')
            value = self.event.select1[-1]
            value2 = self.event.getpagecode()
            try:
                self.assertIn(value,value2)
            except Exception:
                test_event_log.name.exception(f'错误 “{value}” 不在当前页面中-------------测试案例不通过')
                raise
            else:
                test_event_log.name.info(f'成功 “{value}” 在当前页面中-------------测试案例通过')

    @unittest.skip('取消按钮目前定位不到')
    def test_cc_cacel_event(self):
        """

        :return:
        """

        self.event = Event_page(self.driver)
        self.event.cancel_event()
        value = self.event.event_name[-1]
        value2=self.event.getpagecode()
        self.assertNotIn(value,value2)


if __name__=='__main__':
    unittest.main()