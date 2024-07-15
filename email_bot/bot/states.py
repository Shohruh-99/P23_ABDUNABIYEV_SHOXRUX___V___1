from aiogram.fsm.state import StatesGroup, State


class StepState(StatesGroup):
    email_address = State()
    email_message = State()