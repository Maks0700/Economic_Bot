from aiogram import F,Router
from aiogram.types import Message,CallbackQuery
from Keyboards.callback_market import (
Available_Currency,
Currency_Digit,
return_choose_currency)
import requests
from aiogram.utils.markdown import hbold
from re import Match
from magic_filter import RegexpMode
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown
from Keyboards.callback_market import Calculations_Asks
from Keyboards.callback_market import calc_eth
from contextlib import suppress
from motor.core import AgnosticDatabase as MDB


router=Router()
@router.callback_query(Currency_Digit.filter(F.currency==Available_Currency.Ethereum))
async def process_eth(call:CallbackQuery,state:FSMContext):
    await call.message.answer(
        ("Введите лимит на ордер эфира, для расчета контрольной суммы!"))
    await state.set_state(Calculations_Asks.limit_eth)

    
@router.message(F.text.isdigit(),Calculations_Asks.limit_eth)
async def process_ask(message:Message,state:FSMContext,data_base:MDB):
    await state.clear()
    await state.update_data(limit_value=(message.text))
    data=await state.get_data()
    
    
    result_asks=calc_eth(limit=int(data["limit_value"]))
    
    await message.answer((hbold("Количество покупок на рынке составляет ") + 
                          f"<u>{round(result_asks[0],2)}$</u>.\n"+
                          hbold("Количество продаж составляет ")+
                          f"<u>{round(result_asks[1],2)}$</u>."),reply_markup=return_choose_currency())
    await data_base.maks.update_one(
        dict(_id=message.from_user.id),
        {
            "$set":
            {
                "bank.currence":result_asks   
            }
        }
    )
    
        
@router.message(Calculations_Asks.limit_eth)
async def error_message_limit(message:Message):
    with suppress(ValueError):
        await message.reply("Введите корректное значение лимита!!!")
    
    
    
    



    
    
    






