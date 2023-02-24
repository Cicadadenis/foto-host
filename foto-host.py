import logging
import os
import requests
import json, time

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile
from aiogram.utils import executor


re = "\033[1;31m"
gr = "\033[1;32m"
cy="\033[1;36m"

logo = (
            f"                    _             __         {re}___       __{cy}\n"
            f"               ____(_)______ ____/ /__ _____{re}/ _ )___  / /_{cy}\n"
            f"              / __/ / __/ _ `/ _  / _ `/___{re}/ _  / _ \/ __/{cy}\n"
            f"              \__/_/\__/\_,_/\_,_/\_,_/   {re}/____/\___/\__/{cy}\n"
            f"              ----------Telegram-Bot-Cicada3301-----------\n\n"
)
re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"
try:
    BOT_TOKEN = open("token.txt", "r").read()
except:
    print(logo)
    BOT_TOKEN = input(" Введи токен бота зарание нажав в нем старт: ")
    with open("token.txt", "w") as f:
        f.write(BOT_TOKEN)
papka = os.listdir()
if "photos" not in papka:
    os.mkdir("photos")
BOT_TOKEN = open("token.txt", "r").read()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

MethodGetMe = (f'''https://api.telegram.org/bot{BOT_TOKEN}/GetMe''')
response = requests.post(MethodGetMe)
tttm = response.json()
tk = tttm['ok']
if tk == True:
    id_us = (tttm['result']['id'])
    first_name = (tttm['result']['first_name'])
    username = (tttm['result']['username'])
    os.system('cls')
    print(logo)

    print(f"""
                ---------------------------------
                🆔 Bot id: {id_us}
                ---------------------------------
                👤 Имя Бота: {first_name}
                ---------------------------------
                🗣 username: @{username}
                ---------------------------------
                🌐 https://t.me/{username}
                ---------------------------------
                ******* Suport: @Satanasat ******
    """)
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    photo = message.photo[-1]
    photo_path = f'photos/{photo.file_id}.jpg'
    await photo.download(photo_path)
    while True:
        response = requests.post(
            url='https://telegra.ph/upload',
            files={'file': open(photo_path, 'rb')}
        )
        try:
            yy = response.text.split('\\')[2]
            tt = yy.split('"')[0]

            photo_url = 'https://telegra.ph/file' + tt

            await message.reply(
                f'Фото загружено: \n{photo_url}',
                disable_web_page_preview=True,
            )
            break
        except:
            pass
    os.remove(photo_path)

if __name__ == '__main__':
    
    os.makedirs('photos', exist_ok=True)
    
    executor.start_polling(dp, skip_updates=True)