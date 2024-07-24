import logging
import crud_functions
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config_api import API_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
batton1 = KeyboardButton(text='Рассчитать')
batton2 = KeyboardButton(text='Информация')
batton3 = KeyboardButton(text='Купить')
kb.add(batton1)
kb.insert(batton2)
kb.add(batton3)

kbi = InlineKeyboardMarkup()
batton_in1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
batton_in2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kbi.add(batton_in1)
kbi.add(batton_in2)

kb_bay = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Product1", callback_data='product_buying'),
            InlineKeyboardButton(text="Product2", callback_data='product_buying'),
            InlineKeyboardButton(text="Product3", callback_data='product_buying'),
            InlineKeyboardMarkup(text="Product4", callback_data='product_buying')
        ]
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


def calorie_calculator(age, growth, weigth):
    return 10.0 * float(weigth) + 6.25 * float(growth) - 5.0 * int(age) + 5.0


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text='Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Информация')
async def info(mesage: types.Message):
    await mesage.answer(text='Бот для расчета суточной нормы калорий для человека')
    await mesage.delete()


@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer(text='Выберете меню', reply_markup=kbi)


# @dp.message_handler(text='Купить')
# async def get_buying_list(message):
#     for x in range(1, 5):
#         await message.answer(text=f"Название: Product{x} | Описание: описание {x} | Цена: {x * 100}")
#         with open(f'img/{x}.jpg', 'rb') as img:
#             await message.answer_photo(img)
#     await message.answer(text='Выберите продукт для покупки:', reply_markup=kb_bay)
@dp.message_handler(text='Купить')
async def get_buying_list(message):
    prods = crud_functions.get_all_products()
    for prod in prods:
        await message.answer(text=f"Название: {prod[1]} | Описание: {prod[2]} | Цена: {prod[3]}")
        with open(f'img/{prod[0]}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer(text='Выберите продукт для покупки:', reply_markup=kb_bay)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer(text='Введите свой возраст')
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
