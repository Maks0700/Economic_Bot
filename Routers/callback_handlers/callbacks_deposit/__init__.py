from .callback_deposit import router as deposit_router
from .callback_alfa_bank import router as alfa_router
from .callback_sberbank import router as sber_router
from aiogram import Router

router=Router()

router.include_routers(deposit_router,alfa_router,sber_router)

