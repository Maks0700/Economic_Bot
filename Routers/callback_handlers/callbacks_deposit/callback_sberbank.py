from aiogram.types import CallbackQuery,Message
from aiogram import Router,F

from motor.core import AgnosticDatabase as MDB
from Keyboards.keyboards_common import inline_keyboard_builder
from aiogram.fsm.context import FSMContext
from Utils.states import TakeDeposit_Sber
from Keyboards.callback_data_for_bank import (
    Interest_Rate_Sber, 
    Rate_Choose_Sber, 
    Bank, Choose_Bank, 
    inline_keyboard_bank,
    inline_sber_keyboard)
from Filter.is_actual_period import Period_Correct
import pendulum
from Filter.range_func import Range_Func
from aiogram.utils.markdown import hbold


router=Router()

@router.callback_query(Bank.filter(F.bank==Choose_Bank.sber))
async def sber_bank(call:CallbackQuery,state:FSMContext,data_base:MDB):
    user=await data_base.maks.find_one(dict(_id=call.from_user.id))
    user["bank"]["deposit"]=""
    await call.message.answer(hbold("Введите сумму депозита!!"))
    await state.set_state(TakeDeposit_Sber.amount)

@router.message(TakeDeposit_Sber.amount,Range_Func())
async def amount_sber(message:Message,state:FSMContext):
    await message.answer(f"Выберите процентную ставку!!",reply_markup=inline_sber_keyboard())
    await state.update_data(amount_total=int(message.text))
    await state.set_state(TakeDeposit_Sber.rate_percent)
    
@router.message(TakeDeposit_Sber.amount)
async def error_amount(message:Message):
    await message.reply("Enter correct amount!!")

@router.callback_query(Rate_Choose_Sber.filter((F.choose_percent==Interest_Rate_Sber.max_percent)|(F.choose_percent==Interest_Rate_Sber.pension_rate)),TakeDeposit_Sber.rate_percent)
async def rate_percent(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Введите срок депозита!!")
    await state.set_state(TakeDeposit_Sber.period)

@router.message(TakeDeposit_Sber.rate_percent)
async def error_rate(message:Message):
    await message.reply("Пользуйтесь встроенными кнопками!!",reply_markup=inline_sber_keyboard())

@router.message(TakeDeposit_Sber.period,Period_Correct())
async def period_sber(message:Message,state:FSMContext,data_base:MDB):
    await message.answer(hbold("Спасибо за Ваш выбор Сбербанка.Теперь ваши данные находятся PyMongo.Предлагаю вернуться в основное меню"),
                         reply_markup=inline_keyboard_builder(
                             "⬅️ Back",callback_data="main_page"
                         )
    )
    await state.update_data(period=int(message.text))
    data=await state.get_data()
    await state.clear()
    current_datetime=pendulum.now("UTC")
    
    await data_base.maks.update_one(
        dict(_id=message.from_user.id),
        {
            "$set":{
                "bank.deposit.total_amount":data["amount_total"],
                "bank.deposit.when":current_datetime
                }
            
            
        }
    )

@router.message(TakeDeposit_Sber.period)
async def error_period(message:Message):
    await message.reply("Enter correct period!!")    
    
    
