import os


class BaseConfig:
    BOT_REPLY = {
        'GREETING': 'Для получения ссылки на закрытый канал Азама Ходжаева напишите адрес электронной почты, указанный при Вашей покупке.',
        'INVALID_EMAIL': 'Адрес электронной не найден или уже используется. Если произошла ошибка, пожалуйста, свяжитесь с технической поддержкой @azamkhodzhaev_bot',
        'INVITE': 'Ваша ссылка на Telegram-канал ({title}): {link}',
        'PAYMENT_EXPIRED': 'Ваш период оплаты курса закончился. Если произошла ошибка, пожалуйста, свяжитесь с технической поддержкой @azamkhodzhaev_bot'
    }

    RATE = {
        "Тариф - Base x1": -1001611757287,
        "Тариф - Base x3": -1001611757287,
        "Тариф - Base x6": -1001667337121,
        "Тариф - VIP x6": -1001661589284,
        "Тариф - Super VIP x12": -1001601848724
    }


class DevelopmentConfig(BaseConfig):
    HOST = '0.0.0.0'
    PORT = os.getenv('PORT', default=5000)

    APP_URL = 'https://.herokuapp.com'
    APP_KEY = os.getenv('DEVELOPMENT_APP_KEY')

    BOT_KEY = os.getenv('DEVELOPMENT_BOT_TOKEN')

    MYSQL_HOST = ''
    MYSQL_USER = ''
    MYSQL_PASSWD = os.getenv('DEVELOPMENT_MYSQL_PASSWD')
    MYSQL_DB = ''


class TestingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass
