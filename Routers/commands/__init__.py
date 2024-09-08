from aiogram import Router
from .base_commands import router as router_base_commands

router=Router()
router.include_routers(router_base_commands)


