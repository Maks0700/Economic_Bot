from aiogram.filters.callback_data import CallbackData
from enum import Enum, auto,IntEnum
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import List

class Choose_Bank(str,Enum):# Choose the bank
    sber=auto()
    alfa=auto()
    menu=auto()


class Bank(CallbackData,prefix="bank"):# Data for bank
    bank:Choose_Bank
    
    
class Interest_Rate_Alfa(str,Enum):#Rate of percent for alfa bank
    max_percent="21%"
    pension_rate="10%"
    

class Interest_Rate_Sber(str,Enum):#Rate of percent for sber bank
    max_percent="25%"
    pension_rate="15%"
    

class Rate_Choose_Alfa(CallbackData,prefix="alfa"):#Callback_Data for selection of interest rate alfa
    choose_percent:Interest_Rate_Alfa
    

class Rate_Choose_Sber(CallbackData,prefix="sber"):#The same previous Call_Data but for sber
    choose_percent:Interest_Rate_Sber


        
def inline_keyboard_bank(bank_choose:List[str]):
    builder=InlineKeyboardBuilder()
    
    [
        builder.button(text=txt,callback_data=Bank(bank=c_b).pack())#Here in call_data equate the bank Call_Data Choose_BaNK
        for txt,c_b in zip(bank_choose,Choose_Bank)#extend list bank_choose and CallData
    ]
    
    builder.adjust(2)
    return builder.as_markup()




def inline_alfa_rate()->InlineKeyboardBuilder:
    builder=InlineKeyboardBuilder()
    for value_num in Interest_Rate_Alfa:#value_num  is the value of the enum

        builder.button(
            text=value_num.value.title(),callback_data=Rate_Choose_Alfa(choose_percent=value_num).pack()#value.title need to text in button
        )
    
    builder.adjust(1)
    return builder.as_markup()

def inline_sber_keyboard()->InlineKeyboardBuilder:
  
    builder=InlineKeyboardBuilder()
    dict_total={
        Interest_Rate_Alfa.max_percent:Rate_Choose_Sber(choose_percent=Interest_Rate_Sber.max_percent),
        Interest_Rate_Sber.pension_rate:Rate_Choose_Sber(choose_percent=Interest_Rate_Sber.pension_rate)}
    [
        builder.button(text=key,callback_data=value.pack())
        for key,value in dict_total.items()
    ]
    builder.adjust(1)
    return builder.as_markup(**dict_total)
    
        
    


