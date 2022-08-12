from app import conf, app, bot


if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=conf.APP_URL)

    app.run(host=conf.HOST, port=conf.PORT)
