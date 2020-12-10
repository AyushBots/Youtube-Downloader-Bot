from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel ❣️", url="https://t.me/AyushBots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/CyberBoyAyushBot")]
        [InlineKeyboardButton(
            "DEVELOPER💻", url="https://github.com/CyberBoyAyush")]
    ])
    welcomed = f"Hoi! <b>{message.from_user.first_name}</b>\n\nThis Is Youtube Video Downloader Bot🔥\n\nJoin @AyushBots Before Using It❤️\n\nHit /Help To Know More😁"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
