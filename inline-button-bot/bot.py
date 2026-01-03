import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.getenv("TOKEN")   # Render Environment Variable

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Send like this:\n\n"
        "/button Text | Button - link | Button2 - link"
    )

@dp.message(Command("button"))
async def button(message: types.Message):
    try:
        data = message.text.split(None, 1)[1]
        parts = data.split("|")

        text = parts[0].strip()
        keyboard = []

        for btn in parts[1:]:
            name, url = btn.split("-")
            keyboard.append([
                types.InlineKeyboardButton(
                    text=name.strip(),
                    url=url.strip()
                )
            ])

        await message.answer(
            text,
            reply_markup=types.InlineKeyboardMarkup(inline_keyboard=keyboard)
        )

    except:
        await message.answer(
            "❌ Wrong format!\n\n"
            "Use:\n/button Text | Btn - link"
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
