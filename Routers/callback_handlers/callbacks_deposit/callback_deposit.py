from aiogram.types import CallbackQuery
from aiogram import Router,F
from aiogram.utils.markdown import hcode
from Keyboards.keyboards_common import inline_keyboard_builder
from Keyboards.callback_data_for_bank import inline_keyboard_bank,Choose_Bank,Bank
from motor.core import AgnosticDatabase as MDB
from aiogram.types import Message
from aiogram.utils.markdown import hbold



router=Router()

@router.callback_query(F.data=="deposit")
async def choose_bank(call:CallbackQuery):
    await call.message.answer(hbold("Choose your favorite bank"),reply_markup=inline_keyboard_bank(["Сбербанк","Альфа-Банк","⬅️ Back"]))
    

@router.callback_query(Bank.filter(F.bank==Choose_Bank.menu))
async def menu(call:CallbackQuery,data_base:MDB):
    user=await data_base.maks.find_one(dict(_id=call.from_user.id))
    pattern=dict(
        text=
        f"Number of purchases: {hcode(round(user['bank']['currence'][0],2))}💲\n"
        f"Number of sales: {hcode(round(user['bank']['currence'][1],2))}💲\n\n"
        f"Loans: {hcode(user['bank']['loans']['total_amount'])}$\n\n"
        f"Deposit: {hcode(user['bank']['deposit']['total_amount'])}$\n\n"
        
    )
    
    await call.message.answer(**pattern,reply_markup=inline_keyboard_builder(["Кредит","Депозит","⬅️ Back"],["loans","deposit","main_page"]))



    
    
    



