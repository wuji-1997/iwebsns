from wukong.common.my_log import CRM_log
import logging
from wukong.common.myunit import MyUnit
import unittest
from wukong.page.group_page import *
test_group_log=CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)


class Test_group(MyUnit):

    def test_new_group(self):
        """

        :return:
        """
        self.login.login()
        self.group = Group_page(self.driver)
        try:
            self.group.new_group()
        except Exception:
            test_group_log.name.exception('失败，新建分组成功')
        else:
            test_group_log.name.info('成功，新建分组失败')
            value = self.group.gruopname[2]
            value2 = self.group.getpagecode()
            try:
                self.assertIn(value,value2)
            except Exception:
                test_group_log.name.exception(f'失败，{value} 不在当前页面中')
            else:
                test_group_log.name.exception(f'成功，{value} 在 当前页面中')

    def test_search_group(self):
        """

        :return:
        """
        self.group = Group_page(self.driver)
        try:
            self.group.search_group()
        except Exception:
            test_group_log.name.exception('失败，搜索的分组不存在')
        else:
            test_group_log.name.info('成功，查询分组成功')
            value = '对不起，没有您要查找的群组'
            value2 = self.group.getpagecode()
            try:
                self.assertIn(value, value2)
            except Exception:
                test_group_log.name.exception(f'失败，{value} 在 当前页面中')
            else:
                test_group_log.name.exception(f'成功，{value} 不在 当前页面中')

if __name__=='__main__':
    unittest.main()
