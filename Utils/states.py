from aiogram.fsm.state import State,StatesGroup

class TakeLoan(StatesGroup):
    term=State()
    amount=State()


class TakeDeposit_Alfa(StatesGroup):
    amount=State()
    rate_percent=State()
    period=State()

class TakeDeposit_Sber(StatesGroup):
    amount=State()
    rate_percent=State()
    period=State()
    
    

    
    