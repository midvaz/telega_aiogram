import pymysql
from pymysql.cursors import DictCursor
import json
from .config import load_config

config = load_config('bot.ini')
#функция подключения к бд
def connect() -> pymysql.connections.Connection:
    try:
        conn = pymysql.Connect(
            user=config.db.user,
            database=config.db.database,
            password=config.db.password,
            host=config.db.host,
            charset='utf8mb4',
            cursorclass = DictCursor
        )
        return conn
    except Exception as e:
        print('erroe is: ', e)
        return False


if __name__ == '__main__':
    print(connect())