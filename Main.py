from aiogram import Bot,Dispatcher
import asyncio
from aiogram.enums import ParseMode
from config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import suppress
from pymongo.errors import DuplicateKeyError
from Routers import router as main_router

# from Middleware.antiflood import Antflood





async def main():
    
    bot=Bot(settings.bot_token,parse_mode=ParseMode.HTML)
    dp=Dispatcher()
    dp.include_routers(main_router)
    # dp.message.middleware(Antflood(time_limit=2))
    cluster=AsyncIOMotorClient("mongodb+srv://rukhlya1999:DBusp3zgptDsSngG@cluster0.je225.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    data_base=cluster.test_db
    
    
    
    await bot.delete_webhook(True)
    try:
        print("Success!!")
        await dp.start_polling(bot,data_base=data_base)
    except TypeError as T_E:
        print("Error!")
    
    
if __name__=="__main__":
    asyncio.run(main())
    









