import configparser
import os
from wukong.common.my_log import CRM_log
import logging
from wukong.config import conf
config_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)


class Read_conf(object):

    def __init__(self):
        """

        """
        self.sh = configparser.ConfigParser()

    #从配置文件中读取数据
    def getconfvalue(self,file_path,section_Name,option_name):
        """

        :param file_path:
        :param section_Name:
        :param option_name:
        :return:
        """
        try:
            self.sh.read(file_path)
            value = self.sh.get(section_Name,option_name)

        except Exception:
            config_log.name.exception(f'读取配置文件{file_path}失败或{section_Name}不存在或{option_name}不存在')
            raise
        else:
            config_log.name.exception(f"读取配置文件{file_path}成功")
            return value


if __name__=="__main__":
    test = Read_conf()
    value =  test.getconfvalue(os.path.join(conf.current_path,'config.ini'),'project','project_path')
    print(value)