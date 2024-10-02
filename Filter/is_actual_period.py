from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import Message
import re


class Period_Correct(BaseFilter):
    async def __call__(self,period_total:Message) -> Any:# The creating call for define period (in the OOP calling method)
        regex=re.compile(r"(^[1-9]$)|(^1[0-2]$)")#reg express to filter the period
        return True if regex.search(period_total.text) else False

class check_on_text(BaseFilter):
    async def __call__(self,message:Message) -> Any:
        if message.text:
            await message.answer("Intrinsic buttons!!")
        
            
            
    