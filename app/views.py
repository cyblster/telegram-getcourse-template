from app import conf, app, bot, mysql_query
from flask import request
from telebot import types


# Создание и настройка вебхука
@app.route(rule=f'/{conf.BOT_KEY}', methods=['POST'])
def webhook_update():
    json_string = request.get_data().decode('utf-8')
    update = types.Update.de_json(json_string)
    bot.process_new_updates([update])

    return '', 200


# API приложения
@app.route(rule=f'/{conf.APP_KEY}/customer_add', methods=['GET'])
def customer_add():
    payment_id = request.args.get('payment_link').split('/')[-1]
    payment_rate = request.args.get('payment_rate').lower()
    email = request.args.get('email').lower()

    mysql_query(f'INSERT INTO customer (payment_id, payment_rate, email) VALUES ("{payment_id}", "{payment_rate}", "{email}")')

    return '', 200


@app.route(rule=f'/{conf.APP_KEY}/customer_remove', methods=['GET'])
def customer_remove():
    payment_id = request.args.get('payment_link').split('/')[-1]

    payment_rate, telegram_id = mysql_query(f'SELECT payment_rate, telegram_id FROM customer WHERE payment_id = "{payment_id}"')

    if bot.get_chat_member(chat_id=conf.APP_RATE[payment_rate], user_id=telegram_id):
        bot.ban_chat_member(chat_id=conf.APP_RATE[payment_rate], user_id=telegram_id, until_date=60)
        bot.send_message(chat_id=telegram_id, text=conf.BOT_REPLY['PAYMENT_EXPIRED'])

    mysql_query(f'DELETE FROM customer WHERE payment_id = "{payment_id}"')

    return '', 200
