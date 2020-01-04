import xlrd
from xlutils.copy import copy

# datas=xlrd.open_workbook('./case1.xls')
# table=datas.sheet_by_index(0)
# table=datas.sheets()[0]
# print(table.nrows)
# print(table.cell_value(2,4))

class openExcel():
    def __init__(self,filename=None,table_index=None):
        if filename:
            self.filename=filename
            self.table_index = table_index
        else:
            self.filename=r'E:\python\envname\Scripts\imooc\test_api\data\case1.xls'
            self.table_index=0
        self.table=self.get_tabel()

    def get_tabel(self):
        #打开文件
        data=xlrd.open_workbook(self.filename)
        #获取某个sheet表的内容
        table=data.sheets()[self.table_index]
        return table

    #获取行数
    def get_table_rows(self):
        # table=self.get_tabel()
        # return table.nrows
        return self.table.nrows

    #获取某一区间值
    def get_table_value(self,hang,lie):
        return self.table.cell_value(hang,lie)

    #将实际结果写入excel文件
    def write_value(self,row,line,value):
        read_data=xlrd.open_workbook(self.filename)
        copy_data=copy(read_data)
        sheet_data=copy_data.get_sheet(0)
        sheet_data.write(row,line,value)
        copy_data.save(self.filename)

    #获取某一行的值
    def get_row_values(self,row):
        row_values=self.table.row_values(row)
        return row_values

    #获取某一列的值
    def get_col_values(self,col=None):
        if col!=None:
            return self.table.col_values(col)
        else:
            return self.table.col_values(0)

    #根据case_id找到对应的行号
    def get_rownum(self,case_id):
        col_values=self.get_col_values()
        num=0
        for col_value in col_values:
            if case_id==col_value:
                return num
            num=num+1

    #根据行号找到该行的值
    def get_rows_data(self,case_id):
        row=self.get_rownum(case_id)
        return self.get_row_values(row)

    # #根据case_id找到对应的行号
    # def get_rownum1(self,case_id):
    #     col_values=self.table.col_values(0)
    #     num=0
    #     for col_value in col_values:
    #         if case_id==col_value:
    #             return num
    #         num=num+1
    #
    # #根据行号找到该行的值
    # def get_rows_data1(self,case_id):
    #     row=self.get_rownum1(case_id)
    #     return self.table.row_values(row)




if __name__ == '__main__':
    a=openExcel()
    b=a.get_table_rows()
    c=a.get_table_value(13,9)
    print(b)
    print(c)