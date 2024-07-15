from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import html, Router, F

from email_bot.bot.buttons import send_email_btn
from email_bot.bot.functions import send_email
from email_bot.bot.states import StepState

handler_router = Router()

@handler_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalamu alaykum, {html.bold(message.from_user.full_name)}!")
    await message.answer('Iltimos,email manzilga xabar yubroish uchun tugmalardan birini tanlang!', reply_markup=send_email_btn())

@handler_router.message(F.text == '📧 Send Email')
async def main_page_handler(message: Message, state: FSMContext) -> None:
        await state.set_state(StepState.email_address)
        await message.answer("Iltimos, xabar yuborilishi kerak bo'lgan email manzilini kiriting!", reply_markup=ReplyKeyboardRemove())

@handler_router.message(StepState.email_address)
async def email_address_handler(message: Message, state: FSMContext) -> None:
    await state.update_data({'receiver_email' : message.text})
    await state.set_state(StepState.email_message)
    await message.answer("Iltimos, yuborilishi kerak bo'lgan xabarni yuboring!")

@handler_router.message(StepState.email_message)
async def email_message_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await state.clear()
    receiver_email = data.get('receiver_email')
    email_message = message.text
    await send_email(receiver_email,email_message)
    await message.answer("Siz kiritgan email manziliga xabar muvaffaqiyatli yuborildi!")