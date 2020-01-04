from DBUtils.PooledDB import PooledDB
import pymysql
from Website.orm.mysql_config import set_mysql_config
from Website.test_case.modle.function import get_logger

logger=get_logger()

def create_pool():
    db_config=set_mysql_config('test')
    return PooledDB(pymysql,5,user=db_config['user'],
                    password=db_config['password'],
                    host=db_config['host'],
                    port=db_config['port'],
                    db=db_config['db']
                    ).connection()


class Filed():
    def __init__(self,column_name,column_type):
        self.column_name=column_name
        self.column_typr=column_type

class ModleMetaclass(type):
    def __new__(cls, table_name,bases,attrs):
        if table_name=='Modle':
            return type.__new__(cls, table_name,bases,attrs)

        mapping={}
        for k,v in attrs.items():
            if isinstance(v,Filed):
                mapping[k]=v

        for k in mapping.keys():
            attrs.pop(k)

        attrs['__mapping__']=mapping
        attrs['__table__']=table_name.lower()

        return type.__new__(cls,table_name,bases,attrs)

class Modle(dict,metaclass=ModleMetaclass):
    def __init__(self,**awk):
        super().__init__(**awk)

    # insert into table_name (字段名称) values (值)
    def insert(self,column_list,param_list):
        logger.info('执行inset方法：insert into {}({}) values ({})'.format(self.__table__,column_list,param_list))

        for key in column_list:
            if key not in self.__mapping__.keys():
                raise RuntimeError('这个字段没有发现 field not found')

        # 检查参数的合法性   "value"
        args = self.__check_params(param_list)

        sql='insert into {}({}) values ({})'.format(self.__table__,','.join(column_list),','.join(args))
        res=self.__do_excute(sql)
        logger.info(res)

    def __check_params(self,param_list):
        args = []
        for key in param_list:
            key = '\"' + key + '\"'
            args.append(key)
        return args

    def __do_excute(self, sql):
        a = create_pool()
        cosor = a.cursor()
        if 'select' in sql:
            cosor.execute(sql)
            res = cosor.fetchall()
        else:
            res = cosor.execute(sql)
        a.commit()
        a.close()

        return res

    def select(self, column_list, where_list):
        logger.info('执行select方法：select {} from {} where {}'.format(column_list, self.__table__, where_list))

        for key in column_list:
            if key not in self.__mapping__.keys():
                raise RuntimeError('这个字段没有发现 field not found')

        sql = 'select {} from {} where {}'.format(','.join(column_list), self.__table__, 'and'.join(where_list))
        res = self.__do_excute(sql)
        logger.info(res)

    def update(self, set_column_list, where_list):
        logger.info('执行update方法：update {} set {} where {}'.format(self.__table__, set_column_list, where_list))

        sql = 'update {} set {} where {}'.format(self.__table__, 'and'.join(set_column_list),
                                                 'and'.join(where_list))
        res = self.__do_excute(sql)
        logger.info(res)

    def delete(self, where_list):
        logger.info('执行delete方法：delete from {} where {}'.format(self.__table__, where_list))

        sql = 'delete from {} where {}'.format(self.__table__, 'and'.join(where_list))
        res = self.__do_excute(sql)
        logger.info(res)

class Good(Modle):
    computer_part = Filed('computer_part', 'varchar(20)')
    computer_info = Filed('computer_info', 'text')


if __name__ == '__main__':

    goods=Good()
    # goods.insert(['computer_part','computer_info'],['组件','组件信息'])
    goods.select(['computer_part','computer_info'],['id=4'])
    # goods.update(['computer_part="组件3"'],['id=4'])
    # goods.delete(['id=5'])