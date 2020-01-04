import pymysql

class Get_sql():
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='mysql123', db='book')

    def get_sql(self,sql):
        corsor=self.db.cursor()
        corsor.execute(sql)

        #获取列名属性
        index = corsor.description
        # print(index)
        #获取查询结果
        rows=corsor.fetchall()
        # print(rows)

        for res in rows:
            row={}
            for i in range(len(index)):
                row[index[i][0]]=res[i]
            return row

        self.db.commit()
        self.db.close()


if __name__ == '__main__':
    sql='select user,password from test_api where id=2'
    print(Get_sql().get_sql(sql))

