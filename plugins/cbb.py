from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Cʀᴇᴀᴛᴏʀ🔱 : <a href='https://t.me/FounderOfIlluminati'>Tʜɪs Pᴇʀsᴏɴ</a>\n○ Lᴀɴɢᴜᴀɢᴇ : <code>Python3</code>\n○ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴀsʏɴᴄɪᴏ {__version__}</a>\n○ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ : <a href='https://github.com/PiyushAmarRahe/FileSaver'>Click here</a>\n○ Cʜᴀɴɴᴇʟ : @Memes_Hub_India\n○ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ : @Cherished_Community</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❌ ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
