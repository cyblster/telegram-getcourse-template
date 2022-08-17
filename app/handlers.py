from app import conf, app, bot, mysql_query

from telebot import types


@bot.message_handler(commands=['start', 'help', 'info'], chat_types='private')
def message_start(message):
    bot.send_message(chat_id=message.chat.id, text=conf.BOT_REPLY['GREETING'])


@bot.message_handler(regexp='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', chat_types='private')
def message_email(message):
    email = message.text.lower()
    telegram_username = message.from_user.username
    telegram_firstname = message.from_user.first_name
    telegram_lastname = message.from_user.last_name

    for payment_rate, telegram_id in mysql_query(f'SELECT payment_rate, telegram_id FROM customer WHERE email = "{email}"'):
        invite_link = bot.create_chat_invite_link(chat_id=conf.APP_RATE[payment_rate], expire_date=86400, member_limit=1).invite_link

        mysql_query(f'UPDATE customer SET telegram_username = "{telegram_username}" telegram_firstname = "{telegram_firstname}", telegram_lastname = "{telegram_lastname}", invite_link = "{invite_link}"')

        inline_keyboard = types.InlineKeyboardMarkup()
        inline_keyboard.add(types.InlineKeyboardButton(text='Перейти на канал', callback_data='channel_referer_button'))

        bot.send_message(chat_id=telegram_id, text='123', reply_markup=inline_keyboard)

    bot.send_message(chat_id=message.from_user.id, text='success')


@bot.callback_query_handler(func=lambda call: call.data == 'channel_referer_button')
def callback_inline(call):
    pass
