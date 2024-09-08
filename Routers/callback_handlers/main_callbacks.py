from aiogram import F,Router
from aiogram.types import CallbackQuery
from motor.core import AgnosticDatabase as MDB
from aiogram.utils.markdown import hcode
from Keyboards.keyboards_common import inline_builder


router=Router()

@router.callback_query(F.data=="profile")
async def show_profile(query:CallbackQuery,data_base:MDB):
    user=await data_base.maks.find_one(dict(
        _id=query.from_user.id))
    await query.message.edit_text(
        f"ID: {hcode(query.from_user.id)}\n\n"
        f"Balance: {hcode(user['balance'])} $\n\n"
        f"Actives: {hcode(user['actives']['total_amount'])} $\n\n"
        f"Passsives: {hcode(user['passives']['total_amount'])} $\n\n"
        f"Businesses: {hcode(user['businesses']['total_amount'])} $",
        reply_markup=inline_builder("⬅️ Back","main_page")
        
        
    )
@router.callback_query(F.data=="bank")
async def bank_callback(query:CallbackQuery,data_base:MDB):
    user=await data_base.maks.find_one(dict(_id=query.from_user.id))
    pattern=dict(
        text=
        f"Currencies: {hcode(user['bank']['currence'][0])}💴"
        f" {hcode(user['bank']['currence'][1])}💶"
        f" {hcode(user['bank']['currence'][2])}💷\n\n"
        f"Loans: {hcode(user['bank']['loans']['total_amount'])}$\n\n"
        f"Deposit: {hcode(user['bank']['deposit']['total_amount'])}$\n\n"
        
    )
    await query.message.edit_text(**pattern,reply_markup=inline_builder(["Кредит","Депозит","⬅️ Back"],["loans","deposit","main_page"]))
     
    

    