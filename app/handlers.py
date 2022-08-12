from app import conf, app, bot, mysql_query


@bot.message_handler(commands=['start', 'help', 'info'], chat_types='private')
def message_start(message):
    bot.send_message(chat_id=message.chat.id, text=conf.BOT_REPLY['GREETING'])


@bot.message_handler(regexp='([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', chat_types='private')
def message_email(message):
    pass
