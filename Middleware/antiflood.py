from typing import Callable,Dict,Any,Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message,TelegramObject
from cachetools import TTLCache

class Antflood(BaseMiddleware):
    def __init__(self,time_limit:int) -> None:
        self.limit=TTLCache(10_000,ttl=time_limit)#the limit is 10_000 users in chat bot
    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message, data: Dict[str, Any]) -> Any:
        if event.chat.id in self.limit:#verification current user in chat bot
            return #decline actions and await ttl
        self.limit[event.chat.id]=None #clear cache chat.id
        await handler(event,data)#after ttl to make actions handlers
        
         
        
        
    