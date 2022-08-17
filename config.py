import os


class BaseConfig:
    APP_KEY = os.getenv('APP_KEY')
    BOT_KEY = os.getenv('BOT_KEY')
    MYSQL_PASSWD = os.getenv('MYSQL_PASSWD')

    BOT_REPLY = {
        'GREETING': 'Для получения ссылки на закрытый канал Азама Ходжаева напишите адрес электронной почты, указанный при Вашей покупке.',
        'INVALID_EMAIL': 'Адрес электронной не найден или уже используется. Если произошла ошибка, пожалуйста, свяжитесь с технической поддержкой @azamkhodzhaev_bot',
        'PAYMENT_EXPIRED': 'Ваш период оплаты курса закончился. Если произошла ошибка, пожалуйста, свяжитесь с технической поддержкой @azamkhodzhaev_bot'
    }

    APP_RATE = {
        'test': -1001710129231
    }


class DevelopmentConfig(BaseConfig):
    HOST = '0.0.0.0'
    PORT = os.getenv('PORT', default=5000)

    APP_URL = 'https://telegram-getcourse-template.herokuapp.com'

    MYSQL_HOST = 'eu-cdbr-west-03.cleardb.net'
    MYSQL_USER = 'b539ea2c40b7ce'
    MYSQL_DB = 'heroku_36efc482b0d6b19'


class TestingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass
