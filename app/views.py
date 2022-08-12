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
@app.route(rule=f'{conf.APP_KEY}/customer_add', methods=['GET'])
def customer_add():
    payment_link = request.args.get('payment_link')
    payment_rate = request.args.get('payment_rate')
    email = request.args.get('email')

    if not payment_link:
        return '', 400

    if not payment_rate:
        return '', 400

    if not email:
        return '', 400

    payment_id = payment_link.split('/')[-1]

    mysql_query(f'INSERT INTO customer (payment_id, payment_rate, email) VALUES ("{payment_id}", "{payment_rate}", "{email}")')

    return '', 200


@app.route(rule=f'{conf.APP_KEY}/customer_remove', methods=['GET'])
def customer_remove():
    payment_link = request.args.get('payment_link')

    if not payment_link:
        return '', 400

    payment_id = payment_link.split('/')[-1]

    payment_rate, telegram_id = mysql_query(f'SELECT payment_rate, telegram_id FROM customer WHERE payment_id = "{payment_id}"')
    bot.kick_chat_member(chat_id=conf.RATE[payment_rate], user_id=telegram_id, until_date=60)
    bot.send_message(chat_id=telegram_id, text=conf.BOT_REPLY['PAYMENT_EXPIRED'])

    mysql_query('DELETE FROM customer WHERE payment_id = "{payment_id}"')

    return '', 200


@app.route(rule=f'{conf.APP_KEY}/customer_info_by_email', methods=['GET'])
def customer_info_by_email():
    pass
