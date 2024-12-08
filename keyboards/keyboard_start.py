from aiogram import types

button_1 = types.KeyboardButton(text='рефаунд StockX')
button_2 = types.KeyboardButton(text='х5 клуб')
button_3 = types.KeyboardButton(text='рефаунд Я.Маркета')
button_4 = types.KeyboardButton(text='рефаунд озона')
button_5 = types.KeyboardButton(text='рефаунд алика')
button_6 = types.KeyboardButton(text='реф фарфетча')
button_7 = types.KeyboardButton(text='реф грелки')
button_8 = types.KeyboardButton(text='реф Ebay')
button_9 = types.KeyboardButton(text='рефаунд плеерока')
button_10 = types.KeyboardButton(text='маник по доксу и прочим приколам')

keyboard_start = [
    [button_1, button_2, button_3],
    [button_4, button_5, button_6],
    [button_7, button_8, button_9],
    [button_10]
]

keyboard_1 = types.ReplyKeyboardMarkup(keyboard=keyboard_start, resize_keyboard=True)