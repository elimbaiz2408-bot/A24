import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot,Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message,CallbackQuery
from aiogram.fsm.state import StatesGroup,State
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
class Kz25(StatesGroup):
    mmr=State()
    hours=State()
    user_id=State()

load_dotenv(".ADMIN_ID")
load_dotenv(".token1")
admin_id=int(os.getenv("admin_id"))
TOKEN=os.getenv("TOKEN")
bot=Bot(token=TOKEN)
dp=Dispatcher()
btn=InlineKeyboardBuilder()

@dp.message(Command("start"))
async def start(message:Message,state:FSMContext):
    await message.answer("бро напеши /kz25")
@dp.message(Command("kz25"))
async def kz25(message:Message,state:FSMContext):
    await message.answer("привет друг")
    await asyncio.sleep(1)
    await message.answer("сколько у тебя MMR")
    await state.set_state(Kz25.mmr)
@dp.message(Kz25.mmr)
async def MMR_ch(message:Message,state:FSMContext):
    if not message.text.isdigit():
        await message.answer("нельзя использовать буквы")
        await asyncio.sleep(1)
        await message.answer("сколько у тебя MMR")
        return
    mmr=int(message.text)
    if mmr >= 2100:
        await message.answer("ты legenda")
    elif mmr >= 1900:
        await message.answer("ты elit")
    else:
        await message.answer("ты нам не подходиш")
        return
    await state.update_data(mmr=mmr)
    await state.set_state(Kz25.hours)
    await asyncio.sleep(1)
    await message.answer("сколько у вас часов в игре")
@dp.message(Kz25.hours)
async def hours_ch(message:Message,state:FSMContext):
    if not message.text.isdigit():
        await message.answer("нельза использовать буквы")
        await asyncio.sleep(1)
        await message.answer("сколько у тебя часов в игре")
        return
    hours=int(message.text)
    if hours >= 1000:
        await message.answer(f"у тебя {hours}")  
    elif hours <= 200:
        await message.answer("ты нам не подходиш")
        return
    await state.set_state(Kz25.user_id)
    await asyncio.sleep(1)
    await message.answer("введите свой айди")
    await state.update_data(hours=hours)
@dp.message(Kz25.user_id)
async def game_id(message:Message,state:FSMContext):
    if not message.text.isdigit():
        await message.answer("нельзя использовать буквы")
        await asyncio.sleep(1)
        await message.answer("введите свой айди")
        return
    user_id=int(message.text)
    if len(str(user_id)) not in (8,9):
        await message.answer("айди только от 8 до 9 цифр")
        await asyncio.sleep(1)
        await message.answer("введите свой айди")
        return
    await message.answer("жди те мы смотрим ваш профиль")
    await state.update_data(user_id=user_id)
    players_data=await state.get_data()
    mmr=players_data.get('mmr')
    hours=players_data.get('hours')
    user_id=players_data.get('user_id')
    btn.button(text="принять",callback_data=f"ac_{message.from_user.id}")
    btn.button(text="отклонить",callback_data=f"at_{message.from_user.id}")
    btn.adjust(2)
    await bot.send_message(
        admin_id,
        f"MMR:{mmr}\nhours:{hours}\nuser_id:{user_id}",
        reply_markup=btn.as_markup()
    )
@dp.callback_query(F.data.startswith("ac_"))
async def ac(callback:CallbackQuery):
    tg_bot_user_id=callback.data.split("_")[1]
    await callback.bot.send_message(
        chat_id=tg_bot_user_id,text="вы приняты в клан kz25 https://t.me/+3lj62QTBJ784YTYy"
        )
    await callback.answer("ваша заявка принята")
@dp.callback_query(F.data.startswith("at_"))
async def at(callback:CallbackQuery):
    tg_bot_user_id=callback.data.split("_")[1]
    await callback.bot.send_message(
        chat_id=tg_bot_user_id,text="вы нам не подходите"
        )
    await callback.answer("ваша заявка отклонена")
async def main():
    await dp.start_polling(bot)
if __name__=='__main__':
    print("бот запущен")
    asyncio.run(main())
