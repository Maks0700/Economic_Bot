from aiogram.types import CallbackQuery,Message
from aiogram import Router,F
from magic_filter import RegexpMode
from motor.core import AgnosticDatabase as MDB
from aiogram.utils.markdown import hcode
from Keyboards.keyboards_common import inline_builder
from aiogram.fsm.context import FSMContext
from Utils.states import TakeLoan
from Filter.is_digit import IsDigit
import pendulum
import re
router=Router()
@router.callback_query(F.data=="loans")
async def loan_call_process(query:CallbackQuery,data_base:MDB,state:FSMContext):
    user=await data_base.maks.find_one(dict(_id=query.from_user.id))
    user['bank']['loans']['when']['start']=""
    await state.set_state(TakeLoan.term)
    await query.message.answer("How a long time do you want to take a loan?")
    await query.answer()#?????? I don t know 
    

@router.message(TakeLoan.term,F.text.regexp(r"^[1-9]?$",mode=RegexpMode.SEARCH).as_("digit"))
async def take_loand_user(message:Message,state:FSMContext,digit:re.Match[str]):
    
    await state.update_data(term_value=digit.group())
    await state.set_state(TakeLoan.amount)
    await message.answer(hcode("Enter amount!!"))


@router.message(TakeLoan.term)
async def check_term(message:Message):
    await message.reply("Enter your term is correct")


@router.message(TakeLoan.amount,IsDigit())
async def amount_process(message:Message,state:FSMContext,data_base:MDB):
    
    if int(message.text)<0 and int(message.text)>1_000:
        await message.answer("Enter again amount!!")
    else:
        amount_total=int(message.text)
        await state.update_data(amount=amount_total)
        data=await state.get_data()
        await state.clear()
        await message.answer("You are applied your loan and amount in database!!Congratulations!!",
                             reply_markup=inline_builder("⬅️Back","bank"))
        current_datetime=pendulum.now("UTC")#define current datetime
        end_datetime=current_datetime.add(int(data["term_value"]))#define end_time
    await data_base.maks.update_one(
        {"_id":message.from_user.id},
        {
            "$inc":{"balance":amount_total},
            "$set":{"bank.loans.when.start":current_datetime,"bank.loans.when.end":end_datetime,"bank.loans.total_amout":amount_total}
            
            
            
        }
    )    
    
    
    
