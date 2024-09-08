from aiogram import Router
from .commands import router as router_commands
from .callback_handlers import router as callback_router
__all__=("router")
router=Router()
router.include_routers(router_commands,callback_router)
