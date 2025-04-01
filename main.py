import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import Settings
from functions import AdvCashAPIClient

settings = Settings()

# Инициализация бота и диспетчера
bot = Bot(token=settings.tg_bot_token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Инициализация API-клиента AdvCash
api_client = AdvCashAPIClient(api_name=settings.api_name, api_secret=settings.api_secret,
                              account_email=settings.account_email)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Получение баланса
    try:
        balance = api_client.get_balances()
        balance_text = "\n".join(f"{token}: {float(value)}" for token, value in balance.items())
        response = f"Ваш балансы:\n{balance_text}"
    except Exception as e:
        response = f"Ошибка при получении баланса: {e}"

    await message.reply(text=response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
