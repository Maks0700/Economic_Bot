from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import Message
import re

class Range_Func(BaseFilter):
    async def __call__(self,message:Message) -> Any:
        if message.text.isnumeric():
            if int(message.text) in range(10_000,50_000):
                return True
        return 
    