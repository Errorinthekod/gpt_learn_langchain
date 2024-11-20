import os
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
import openai
from config import OPENAI_API_KEY, TOKEN
import asyncio

client = openai.OpenAI(api_key = OPENAI_API_KEY)

bot = Bot(token = TOKEN)
dp = Dispatcher(storage = MemoryStorage())
router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Hello! I'm chatbot. How can I help you?")

tour_info = '''
1. Тур Париж - 5000$. 7 дней
2. Тур Рим - 3000$. 7 дней
3. Тур Варшава - 900$. 10 дней
'''

@router.message(F.text)
async def chat(message: Message):
    response = client.chat.completions.create(
        model="gpt-4",
        messages = [{"role": "system", "content": f"You are helpful assistant for languages. Доступные туры {tour_info}"}, #able to write in russian
                     {"role": "user", "content": message.text}]
    )
    await message.answer(response.choices[0].message.content)

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    print('Bot activated')