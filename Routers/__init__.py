from aiogram import Router
from .commands import router as router_commands
from .callback_handlers import router as callback_router
from .Market import router as router_market
__all__=("router",)
router=Router()
router.include_routers(router_commands,callback_router,router_market)
