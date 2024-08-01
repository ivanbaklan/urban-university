from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)

api = ""  # Please insert token before start.
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard=True)
key_info = KeyboardButton(text="Информация")
key_count = KeyboardButton(text="Рассчитать")
kb.add(key_info, key_count)

inline_kb = InlineKeyboardMarkup()
key_calc_calories = InlineKeyboardButton(
    text="Рассчитать норму калорий", callback_data="key_calc_calories"
)
key_get_formula = InlineKeyboardButton(
    text="Формулы расчёта", callback_data="key_get_formulas"
)
inline_kb.add(key_calc_calories, key_get_formula)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start_command(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)


@dp.callback_query_handler(text="key_get_formulas")
async def get_formulas(call):
    await call.message.answer("10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) + 5")
    await call.answer()


@dp.callback_query_handler(text="key_calc_calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    try:
        result = (10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5)
        await message.answer(f"Ваша норма калорий: {result}")
    except ValueError:
        await message.answer("Возраст Рост и Вес должны быть числами")
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
