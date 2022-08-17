from app import conf, app, bot


if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f'{conf.APP_URL}/{conf.BOT_KEY}')

    app.run(host=conf.HOST, port=conf.PORT)
