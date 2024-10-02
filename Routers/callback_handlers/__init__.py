from .main_callbacks import router as call_routers
from .callback_loans import router as extra_routers
from .callbacks_deposit import router as deposit_router
from aiogram import F,Router
router=Router()
router.include_routers(call_routers,extra_routers,deposit_router)
