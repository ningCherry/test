import json

from test_api.common.depend_data import Depend_data
from test_api.common.excel_get_data import GetData
from test_api.basic_fun.function import *
from test_api.basic_fun.base_method import RunMain


class RunTest():
    def __init__(self):
        self.base=GetData()
        self.Runmain=RunMain()

    def go_on_run(self):
        rows=self.base.get_id()
        pass_count=[]
        fail_count=[]

        for i in range(1,rows):
            id=self.base.get_excel_id(i)
            url1=self.base.get_url(i)
            run1=self.base.get_is_run(i)
            method1=self.base.get_method_way(i)
            header1=self.base.get_header(i)
            data1=self.base.get_line(i)
            result=self.base.get_qw_result(i)
            # result=self.base.get_result(i)
            # print(result)
            case_depend=self.base.get_case_depend1(i)
            data_depend=self.base.get_data_depend(i)

            if run1:

                if case_depend!=None:
                    #获取依赖的响应数据
                    depend_respense_data=Depend_data().get_data_for_key(i)
                    data1[data_depend]=depend_respense_data

                res = self.Runmain.run_main(url1, method1, data1, header1)
                print(res)

                if test_result(result,json.loads(res)):
                    print('测试通过')
                    self.base.get_actual_result(i,res)
                    #统计跑成功的案例id
                    pass_count.append(id)
                else:
                    print('测试失败')
                    self.base.get_actual_result(i,res)
                    # 统计跑失败的案例id
                    fail_count.append(id)
        # print(len(pass_count))
        # print(len(fail_count))
        # send_main(pass_count,fail_count)

if __name__ == '__main__':
    a=RunTest().go_on_run()
    # print(a)


