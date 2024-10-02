from .callback_bitcoin import router as bitcoin_router
from .callback_ethereum import router as ethereum_router
from aiogram import Router

router=Router()
router.include_routers(bitcoin_router,ethereum_router)
