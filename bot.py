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


async def main():
    bot = Bot(token="5972437920:AAGcRIT6VOaJKLkn1MN3qqpVSVHvbQ8tqCE", parse_mode="HTML")
    dp.include_router(form_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
