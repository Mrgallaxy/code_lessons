from aiogram import Bot, Dispatcher, F
import asyncio
from aiogram.types import Message
import logging
from aiogram.filters import Command, CommandStart
from commands import rt as router
API_TOKEN = 'CHANGE TO YOUR BOT TOKEN'

#! бот и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


debug = False

async def on_startup():
  if debug == True:
    logging.basicConfig(level=logging.DEBUG)
  else:
    pass
  dp.include_router(router)
  print("handlers succes:wq")
  print(f'Бот {bot.id} запущен')
  await dp.start_polling(bot, skip_updates=True)



if __name__ == '__main__':
  try:
    asyncio.run(on_startup())
  except KeyboardInterrupt:
    print('Прервано пользователем.')
