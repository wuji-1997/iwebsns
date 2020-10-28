from wukong.common.my_log import CRM_log
import logging
from wukong.common.myunit import MyUnit
import unittest
from wukong.page.sharp_page import Sharp_page
test_share_log= CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)


class Test_share(MyUnit):

    def test_new_share(self):
        """

        :return:
        """
        self.login.login()
        self.share = Sharp_page(self.driver)
        try:
            self.share.new_share()
        except Exception:
            test_share_log.name.exception(f'新建分享{self.share.share_input[2]}失败')
            raise
        else:
            test_share_log.name.info(f'新建分享{self.share.share_input[2]}成功')
            self.share.intoshareform()
            value = self.share.share_title[2]
            value2 =self.share.getpagecode()
            try:
                self.assertIn(value,value2)
            except Exception:
                test_share_log.name.exception(f'断言失败，{value}  不在 当前页面中')
                raise
            else:
                test_share_log.name.info(f'断言成功，{value}  在 当前页面中')



    def test_zdelete_share(self):
        """

        :return:
        """

        self.share = Sharp_page(self.driver)
        try:
            self.share.delete_share()
        except Exception:
            test_share_log.name.exception('删除分享失败')
            raise
        else:
            test_share_log.name.info('删除分享成功')
            value = self.share.share_title[2]
            value2 = self.share.getpagecode()
            try:
                self.assertNotIn(value, value2)
            except Exception:
                test_share_log.name.exception(f'断言失败，{value}  在 当前页面中')
                raise
            else:
                test_share_log.name.info(f'断言成功，{value}  不在 当前页面中')
if __name__=="__main__":
    unittest.main()