from aiogram.filters.callback_data import CallbackData
from enum import Enum, auto,IntEnum
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from typing import List
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton
import requests
from aiogram.utils.markdown import hbold
from aiogram.fsm.state import State,StatesGroup



class Available_Currency(str,Enum):
    Bitcoin=auto()
    Ethereum=auto()


class Calculations_Asks(StatesGroup):
    
    limit_bit=State()
    limit_eth=State()



class Currency_Digit(CallbackData,prefix="currency"):
    currency:Available_Currency
    
    

def keyboard_create_currency():
    builder=InlineKeyboardBuilder()
    dict_interest_currency={
        "Bitcoin":Currency_Digit(currency=Available_Currency.Bitcoin),
        "Ethereum":Currency_Digit(currency=Available_Currency.Ethereum)
        
        }
    [
      builder.button(text=txt,callback_data=currency_value.pack())
      for txt,currency_value in dict_interest_currency.items()
    ]
    builder.button(text="⬅️В главное меню",callback_data="main_page")
    builder.adjust(2,1)
    return builder.as_markup(**dict_interest_currency)




#create keyboard for calculations asks and bind

def calc_bitc(limit:int):
    response=requests.get(f"https://yobit.net/api/3/trades/btc_usd?limit={limit}?ignore_valid=1")#connect to api yobit.net
    total_trade_ask=0
    total_trade_bids=0
    for item in response.json()[f"btc_usd"]:# in the data by request keeping bid and ask of the trades
        if item["type"]=="ask":
            total_trade_ask+=item["price"]*item["amount"]
        if item["type"]=="bid":
            total_trade_bids+=item["price"]*item["amount"]
    info=[total_trade_ask,total_trade_bids]
    return info

def calc_eth(limit:int):#the same as previous function but for ethereum
    response=requests.get(f"https://yobit.net/api/3/trades/eth_usd?limit={limit}?ignore_valid=1")
    total_trade_ask=0
    total_trade_bids=0
    for item in response.json()[f"eth_usd"]:
        if item["type"]=="ask":
            total_trade_ask+=item["price"]*item["amount"]
        if item["type"]=="bid":
            total_trade_bids+=item["price"]*item["amount"]
    info=[total_trade_ask,total_trade_bids]
    return info



def return_choose_currency():
    keyboard_return=InlineKeyboardBuilder()
    keyboard_return.add(InlineKeyboardButton(text="⬅️Вернуться к выбору валюты",callback_data="markets"))
    keyboard_return.adjust(1)
    
    return keyboard_return.as_markup()

 
    


    

    


    
        
    



    
    
    