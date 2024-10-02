from aiogram.types import CallbackQuery,Message
from aiogram import Router,F
from magic_filter import RegexpMode
from motor.core import AgnosticDatabase as MDB
from aiogram.utils.markdown import hcode
from Keyboards.keyboards_common import inline_keyboard_builder
from aiogram.fsm.context import FSMContext
from Utils.states import TakeDeposit_Alfa
from re import Match
from Keyboards.callback_data_for_bank import (
    Rate_Choose_Alfa, 
    Bank, Choose_Bank, 
    Interest_Rate_Alfa, 
    inline_keyboard_bank,
    inline_alfa_rate)
from Filter.is_actual_period import Period_Correct
import pendulum
from Filter.range_func import Range_Func
from aiogram.utils.markdown import hbold


router=Router()

express_filter_percent=(F.choose_percent==Interest_Rate_Alfa.max_percent)|(F.choose_percent==Interest_Rate_Alfa.pension_rate)
@router.callback_query(Bank.filter(F.bank==Choose_Bank.alfa))
async def proceess_alfa(call:CallbackQuery,state:FSMContext,data_base:MDB):
    user=await data_base.maks.find_one(dict(_id=call.from_user.id))
    user["bank"]["deposit"]=""#update bank in PyMongo
    await call.message.answer(hbold("Введите сумму"))
    await state.set_state(TakeDeposit_Alfa.amount)
    



@router.message(TakeDeposit_Alfa.amount,Range_Func())
async def amount_alfa(message:Message,state:FSMContext):
    
        await message.answer(f"Выберите процентную ставку!",reply_markup=inline_alfa_rate())
        await state.update_data(amount_total=int(message.text))
        await state.set_state(TakeDeposit_Alfa.rate_percent)
    

@router.message(TakeDeposit_Alfa.amount)
async def error_amount(message:Message):
    await message.reply("Пожалуйста, введите корректное значение!!")



    
@router.callback_query(Rate_Choose_Alfa.filter(express_filter_percent),TakeDeposit_Alfa.rate_percent)
async def rate_percent(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Введите период депозита!!")
    await state.update_data(rate=call.message.text)
    await state.set_state(TakeDeposit_Alfa.period)
    
    
@router.message(TakeDeposit_Alfa.rate_percent)
async def error_bank(message:Message):
    await message.reply("Пользуйтесь встроенными кнопками!!",reply_markup=inline_alfa_rate())

@router.message(TakeDeposit_Alfa.period,Period_Correct())
async def period_alfa(message:Message,state:FSMContext,data_base:MDB):
    await message.answer(hbold("Спасибо за Ваш выбор Альфа-Банка.Теперь ваши данные находятся PyMongo.Предлагаю вернуться в основное меню"),
                         reply_markup=inline_keyboard_builder(
                             "⬅️ Back",callback_data="main_page"
                         )
    )
    await state.update_data(period=int(message.text))
    data=await state.get_data()
    await state.clear()
    current_datetime=pendulum.now("UTC")
    
    await data_base.maks.update_one( #in data_base update user parametrs(deposit and current time)
        dict(_id=message.from_user.id),
        {
            "$set":{
                "bank.deposit.total_amount":data["amount_total"],
                "bank.deposit.when":current_datetime
                }
            
            
        }
    )

@router.message(TakeDeposit_Alfa.period)
async def error_period(message:Message):
    await message.reply("Введите корректное значение!!")    
    

    
    
    

    

    







    

 
    




