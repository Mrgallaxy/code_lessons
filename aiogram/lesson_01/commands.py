from aiogram.types import Message
import logging
from aiogram.filters import Command, CommandStart
from aiogram import Router, F

rt = Router()


#!команда старт
@rt.message(CommandStart())
async def start(message: Message):
    await message.reply("Привет!")
#! команда
@rt.message(Command('help'))
async def help(message: Message):
    await message.reply("это команда /help")

#!отловка через ф фильтра
@rt.message(F.text == "как дела?")
async def how_are_you(message: Message):
    await message.reply("хорошо!")

#! отловка фото через ф фильтра
@rt.message(F.photo)
async def photo(message: Message):
  global messages
  messages = message.photo[-1].file_id
  await message.reply(f"photo saved")

#!отрпавка фото по айди
@rt.message(Command('get_photo'))
async def get_photo(message: Message):
  await message.answer_photo(photo=f"{messages}", description="your photo")



