from wukong.common.my_log import CRM_log
import logging
from wukong.common.myunit import MyUnit
import unittest
from wukong.page.album_page import Album_page
test_album_log= CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)


class Test_album(MyUnit):
    @unittest.skip('wuji')
    def test_aa_newalbum(self):
        """

        :return:
        """
        self.login.login()

        self.album = Album_page(self.driver)
        self.album.make_sleep(10)
        try:
            self.album.new_album()
        except Exception:
            test_album_log.name.exception(f'新增相册失败')
        else:
            test_album_log.name.info('新增相册成功')
            value = self.album.album_name[-1]
            value2 = self.album.getpagecode()
            try:
                self.assertIn(value,value2)
            except Exception:
                test_album_log.name.exception(f'断言失败，{value} 不在当前页面')
                raise
            else:
                test_album_log.name.info(f'断言成功，{value} 在当前页面')


    def test_cc_deletealbum(self):
        """

        :return:
        """
        self.login.login()
        self.album = Album_page(self.driver)
        try:
           self.album.delete_album()
        except Exception:
            test_album_log.name.info('删除相册失败')
            raise
        else:
            test_album_log.name.info('删除相册成功')
            value = self.album.album_tag[-1]
            value2 = self.album.getpagecode()
            try:
                self.assertNotIn(value,value2)
            except Exception:
                test_album_log.name.exception(f'断言失败，{value} 在当前页面')
                raise
            else:
                test_album_log.name.info(f'断言成功，{value} 不在当前页面')

    @unittest.skip('wuji')
    def test_bb_updatealbum(self):
        """

        :return:
        """

        self.album = Album_page(self.driver)
        try:
            self.album.update_album()
        except Exception:
            test_album_log.name.exception('更新相册失败')
            raise
        else:
            test_album_log.name.info('更新相册成功')
            value =self.album.updatetag[-1]
            value2 = self.album.getpagecode()
            try:
                self.assertIn(value,value2)
            except Exception:
                test_album_log.name.exception(f'断言失败，{value} 在当前页面')
                raise
            else:
                test_album_log.name.info(f'断言成功，{value} 不在当前页面')



if __name__=='__main__':
    unittest.main()