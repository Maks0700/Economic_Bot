from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import Message
import re

class IsDigit(BaseFilter):
    async def __call__(self,message:Message) -> Any:
        pattern=re.compile(pattern=r"^\d+(\.\d+)?$")
        return True if pattern.search(message.text) else False


