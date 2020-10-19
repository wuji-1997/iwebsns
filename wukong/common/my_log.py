"""
封装日志模块
记录项目运行过程中的全部信息，方便定位问题
"""
import logging
import time

class CRM_log(object):

    def __init__(self,name,file=logging.INFO,cmd = logging.INFO):
        """

        :param name:
        :param file: 文件输出渠道日志等级
        :param cmd:  控制台输出渠道日志等级
        """
        self.name = logging.getLogger(name)   #定义日志收集器
        self.name.setLevel(logging.DEBUG)     #设置日志收集器收集的日志等级

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(levelno)s] - %(levelname)s - %(message)s')           #设置日志输出的格式

        log_time = time.strftime('%Y-%m-%d')


        self.filelog = r'G:\demo\wukong\log\Log\log'+log_time+ '.log'                         #文件输出渠道输出的日志文件存储地址

        sh = logging.FileHandler(self.filelog)
        sh.setFormatter(fmt)
        sh.setLevel(file)

        cmd_sh = logging.StreamHandler()
        cmd_sh.setFormatter(fmt)
        cmd_sh.setLevel(cmd)

        self.name.addHandler(sh)
        self.name.addHandler(cmd_sh)
        #将日志输出的渠道添加到日志容器中




if __name__ == '__main__':
    test = CRM_log('wuji',file=logging.INFO,cmd=logging.INFO)
    test.name.debug("debug")