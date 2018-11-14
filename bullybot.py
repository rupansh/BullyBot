from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "ENTER_TOKEN"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

boi = 0
bullysubject = []


@dp.message_handler(commands=['bullystop'])
async def disable(message: types.Message):
    global boi
    boi = 68
    await message.reply("keh")


@dp.message_handler(commands=['bully'])
async def bully(message: types.Message):
    global boi
    global bullysubject
    args = message.get_full_command()
    bullysubject.append(int(args[1]))
    boi = 0
    await message.reply("bullying this boi")


@dp.message_handler()
async def bullyreply(message: types.Message):
    if message.from_user.id in bullysubject and boi == 0:
        await message.reply("you gay boi")
        print(bullysubject)

if __name__ == '__main__':
    executor.start_polling(dp)
