# from typing import Callable,Dict,Any,Awaitable
# from aiogram import BaseMiddleware
# from aiogram.types import Message,TelegramObject
# from cachetools import TTLCache

# class Antflood(BaseMiddleware):
#     def __init__(self,time_limit:int) -> None:
#         self.limit=TTLCache(10_000,ttl=time_limit)
#     async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message, data: Dict[str, Any]) -> Any:
#         if event.chat.id in self.limit:
#             return
#         self.limit[event.chat.id]=None
#         await handler(event,data)
        
         
        
        
    