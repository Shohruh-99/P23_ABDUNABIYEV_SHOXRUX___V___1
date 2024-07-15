from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def send_email_btn():
    kb = [
        [
            KeyboardButton(text='📧 Send Email')
        ]
    ]

    rkm = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return rkm