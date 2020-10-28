import unittest
from wukong.config.conf import *




if __name__=='__main__':

    test_suit=unittest.defaultTestLoader.discover(case_path,pattern='test_login')
    runner = unittest.TextTestRunner()
    runner.run(test_suit)

