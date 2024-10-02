from aiogram import Router
from .base_commands import router as router_base_commands
from .admin_commands import router as  router_admin_commands

router=Router()
router.include_routers(router_admin_commands,router_base_commands)


