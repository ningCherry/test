def set_mysql_config(env):
    if env=='pro':
        db_config={
            'user':'root',
            'password':'mysql123',
            'host':'127.0.0.1',
            'port':3306,
            'db':'book'
        }
    elif env=='test':
        db_config = {
            'user': 'root',
            'password': 'mysql123',
            'host': '127.0.0.1',
            'port': 3306,
            'db': 'book'
        }
    return db_config