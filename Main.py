from aiogram import Bot,Dispatcher
import asyncio
from aiogram.enums import ParseMode
from config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import suppress
from Routers import router as main_router
from Middleware.antiflood import Antflood
import logging


bot=Bot(settings.bot_token,parse_mode=ParseMode.HTML)
dp=Dispatcher()
logging.basicConfig(level=logging.INFO)
    
dp.include_routers(main_router)
dp.message.middleware(Antflood(time_limit=2))
cluster=AsyncIOMotorClient("mongodb+srv://rukhlya1999:DBusp3zgptDsSngG@cluster0.je225.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")#connect to db
data_base=cluster.test_db


async def main():
    await bot.delete_webhook(True)
    try:
       await dp.start_polling(bot,data_base=data_base)
    except TypeError as T_E:
        print("Error!")
    
    
if __name__=="__main__":
    asyncio.run(main())
    









