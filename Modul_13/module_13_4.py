import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from config_api import API_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


def calorie_calculator(age, growth, weigth):
    return 10.0 * float(weigth) + 6.25 * float(growth) - 5.0 * int(age) + 5.0


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text='Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(text='Calories')
async def set_age(message: types.Message):
    await message.answer(text='Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(text='Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)

    await message.answer(text='Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f'Ваши возраст: {data["age"]} лет, рост:  {data["growth"]} см, вес:  {data["weight"]} кг')
    result = calorie_calculator(data['age'], data['growth'], data['weight'])
    await message.answer(text=f'Ваша норма калорий {result}')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
