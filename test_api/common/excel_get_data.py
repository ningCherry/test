import json

from test_api.common.excel_data import ExcelData
from test_api.common.excel_fun import openExcel
from test_api.data.get_sql import Get_sql


class GetData():
    def __init__(self):
        self.open_data=openExcel()
        self.get_sql=Get_sql()
        self.filename = r'E:\python\envname\Scripts\imooc\test_api\data\data.json'

    #获取行数
    def get_id(self):
        return self.open_data.get_table_rows()

    #获取id
    def get_excel_id(self,row):
        line=ExcelData().get_id()
        id=self.open_data.get_table_value(row,line)
        return id

    #获取url
    def get_url(self,row):
        line=ExcelData().get_url()
        url=self.open_data.get_table_value(row,line)
        return url

    #获取是否执行
    def get_is_run(self,row):
        line=ExcelData().get_yunxing()
        is_run=self.open_data.get_table_value(row,line)
        if is_run=='yes':
            flag=True
        else:
            flag=False
        return flag

    #获取请求类型
    def get_method_way(self,row):
        line=ExcelData().get_method_way()
        method_way=self.open_data.get_table_value(row,line)
        return method_way

    #是否携带header
    def get_header(self,row):
        line=ExcelData().get_header()
        header=self.open_data.get_table_value(row,line)
        if header=='':
            return None
        else:
            return header

    #获取请求数据
    def get_data_line(self,row):
        line=ExcelData().get_data()
        data=self.open_data.get_table_value(row,line)
        return data

    #获取请求数据json格式
    def get_line(self,row):
        with open(self.filename,'r') as f:
            data=json.load(f)
            return data[self.get_data_line(row)]

    #获取预期结果
    def get_result(self,row):
        line=ExcelData().get_result()
        result=self.open_data.get_table_value(row,line)
        return result

    #根据预期结果去查询数据库的值
    def get_qw_result(self,row):
        result=self.get_result(row)
        re=self.get_sql.get_sql(result)
        return re

    #获取case_depend
    def get_case_depend1(self,row):
        line=ExcelData().get_case_depend()
        case_depend=self.open_data.get_table_value(row,line)
        if case_depend:
            return case_depend
        else:
            return None

    # 获取case_response_depend
    def get_case_response_depend(self, row):
        line = ExcelData().get_case_response_depend()
        case_response_depend = self.open_data.get_table_value(row, line)
        return case_response_depend

    # 获取data_depend
    def get_data_depend(self, row):
        line = ExcelData().get_data_depend()
        data_depend = self.open_data.get_table_value(row, line)
        return data_depend

    #将实际结果写入excel文件
    def get_actual_result(self,row,value):
        line=ExcelData().get_actual_result()
        actual_data=self.open_data.write_value(row,line,value)
        return actual_data

if __name__ == '__main__':
    a=GetData().get_qw_result(12)
    print(a)
    print(type(a))
