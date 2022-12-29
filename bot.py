import asyncio
import logging
import random
import sys

from typing import Any, Dict

import aiogram
from aiogram import Bot, Dispatcher, F
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import StatesGroup, State
from aiogram.dispatcher.router import Router
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import text, hide_link

from parser import resource_parser

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
form_router = Router()


# @dp.message(commands=["start"])
# async def cmd_start(message: Message):
#     answer = text("Hello, I'm simple button bot",
#                   "Author's [GitHub](https://github.com/MikhailVolvach)",
#                   sep="\n")
#     await message.answer(answer, parse_mode="MARKDOWN")


# @dp.message(commands=["help"])
# async def cmd_help(message: Message):
#     await message.answer("Меню")


# @dp.message(commands=["findItem"])
# async def cmd_find_item(message: Message):
#     await message.answer("Поиск")


# @dp.message(content_types=ContentType.ANY)
# async def echo_with_reply(message: types.Message):
#
#     markup = ReplyKeyboardBuilder()
#     markup.add(
#         KeyboardButton(text="Начать"),
#         KeyboardButton(text="Закончить")
#     )
#
# #    if mes == "Начать":
# #        await message.answer("Начинаем")
# #   elif mes == "Закончить":
# #        await message.answer("Заканчиваем")
# #    else:
# #        markup = ReplyKeyboardBuilder()
# #        markup.add(
# #            KeyboardButton(text="Начать"),
# #            KeyboardButton(text="Закончить")
# #        )
#     await message.answer("Пожалуйста, нажмите кнопку ", reply_markup=markup.as_markup())


class Form(StatesGroup):
    resource = State()


@form_router.message(Command(commands=["start"]))
async def form_start(message: Message, state: FSMContext):
    await state.set_state(Form.resource)
    await message.reply(
        "Hi there! What do you want to see?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Posts"),
                    # KeyboardButton(text="Comments"),
                    # KeyboardButton(text="Albums"),
                    KeyboardButton(text="Photos"),
                    # KeyboardButton(text="To Do"),
                    # KeyboardButton(text="Users"),
                    KeyboardButton(text="/cancel")
                ]
            ],
            resize_keyboard=True
        )
    )


@form_router.message(Command(commands=["cancel"]))
@form_router.message(F.text.casefold() == "cancel")
async def form_cancel_handler(message: Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Cancelled.",
        reply_markup=ReplyKeyboardRemove()
    )


# @form_router.message(Form.resource)
# async def process_resource(message: Message, state: FSMContext):
#     await state.set_state()


# @form_router.message(Form.resource, F.text.casefold() == "Posts")
@form_router.message(Form.resource)
async def process_posts(message: Message, state: FSMContext):
    await state.set_state(Form.resource)

    response_data = resource_parser(message.text)
    number = random.randrange(1, len(response_data))

    if message.text == "Posts":
        await message.answer(
            f"<b>{response_data[number]['title']}</b>\n{response_data[number]['body']}",
        )
    elif message.text == "Photos":
        await message.answer(
            f"<b>{response_data[number]['title']}</b>{hide_link(response_data[number]['url'])}"
        )

    await message.answer(
        "Do you want to go to the start?",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="/start")
                ]
            ],
            resize_keyboard=True
        )
    )




    # await state.set_state(Form.like_bots)
    # await message.answer(
    #     f"Nice to meet you, {aiogram.html.quote(message.text)}! \nDid do you want to know about this item?",
    #     reply_markup=ReplyKeyboardMarkup(
    #         keyboard=[
    #             [
    #                 KeyboardButton(text="Yes"),
    #                 KeyboardButton(text="No")
    #             ]
    #         ],
    #         resize_keyboard=True,
    #     ),
    # )


# @form_router.message(Form.like_bots, F.text.casefold() == "no")
# async def process_dont_like_write_bots(message: Message, state: FSMContext):
#     data = await state.get_data()
#     await state.clear()
#     await message.answer(
#         "Not bad not terrible. \nSee you soon.",
#         reply_markup=ReplyKeyboardRemove()
#     )
#     await show_summary(message=message, data=data, positive=False)


# @form_router.message(Form.like_bots, F.text.casefold() == "yes")
# async def process_like_write_bots(message: Message, state: FSMContext):
#     await message.reply(
#         "Cool! I'm too!",
#         reply_markup=ReplyKeyboardRemove()
#     )
#
#
# @form_router.message(Form.like_bots)
# async def process_unknown_write_bots(message: Message, state: FSMContext):
#     await message.reply("I don't understand you :(")
#
#
# async def show_summary(message: Message, data: Dict[str, Any], positive: bool = True):
#     name = data["name"]
#     text = f"I'll keep in mind that, {aiogram.html.quote(name)}, "
#     text += (
#         "you like to write bots"
#         if positive
#         else "you don't like to write bots"
#     )
#     await message.answer(text=text, reply_markup=ReplyKeyboardRemove())


async def main():
    bot = Bot(token="5972437920:AAGcRIT6VOaJKLkn1MN3qqpVSVHvbQ8tqCE", parse_mode="HTML")
    dp.include_router(form_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
