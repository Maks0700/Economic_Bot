from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder

def inline_keyboard_builder(
    text:str|list[str],
    callback_data:str|list[str],
    sizes:int|list[int]=1,
   
    
)->InlineKeyboardBuilder:
    builder=InlineKeyboardBuilder()
    if isinstance(text,str):#verification of type parametrs
        text=[text]
    if isinstance(callback_data,str):
        callback_data=[callback_data]
    if isinstance(sizes,int):
        sizes=[sizes]    
    [
        builder.button(text=txt,callback_data=c_b) #add to builder buttons
        for txt,c_b in zip(text,callback_data)
    ]
    builder.adjust(*sizes)
    return builder.as_markup()