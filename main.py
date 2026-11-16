
import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🌐 Купить VPN",
            callback_data="buy"
        )],
        [InlineKeyboardButton(
            text="💳 Тарифы",
            callback_data="tariffs"
        )],
        [InlineKeyboardButton(
            text="📞 Поддержка",
            url="https://t.me/dvrazrab"
        )]
    ])

    await message.answer(
        "👋 Добро пожаловать в BAMM VPN!\n\n"
        "🔒 Быстрый и надёжный VPN.\n"
        "Выберите нужный раздел:",
        reply_markup=keyboard
    )

@dp.callback_query()
async def buttons(callback: CallbackQuery):
    if callback.data == "buy":
        await callback.message.answer(
            "🛒 Покупка VPN скоро будет доступна."
        )

    elif callback.data == "tariffs":
        await callback.message.answer(
            "💳 Тарифы BAMM VPN:\n\n"
            "1 месяц — скоро\n"
            "3 месяца — скоро\n"
            "12 месяцев — скоро"
        )

    await callback.answer()

async def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

