import json

from test_api.common.excel_fun import openExcel


class openJson():
    def __init__(self,hang,lie,filename=None):
        if filename:
            self.filename=filename
        else:
            self.filename=r'E:\python\envname\Scripts\imooc\test_api\data\data.json'
        self.line=openExcel().get_table_value(hang,lie)

    def get_json(self):
        with open(self.filename,'r') as f:
            data=json.load(f)
            return data[self.line]

if __name__ == '__main__':
    print(openJson(13,9).get_json())