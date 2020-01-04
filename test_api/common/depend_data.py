import json

from test_api.common.excel_fun import openExcel
from test_api.common.excel_get_data import GetData
from test_api.basic_fun.base_method import RunMain


class Depend_data():
    def __init__(self):
        self.data=GetData()
        self.runMain=RunMain()

    #获取某行整行的值
    def get_rows_data(self,case_id):
        return openExcel().get_rows_data(case_id)

    #根据case依赖执行case
    def run_dependent(self,row):
        #获取case_depend的值
        case_depend=self.data.get_case_depend1(row)
        #根据case_depend的值获取行号
        rows_value=self.data.open_data.get_rownum(case_depend)
        #根据行号获取具体的值
        url=self.data.get_url(rows_value)
        method=self.data.get_method_way(rows_value)
        data=self.data.get_line(rows_value)
        header=self.data.get_header(rows_value)

        #执行case
        res = self.runMain.run_main(url, method, data, header)
        # print(res)
        return res


    #根据依赖的key去获取执行依赖case的响应，然后返回
    def get_data_for_key(self,row):
        case_response_depend=self.data.get_case_response_depend(row)
        response_data=self.run_dependent(row)

        # print(case_response_depend)
        # print(response_data)

        # json_exe=parse(case_response_depend)
        # madle=json_exe.find(response_data)
        # return [math.value for math in madle][0]

        result=json.loads(response_data)
        # print(result)
        for key,value in result.items():
                if key=='user':
                    return value

