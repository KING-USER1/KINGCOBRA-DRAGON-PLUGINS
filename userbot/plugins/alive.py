
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# 

import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, mafiaversion
from mafiabot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "GHOULS OP"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for ÂÝŮ$HópBØȚ

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

edit_time = 10
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/8af96ae4128e766ba6ac7.jpg"
file2 = "https://telegra.ph/file/8af96ae4128e766ba6ac7.jpg"
file3 = "https://telegra.ph/file/8af96ae4128e766ba6ac7.jpg"
file4 = "https://telegra.ph/file/8af96ae4128e766ba6ac7.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🔥🔥GHOULS BOT 𝕀𝕊 𝔸𝕃𝕀𝕍𝔼🔥🔥**__\n\n"

pm_caption += (
    f"                 👑𝕄𝔸𝕊𝕋𝔼ℝ👑\n**  『😈[{DEFAULTUSER}](tg://user?id={dragon})😈』**\n\n"
)

pm_caption += "🛡️TELETHON🛡️ : `1.15.0` \n\n"

pm_caption += f"😈DRAGON😈 : `{dragonversion}`\n\n"

pm_caption += f"😱SUDO😱            : `{sudou}`\n\n"

pm_caption += "😇CHANNEL😇️   : [ᴊᴏɪɴ](https://t.me/GHOULS_USER_BOT)\n\n"

pm_caption += "😎CREATOR😎    : [BAAPu](https://t.me/KING_COBRA_TERABAAP)\n\n"

pm_caption += "🤩SUPPORTER🤩    :[HellBoy](https://t.me/kraken_the_badass)\n\n"

pm_caption += "      [🔥REPO🔥](https://github.com/KING-USER1/GHOULS_USERBOT) 🔹 [📜License📜](https://github.com/KING-USER1/GHOULS_USERBOT/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
