from wukong.common.my_log import CRM_log
import logging
from wukong.config import conf
import xlrd
import os

excel_log = CRM_log(__name__,file=logging.INFO,cmd=logging.INFO)

class ReadExcel(object):

    def __init__(self,sheetname=None):
        """

        :param filepath:
        :param sheet_name:
        """
        self.sheet_name =sheetname
        try:
            self.workname = xlrd.open_workbook(r'G:\demo\wukong\data\test-excel.xlsx')
            self.worksheetname = self.workname.sheet_by_name(self.sheet_name)
        except Exception:
            excel_log.name.exception(f'{self.workname}或者{self.worksheetname}不存在')
            raise
        else:
            excel_log.name.info(f'打开{self.workname}成功获取{self.worksheetname}成功')

    def getExcelValue(self,rows,colxs):
        """

        :param rows:
        :param colxs:
        :return:
        """
        try:
            value = self.worksheetname.cell_value(rows,colxs)
        except Exception:
            excel_log.name.exception(f'获取表数据 {value} 失败')
        else:
            excel_log.name.info(f'获取表数据 {value} 成功')
            return value

if __name__=='__main__':
    test = ReadExcel('相册页面')
    value = test.getExcelValue(5,4)
    value2 = test.getExcelValue(5,5)
    print(value,value2)