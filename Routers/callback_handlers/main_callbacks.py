from aiogram import F,Router
from aiogram.types import CallbackQuery
from motor.core import AgnosticDatabase as MDB
from aiogram.utils.markdown import hcode,hbold
from Keyboards.keyboards_common import inline_keyboard_builder
from Keyboards.callback_market import keyboard_create_currency
from Keyboards.callback_market import Calculations_Asks,Currency_Digit,Available_Currency
from aiogram.fsm.context import FSMContext
router=Router()

@router.callback_query(F.data=="profile")
async def show_profile(query:CallbackQuery,data_base:MDB):
    user=await data_base.maks.find_one(dict(#define our user with his id and add him to collections
        _id=query.from_user.id))
    await query.message.answer(
        f"ID: {hcode(query.from_user.id)}\n\n" #thanks to find user_id using his collections data and adding to bot
        f"Balance: {hcode(user['balance'])} $\n\n"
        f"Actives: {hcode(user['actives']['total_amount'])} $\n\n"
        f"Passsives: {hcode(user['passives']['total_amount'])} $\n\n"
        f"Businesses: {hcode(user['businesses']['total_amount'])} $",
        reply_markup=inline_keyboard_builder("⬅️ Back","main_page")
        
        
    )
@router.callback_query(F.data=="bank")
async def bank_callback(query:CallbackQuery,data_base:MDB):
    user=await data_base.maks.find_one(dict(_id=query.from_user.id))
    pattern=dict(
        text=f"Number of purchases: {hcode(round(user['bank']['currence'][0],2))}💲\n"
        f"Number of sales: {hcode(round(user['bank']['currence'][1],2))}💲\n\n"
        f"Loans: {hcode(user['bank']['loans']['total_amount'])}$\n\n"
        f"Deposit: {hcode(user['bank']['deposit']['total_amount'])}$\n\n"
        
    )
    await query.message.answer(**pattern,reply_markup=inline_keyboard_builder(["Кредит","Депозит","⬅️ Back"],["loans","deposit","main_page"]))
    
@router.callback_query(F.data=="markets")

async def market_currency(call:CallbackQuery,data_base:MDB):
    await call.message.answer(hbold("Введите интересующую Вас криптовалюту!!!"),reply_markup=keyboard_create_currency())

    
    

    