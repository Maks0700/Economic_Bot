from aiogram.types import Message
from aiogram import Router,F
from magic_filter import RegexpMode
from config import settings
from re import Match
from Filter.test_filter import IsAdmin

router=Router()
# @router.message(IsAdmin(settings.admin_is))
# @router.message(F.from_user.id.in_(settings.admin_is))
@router.message(F.text.regexp(r"(^0[1-7]\.11$)",mode=RegexpMode.SEARCH).as_("secret_word") or IsAdmin(settings.admin_is))
async def admin_message(message:Message):
        await message.answer("Hi, admin!")
        
    
        




