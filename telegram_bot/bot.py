import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from django.conf import settings
from tasks.models import Task


bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher

help_text = """Привет! Я бот приложения PingMe.  

Я помогу тебе управлять твоими задачами прямо из Telegram.  
Вот что я умею:  

📌 /add_task — добавить новую задачу  
📋 /tasks — показать список твоих задач  
✅ /complete_task — отметить задачу как выполненную  
❌ /delete_task  — удалить задачу  
⚙️ /settings — изменить настройки уведомлений  

Если у тебя есть вопросы или предложения, напиши в поддержку! 😊"""
about_text = """
Привет! 👋  

Я — бот приложения PingMe, созданный для удобного управления твоими задачами прямо из Telegram.  

Что я умею?  
📌 Добавлять задачи  
📋 Показывать список текущих задач  
⏳ Отмечать задачи выполненными  
❌ Удалять ненужные задачи  
🔔 Отправлять напоминания  

Больше не нужно открывать сайт — все важные задачи всегда под рукой!  

Чтобы узнать, как мной пользоваться, введи команду /help."""

start_inline_keybord = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📜 Меню", callback_data="menu")]
        [InlineKeyboardButton(text="ℹ О боте", callback_data="about")]
        [InlineKeyboardButton(text="", callback_data="")]
    ]
)



@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я бот PingMe!)', reply_markup=start_inline_keybord)


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(help_text)

@dp.message(Command("about"))
async def about(message: Message):
    await message.answer(about_text)


async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling