import os
from wukong.common.readini import Read_conf
#当前路径
current_path = os.path.split(os.path.realpath(__file__))[0]
#os.path.realpath(__file__)返回当前执行脚本的路径
#os.path.split()返回工作项目路径和当前执行脚本文件名以元组形式返回

read_path = Read_conf()
#项目路径:G:\demo
projectpath =read_path.getconfvalue(os.path.join(current_path,'config.ini'),'project','project_path')

#log路径
#G:\demo\wukong\log\Log
log_path = os.path.join(projectpath,'wukong','log','Log')

#测试数据文件路径
#G:\demo\wukong\data
excel_path =os.path.join(projectpath,'wukong','data')

#report文件路径
#G:\demo\wukong\report
report_path = os.path.join(projectpath,'wukong','data')

#测试用例路径
#G:\demo\wukong\test_case
case_path = os.path.join(projectpath,'wukong','test_case')




if __name__=='__main__':
    pass