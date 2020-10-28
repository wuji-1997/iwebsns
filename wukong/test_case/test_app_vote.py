from wukong.common.my_log import CRM_log
import logging
from wukong.common.myunit import MyUnit
import unittest
from wukong.page.vote_page import Vote_page
test_vote_log= CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)


class Test_vote(MyUnit):

    @unittest.skip("pass")
    def test_aa_new_vote(self):
        """

        :return:
        """

        self.vote = Vote_page(self.driver)
        try:
            self.login.login()
        except Exception:
            test_vote_log.name.exception("登录失败")
            raise
        else:
            test_vote_log.name.info("登录成功")
            try:
                self.vote.new_vote()
            except Exception:
                test_vote_log.name.exception(f"新建投票 “{self.vote.vote_title[2]}” 失败")
                raise
            else:
                test_vote_log.name.info(f"新建投票 “{self.vote.vote_title[2]}” 成功")
                value = self.vote.vote_title[2]
                value2 = self.vote.getpagecode()
                try:
                    self.assertIn(value,value2)
                except Exception:
                    test_vote_log.name.exception(f'错误 “{value}” 不在当前页面中-------------测试案例不通过')
                    raise
                else:
                    test_vote_log.name.info(f'正确 “{value}” 在当前页面中--------------测试案例通过')

    @unittest.skip("pass")
    def test_zz_delete_vote(self):
        """

        :return:
        """


        self.vote = Vote_page(self.driver)
        try:
            self.vote.detele_vote()
        except Exception:
            test_vote_log.name.exception(f"删除投票 “{self.vote.clicknewvote[-1]}” 失败")
            raise
        else:
            test_vote_log.name.info(f"删除投票 “{self.vote.clicknewvote[-1]}” 成功")
            value = self.vote.vote_title[2]
            value2 = self.vote.getpagecode()

            try:
                self.assertNotIn(value, value2)
            except Exception:
                test_vote_log.name.exception(f'错误 “{value}” 在当前页面中-------------测试案例不通过')
                raise
            else:
                test_vote_log.name.info(f'正确 “{value}” 不在当前页面中--------------测试案例通过')

    @unittest.skip("pass")
    def test_bb_update_candidates(self):
        """

        :return:
        """

        self.vote = Vote_page(self.driver)
        try:
            self.vote.update_candidates()
            self.vote.make_sleep(10)
            self.vote.click_new_vote()
        except Exception:
            test_vote_log.name.exception(f'新增候选项 “{self.vote.more_candidates[1][2]}” 失败')
        else:
            test_vote_log.name.info(f'新增候选项 “{self.vote.more_candidates[1][2]}” 成功')
            value = self.vote.more_candidates[1][2]
            value2 = self.vote.getpagecode()
            try:
                self.assertIn(value, value2)
            except Exception:
                test_vote_log.name.exception(f'错误 “{value}” 不在当前页面中-------------测试案例不通过')
                raise
            else:
                test_vote_log.name.info(f'正确 “{value}” 在当前页面中--------------测试案例通过')


    def test_cc_update_dealine_time(self):
        """

        :return:
        """
        self.login.login()
        self.vote = Vote_page(self.driver)
        try:

            self.vote.update_dealine_time()
            self.vote.make_sleep(4)
            self.vote.click_new_vote()
        except Exception:
            test_vote_log.name.exception(f'截止时间修改为 “{self.vote.update_time[2]}” 失败')
        else:
            test_vote_log.name.info(f'截止时间修改为 “{self.vote.update_time[2]}” 成功')
            value = self.vote.update_time[2]
            value2 = self.vote.getpagecode()
            try:
                self.assertIn(value, value2)
            except Exception:
                test_vote_log.name.exception(f'错误 “{value}” 不在当前页面中-------------测试案例不通过')
                raise
            else:
                test_vote_log.name.info(f'正确 “{value}” 在当前页面中--------------测试案例通过')

    @unittest.skip('pass')
    def test_dd_write_vote_sumup(self):
        pass

    @unittest.skip('pass')
    def test_ee_additional_reward(self):
        pass

    @unittest.skip('pass')
    def test_ff_jionin(self):
        pass

    @unittest.skip('pass')
    def test_gg_look(self):
        pass

if __name__=='__main__':
    unittest.main()