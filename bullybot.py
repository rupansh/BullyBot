import telebot

TOKEN = "ENTER_TOKEN"
bot = telebot.TeleBot(TOKEN)

boi = [0]


@bot.message_handler(commands=['bullystop'])
def disable(message):
    boi.append(68)
    bot.reply_to(message, "stopping bully")


@bot.message_handler(commands=['bullystart'])
def enable(message):
    boi.append(69)
    if 68 in boi:
        boi.remove(68)
    bot.reply_to(message, "initiate cyber bullying")


@bot.message_handler()
def gay(message):
    if message.from_user.id == int("Telegram_ID") and 69 in boi and 68 not in boi:
        bot.reply_to(message, "you gay boi")


bot.polling()
