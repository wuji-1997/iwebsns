from wukong.common.my_log import CRM_log
import logging
from wukong.common.myunit import MyUnit
import unittest
from wukong.page.blog_page import Blog_page
test_blog_log= CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)


class Test_blog(MyUnit):


    def test_aa_newblog(self):
        """

        :return:
        """
        self.bolg = Blog_page(self.driver)
        try:
            self.login.login()
        except Exception:
            test_blog_log.name.exception("登录失败")
            raise
        else:
            test_blog_log.name.info("登录成功")
            try:
                self.bolg.create_new_blog()
            except Exception:
                test_blog_log.name.exception(f"新建日志 “{self.bolg.title[-1]}” 失败")
                raise
            else:
                test_blog_log.name.info(f"新建日志 “{self.bolg.title[-1]}” 成功")
                value = self.bolg.getpagecode()
                value2 = self.bolg.bolg_tag[-1]
                try:
                    self.assertIn(value2,value)
                except Exception:
                    test_blog_log.name.exception(f'错误 “{value2}” 不在当前页面中-------------测试案例不通过')
                    raise
                else:
                    test_blog_log.name.info(f'正确 “{value2}” 在当前页面中--------------测试案例通过')


    def test_zz_deleteblog(self):
        """

        :return:
        """

        self.bolg= Blog_page(self.driver)
        try:
            self.bolg.delete_blog()
        except Exception:
            test_blog_log.name.exception(f'删除日志 “{self.bolg.title[-1]}”  失败')
            raise
        else:
            test_blog_log.name.info(f'删除日志 “{self.bolg.title[-1]}”  成功')
            value = self.bolg.getpagecode()
            value2 = self.bolg.deletebutton[-1]
            try:
                self.assertNotIn(value2,value)
            except Exception:
                test_blog_log.name.exception(f'错误 {value2} 在当前页面中 -----测试案例不通过')
                raise
            else:
                test_blog_log.name.info(f'正确 {value2} 不在当前页面中 删除日志{self.bolg.title[-1]}成功----------------测试案例通过')


    def test_cc_updateblog(self):
        """

        :return:
        """
        self.bolg = Blog_page(self.driver)

        try:
            self.bolg.update_blog()
        except Exception:
            test_blog_log.name.exception("操作更新失败")
        else:
            test_blog_log.name.info("操作更新成功")
            value = self.bolg.getpagecode()
            value2 = self.bolg.update_tag[-1]
            try:
                self.assertIn(value2, value)
            except Exception:
                test_blog_log.name.exception(f'错误 {value2} 不在当前页面中 -----测试案例不通过')
                raise
            else:
                test_blog_log.name.info(f'正确 {value2} 在当前页面中--------------测试案例通过')

    @unittest.skip("存在问题")
    def test_bb_replyblog(self):
        """

        :return:
        """
        self.bolg = Blog_page(self.driver)
        self.bolg.reply_blog()
        value = self.bolg.getpagecode()
        value2 = self.bolg.blogreply[-1]
        self.assertNotIn(value2,value)

if __name__=="__main__":
    '''
    创建测试套件
    suit = unittest.TestSuite()
    suit.addTest(Test_blog("test_aa_newblog"))
    suit.addTest(Test_blog("test_bb_replyblog"))
    suit.addTest(Test_blog("test_cc_updateblog"))
    suit.addTest(Test_blog("test_dd_deleteblog"))
    
    创建运行器
    runner = unittest.TextTestRunner()  
    runner.run(suit)
    '''
    unittest.main()