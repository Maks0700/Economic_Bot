from typing import Any
from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsAdmin(BaseFilter):
    def __init__(self,num_admin:int) -> bool:#init need to define num_admin value
        self.admin_total=num_admin   
    async def __call__(self,admin_num:Message) -> Any:#method call as likely method is actual_period
        if admin_num.chat.id==self.admin_total:#verification of admin and the current user
            return True
        return False
    

        
