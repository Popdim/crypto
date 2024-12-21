import asyncio
from aiogram import Bot, Dispatcher, types, F
from credits import bot_token, CRYPTO_TOKEN
from aiogram.filters.command import Command
import logging
from keyboards.keyboard_start import keyboard_1
import httpx

bot = Bot(token=bot_token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
CRYPTO_URL = 'https://pay.crypt.bot/api/'
testnet_url = 'https://testnet-pay.crypt.bot/api/'

# async def create_payment(valute, summa, desc):
#     headers = {"Authorization": f"Bearer {CRYPTO_TOKEN}"}
#     payload = {
#         "asset": valute,
#         "amount": summa,
#         "description": desc
#     }
#     async with httpx.AsyncClient() as client:
#         response = await client.post(f"{CRYPTO_URL}createInvoice", headers=headers, json=payload)
#         return response.json()

async def create_payment(valute, summa, desc):
    headers = {"Crypto-Pay-API-Token": CRYPTO_TOKEN}
    payload = {
        "asset": valute,
        "amount": summa,
        "description": desc
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{CRYPTO_URL}createInvoice", headers=headers, json=payload)
        return response.json()
@dp.message(Command('start'))
async def cmnd_start(message: types.Message):
    await message.answer('Привет, ты в шопе 1055p. Вот список товаров, которые я продаю')
    await message.answer('''1. реф stockx 
2. бесконечные баллы х5 клуба
3. рефаунд яндекс маркета
4. рефаунд озона
5. рефаунд алика
6. рефаунд фарфетча
7. рефаунд грелки
8. рефаунд ебея
9. рефаунд плеерока
10. маник по доксу и прочим приколам''', reply_markup=keyboard_1)
    await message.answer('Выбери интерсующий Тебя товар')


# @dp.message(Command('payment'))
# async def payment_cmd(message: types.Message):
#     try:
#         valute = 'USDT'
#         summa = 10
#         desc = 'оплата мануала'
#         payment = await create_payment(valute, summa, desc)
#         print(payment)
#     except Exception as e:
#         await message.answer('ошибка оплаты')

@dp.message(F.text=='рефаунд StockX')
async def cmd_1(message: types.Message):
    summa = 10
    desc = 'Оплата мануала по рефаунду StockX'
    valute = 'USDT'
    result = await create_payment(valute, summa, desc)
    await message.answer_photo(photo='https://images.prismic.io/contrary-research/Zmvczpm069VX1vdB_StockXcover-1-.png?auto=format,compress',
                               caption=f'Мануал по рефаунду Ebay \nЦена: 10$ \nОписание: Мануал по рефаунду(полному возврату денег за покупку) тороговой площадки Ebay. Мануал куплен за 100$ \n'
                                       '')
    print(result)
    await message.answer(f'Ссылка на оплату \n{result.get("result").get("pay_url")}')

@dp.message(F.text=='баллы х5 клуба')
async def cmd_2(message: types.Message):
    summa = 10
    desc = 'Оплата мануала по бесконечным баллам X5 клуба'
    valute = 'USDT'
    result = await create_payment(valute, summa, desc)
    await message.answer_photo(photo='https://wineretail.info/uploads/photo/SETI/X5/01.jpg',
                               caption='Мануал по рефаунду Ebay \nЦена: 10$ \nОписание: Мануал по рефаунду(полному возврату денег за покупку) тороговой площадки Ebay. Мануал куплен за 100$')
    await message.answer(f'Ссылка на оплату \n{result.get("result").get("pay_url")}')
@dp.message(F.text=='рефаунд q.Маркета')
async def cmd_3(message: types.Message):
    summa = 10
    desc = 'Оплата мануала по рефаунду Я.Маркета'
    valute = 'USDT'
    await message.answer_photo(photo='https://adindex.ru/news/marketing/322257/img/yandex.jpg',
                               caption='Мануал по рефаунду Яндекс Маркета \nЦена: 10$ \nОписание: Мануал по рефаунду(полному возврату денег за покупку) тороговой площадки Ebay. Мануал куплен за 100$')
@dp.message(F.text=='рефаунд OZON')
async def cmd_1(message: types.Message):
    summa = 10
    desc = 'Оплата мануала по рефаунду OZON'
    valute = 'USDT'
    await message.answer_photo(photo='https://catalogi.ru/upload/iblock/d9a/70p658pwxybfmzot3ttja0f4e014ehdx.png',
                               caption='Мануал по рефаунду OZON \nЦена: 10$ \nОписание: Мануал по рефаунду(полному возврату денег за покупку) тороговой площадки Ebay. Мануал куплен за 100$')
@dp.message(F.text=='рефаунд AliExpress')
async def cmd_1(message: types.Message):
    await message.answer_photo(photo='https://catalogi.ru/upload/iblock/d9a/70p658pwxybfmzot3ttja0f4e014ehdx.png',
                               caption='Мануал по рефаунду Ebay \nЦена: 10$ \nОписание: Мануал по рефаунду(полному возврату денег за покупку) тороговой площадки Ebay. Мануал куплен за 100$')
@dp.message(F.text=='рефаунд Farfetch')
async def cmd_1(message: types.Message):
    summa = 10
    desc = 'Оплата мануала по рефаунду Farfetch'
    valute = 'USDT'
    await message.answer_photo(photo='https://catalogi.ru/upload/iblock/d9a/70p658pwxybfmzot3ttja0f4e014ehdx.png',
                               caption='Мануал по рефаунду Farfetch \nЦена: 10$ \nОписание: Мануал по рефаунду(полному возврату денег за покупку) тороговой площадки Ebay. Мануал куплен за 100$')
@dp.message(F.text=='реф Grailed')
async def cmd_1(message: types.Message):
    await message.answer_photo(photo='https://media-assets.grailed.com/prd/misc/-RX1V_JQQQLCZNNTDSDYB-WCAIHQG170G9OVQG?fit=crop&h=630&w=1200',
                               caption='Мануал по рефаунду Ebay \nЦена: 10$ \nОписание: Мануал по рефаунду(полному возврату денег за покупку) тороговой площадки Ebay. Мануал куплен за 100$')
@dp.message(F.text=='реф Ebay')
async def cmd_1(message: types.Message):
    await message.answer_photo(photo='https://catalogi.ru/upload/iblock/d9a/70p658pwxybfmzot3ttja0f4e014ehdx.png',
                               caption='Мануал по рефаунду Ebay \nЦена: 10$ \nОписание: Мануал по рефаунду(полному возврату денег за покупку) тороговой площадки Ebay. Мануал куплен за 100$')
@dp.message(F.text=='рефаунд Playerok')
async def cmd_1(message: types.Message):
    await message.answer_photo(photo='https://playerok.com/og_playerok.png',
                               caption='Мануал по рефаунду Ebay \nЦена: 10$ \nОписание: Мануал по рефаунду(полному возврату денег за покупку) тороговой площадки Ebay. Мануал куплен за 100$')
@dp.message(F.text=='маник по доксу и прочим приколам')
async def cmd_1(message: types.Message):
    await message.answer_photo(photo='https://media.360.ru/get_resized/qvWL2YcmdK9fsE8ImAJ7UWsordc=/1920x0/filters:rs(fit):format(webp)/YXJ0aWNsZXMvaW1hZ2UvMjAyNC84LzIwMTkwMTA3LWdhZi11NTUtMjgwLmpwZw.webp',
                               caption='Мануал по рефаунду Ebay \nЦена: 10$ \nОписание: Мануал по рефаунду(полному возврату денег за покупку) тороговой площадки Ebay. Мануал куплен за 100$')
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())