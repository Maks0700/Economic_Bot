from aiogram.fsm.state import State,StatesGroup

class TakeLoan(StatesGroup):
    term=State()
    amount=State()