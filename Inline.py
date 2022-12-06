from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



Iks = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👍🏻", callback_data="👍🏻"),

            InlineKeyboardButton(text="❌", callback_data="❌"),

            InlineKeyboardButton(text="👎🏻", callback_data="👎🏻")
        ]
    ]
)