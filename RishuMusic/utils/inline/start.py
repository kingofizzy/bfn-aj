from pyrogram.types import InlineKeyboardButton

import config
from RishuMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_3"],url=f"https://t.me/{app.username}?startgroup=true",)
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="MAIN_CP"),
        ],
        
        [
            InlineKeyboardButton(text=_["S_B_10"], callback_data="ALLBOT_CP"),
            InlineKeyboardButton(text=_["S_B_11"], callback_data="PROMOTION_CP"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], url=f"https://t.me/egypt_king_khaman"),
            InlineKeyboardButton(text=_["S_B_12"], url=f"https://t.me/itz_alpha_dude"),
        ],
    ]
    return buttons
