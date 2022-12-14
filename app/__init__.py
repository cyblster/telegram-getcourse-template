import config
from flask import Flask
from telebot import TeleBot
from pymysql import Connection


def mysql_query(query_string):
    mysql.connect()
    mysql_cursor = mysql.cursor()
    mysql_cursor.execute(query_string)
    mysql.close()

    return mysql_cursor.fetchall() or []


conf = config.DevelopmentConfig  # Текущий конфиг

app = Flask(__name__)

bot = TeleBot(conf.BOT_KEY)

mysql = Connection(host=conf.MYSQL_HOST, user=conf.MYSQL_USER, passwd=conf.MYSQL_PASSWD, db=conf.MYSQL_DB, autocommit=True)

from . import views
from . import handlers
