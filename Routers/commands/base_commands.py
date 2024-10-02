from contextlib import suppress
from aiogram import F,types,Router
from aiogram.enums import ParseMode
from aiogram.filters import Command,CommandStart
from aiogram.utils import markdown
from motor.core import AgnosticDatabase as MDB
from Keyboards.keyboards_common import inline_keyboard_builder
from pymongo.errors import DuplicateKeyError 
router=Router()




@router.message(CommandStart())
@router.callback_query(F.data=="main_page")
async def com_start(message:types.Message|types.CallbackQuery,data_base:MDB):
    with suppress(DuplicateKeyError):
        await data_base.maks.insert_one( #insert in collections data
            dict(
                _id=message.from_user.id,
                balance=100,
                bank={
                    "currence":[0,0],
                    "loans":
                        {
                            "total_amount":0,
                            "repaid":{"amount":0,"when":[]},
                            "when":{"start":"","end":""}
                        },
                    "deposit":{"total_amount":0,"when":""}
                    
                    
                },
                actives={"total_amount":0,"items":[]},
                passives={"total_amount":0,"items":[]},
                businesses={"total_amount":0,"items":[]}
                
            ))
    pattern=dict(
            text=markdown.text(
                markdown.hbold("Let's go to buiseness!!")),
            reply_markup=inline_keyboard_builder(
        ["👤Профиль","💰Банк","📈Рынки"],
        ["profile","bank","markets"]
        )
                )
                
        
    
    
    if isinstance(message,types.CallbackQuery):
        
        await message.message.answer(**pattern)#message==query(CallbackQuery)
        await message.answer()
    else:
        await message.answer(**pattern)
        
            
        
    

    