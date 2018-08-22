import telebot

TOKEN = "ENTER_TOKEN"
bot = telebot.TeleBot(TOKEN)

boi = [0]
bullysubject = []


@bot.message_handler(commands=['bullystop'])
def disable(message):
    boi.append(68)
    bot.reply_to(message, "keh")


@bot.message_handler()
def bully(message):
    if message.text.startswith("/bully "):
        bullysubject.clear()
        keh = message.text.replace("/bully ", "", 1)
        bullysubject.append(int(keh))
        while 68 in boi:
            boi.remove(68)
        bot.reply_to(message, "bullying this boi")
    elif message.from_user.id in bullysubject and 68 not in boi:
        bot.reply_to(message, "Get rekt depressed uncle")
        print(bullysubject)


bot.polling()
