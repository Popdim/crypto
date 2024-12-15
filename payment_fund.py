import asyncio
from credits import bot_token, CRYPTO_TOKEN
import httpx

CRYPTO_URL = 'https://pay.crypt.bot/api/'
testnet_url = 'https://testnet-pay.crypt.bot/api/'


valute = 'USDT'
summa = 0.2
desc = 'оплата мануала'

async def create_payment(valute, summa, desc):

    headers = {"Crypto-Pay-API-Token": CRYPTO_TOKEN}
    payload = {
        "asset": valute,
        "amount": summa,
        "description": desc
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{testnet_url}createInvoice", headers=headers, json=payload)
        # print(response.json())
# async def check_payment():
#     headers = {"Crypto-Pay-API-Token": CRYPTO_TOKEN}
#     async with httpx.AsyncClient() as client:
#         response = await client.get(f"{testnet_url}getInvoices", headers=headers)
#         invoice = response.json()
#         print(f'оплачено {invoice}')

async def main():
    await create_payment(valute, summa, desc)
    while True:
        await check_payment()
        await asyncio.sleep(10)
if __name__ == '__main__':
    asyncio.run(main())
