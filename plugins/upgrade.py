from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from pyrogram import Client , filters




@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
    text = """**Free Plan User**
Daily  Upload limit 2GB
Price 0

**🪙 Basic**
Daily  Upload  limit 20GB
Price Rs 30  ind  Month

**⚡ Standard**
Daily Upload limit 50GB
Price Rs 80  ind per Month

**💎 Pro**
Daily Upload limit 100GB
Price Rs 200  ind per Month

Payment Details :-
<b>➜ UPI ID :</b> <code>blank blank @axl</code>
<b>➜ PayPal :</b> <a href='blank blank'>Click Here</a>
<b>➜ QR Code :</b> <a href='blank blank'>Click Here</a>

After Payment Send Screenshots Of Payment To Admin @YetGood"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://t.me/yetgood"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await update.message.edit(text = text,reply_markup = keybord, disable_web_page_preview=True)
    
    

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
  text = """**Free Plan User**
Daily  Upload limit 2GB
Price 0

**🪙 Basic**
Daily  Upload  limit 20GB
Price Rs 30  ind  Month

**⚡ Standard**
Daily Upload limit 50GB
Price Rs 80  ind per Month

**💎 Pro**
Daily Upload limit 100GB
Price Rs 200  ind per Month

Payment Details :-
<b>➜ UPI ID :</b> <code>blank blank @axl</code>
<b>➜ PayPal :</b> <a href='blank blank'>Click Here</a>
<b>➜ QR Code :</b> <a href='blank blank'>Click Here</a>

After Payment Send Screenshots Of Payment To Admin @YetGood"""
    
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 Admin", url = "https://t.me/yetgood"),
        InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]
        ])
    
    await message.reply_text(text=text, reply_markup=keybord, quote=True, disable_web_page_preview=True)
    
	
    
    
    
# Sumit Developer
# @YetGood Telegram account
