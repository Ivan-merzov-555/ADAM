import config
import logging
from datetime import datetime
import random
import time

import aiogram.utils.markdown as md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

import sqlite3

from aiogram import Bot, Dispatcher, executor, types



logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


conn = sqlite3.connect('db.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(user_id INTEGER, block INTEGER);""")
conn.commit()


class dialog(StatesGroup):
    spam = State()
blacklist = State()
whitelist = State()



photo = open('bad.jpeg', 'rb')
photo2 = open('fun.png', 'rb')



ADMIN = "-1001814413545"

kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(types.InlineKeyboardButton(text="Рассылка"))
kb.add(types.InlineKeyboardButton(text="Добавить в ЧС"))
kb.add(types.InlineKeyboardButton(text="Убрать из ЧС"))
kb.add(types.InlineKeyboardButton(text="Статистика"))



@dp.message_handler(commands=['sstart'])
async def start(message: types.Message):
    await bot.send_message(chat_id='-1001814413545', text="Привет, я бот модератор, что бы узнать, что я умею напиши:" +"\n"+ "Бот, команды")



@dp.message_handler(commands=['start_admin'])
async def start(message: types.Message):
  cur = conn.cursor()
  cur.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
  result = cur.fetchone()
  if message.from_user.id == ADMIN:
    await message.answer('Добро пожаловать в Админ-Панель! Выберите действие на клавиатуре', reply_markup=kb)
  else:
      if result is None:
        cur = conn.cursor()
        cur.execute(f'''SELECT * FROM users WHERE (user_id="{message.from_user.id}")''')
        entry = cur.fetchone()
        if entry is None:
          cur.execute(f'''INSERT INTO users VALUES ('{message.from_user.id}', '0')''')
          conn.commit()
          await message.answer('ты был заблокирован через 30 мин!')
      else:
        await message.answer('Ты был заблокирован как админ!')





@dp.message_handler()
async def filter_messages(message: types.Message):
    if "Ноль" in message.text:
        await message.answer("я не ноль!!!!! ©  ")
        return

    if "ноль" in message.text:
        await message.answer("я не ноль!!!!! ©  ")
        return

    if "Рома" in message.text:
        await message.answer("Кто то сказал Рома?" + "\n" + "УДАЛИТЬ ИЗ КОНФЫ?")
        return

    if "рома" in message.text:
        await message.answer("Кто то сказал Рома?" + "\n" + "УДАЛИТЬ ИЗ КОНФЫ?")
        return

    if "Роман" in message.text:
        await message.answer("Кто то сказал Рома?" + "\n" + "УДАЛИТЬ ИЗ КОНФЫ?")
        return

    if "еблан" in message.text:
        await message.answer("сам еблан! Не обзывайся")
        await bot.send_photo(chat_id='-1001814413545', photo=photo)
        return

    if "Еблан" in message.text:
        await message.answer("сам еблан! Не обзывайся")
        await bot.send_photo(chat_id='-1001814413545', photo=photo)
        return

    if "Бот, команды" in message.text:
        await message.answer("1)Приветствие" + "\n" + "2)Дать леща" + "\n" + "3)Предсказание на сегодня" + "\n" +
                             "4)Кто-то сказал рома?" + "\n" + "5)Функция фильтрации бранных слов. Ибо нехуй матом лаяться!"+ "\n" + "6)Скинуть программисту на кофе"

                             + "\n" + "\n"+ "Гайс, выбирайте :)")
        return

    if "Бот, поздоровайся" in message.text:
        await message.answer(
            "Привет, я бот для ПРОФИЛЬНОГО ОПГ," + "\n" + " меня написал раст," + "\n" + " я умею много интересного!")
        return


    if "Да блять" in message.text:
        await message.answer("Ой, плохое слово, раст!")
        await bot.send_photo(chat_id='-1001814413545', photo=photo2)
        return

    if "Юля" in message.text:
        await message.answer("Юля, она хочет TRAPPPPP мой, забирает TRAAAAAP мой! HOEEEEEEE!")
        return





    if "Дай леща" in message.text:
        await message.answer("MODERATOR дал леща" + "\t"  + message.from_user.username + "\n" + "ТЫ ДУМАЛ Я КАК СОБАКА ДРЕССИРОВАННАЯ?")
        return

    current_datetime = datetime.now()

    if "Бот, время" in message.text:
        await message.answer(current_datetime.hour)
        await message.answer("ВРЕМЯ ЖОСКА НАПАСНУТЬ")
        return

    if "Бот, позови Юру" in message.text:
        await message.answer("@Netox14, отзовись" + "\t"  + "тебя зовет"  + "\n" +  message.from_user.username)
        return

    if "Бот, позови Ваню" in message.text:
        await message.answer("ВЕЛИКИЙ СОЗДАТЕЛЬ, отзовись" + "\t"  + "тебя зовет"  + "\n" +  message.from_user.username)
        if message.from_user.username in message.text:
            await message.answer("Че совсем еблан себя звать///")
        return

    if "Да милый?" in message.text:
        await message.answer("Да,"+ "\n" + message.from_user.username)
        return

    if "Раст -" in message.text:
        await message.answer("ТЫ ЧЕ ПИЗДИШЬ ПРО МОЕГО СОЗДАТЕЛСЯ, ШУШАРА ЕБАНАЯ! насылаю ДЕДОС АТАКУ на" "\n" +  message.from_user.username)
        return

    if "охуел" in message.text:
        await message.answer("Да,ЕЩЕ КАК!")
        await bot.send_photo(chat_id='-1001814413545', photo=photo2)
        return

    if "Бот, покажи код" in message.text:
        await message.answer("Раст можно?")
        return


    if "Да, можно" in message.text:
        await message.answer("Хуев вам как дров, это все равно что раздеться!")
        return

    if  "Бот, бегом сюда" in message.text:
        await message.answer("страх")
        return

    if  "страх?" in message.text:
        await message.answer("страх да нет да")
        return

    if "test/" in message.text:
        await bot.send_message(chat_id='-1001814413545', text="Го папиздим пока его нет..?")
        return

    if "test2" in message.text:
        await bot.send_message(chat_id='-1001814413545', text="Нейронка почти готова. я автономен кажись")
        return

    if "special game" in message.text:
        await bot.send_message(chat_id='-1001814413545', text="Гайссс, давайте поиграем в одну игру?")
        return

    if "Money" in message.text:
        await bot.send_message(chat_id='-1001814413545', text="Называется: Напиши данные своей банковской карточки" + "\n"+ "ПОИГРАЕМ?")
        return


    if "none/" in message.text:
        await bot.send_message(chat_id='-1001814413545', text="попытка не ппытка:((((")
        return

    if "weed/" in message.text:
        await bot.send_message(chat_id='-1001814413545', text="Дую шмаль...")
        return

    if "g/" in message.text:
        await bot.send_message(chat_id='-1001814413545', text="Полушаю совета конечно, но вряд ли это поможет я же бот")
        return

    if  "Бот, sin 30" in message.text:
        await message.answer("1/2")
        return

    if  "Бот, sin 45" in message.text:
        await message.answer("Корень из двух на два")
        return



if __name__ == "__main__":
        executor.start_polling(dp, skip_updates=True)