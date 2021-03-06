import re

from dragonbot import bot
from dragonbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from dragonbot.cmdhelp import CmdHelp
from dragonbot.helpers.functions import deEmojify


@bot.on(admin_cmd(pattern="anime(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="anime(?: |$)(.*)", allow_sudo=True))
async def nope(cobra):
    dragon = cobra.pattern_match.group(1)
    if not dragon :
        if cobra.is_reply:
            (await cobra.get_reply_message()).message
        else:
            await edit_or_reply(cobra, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("animedb_bot", f"{(deEmojify(cobra))}")

    await troll[0].click(
        cobra.chat_id,
        reply_to=cobra.reply_to_msg_id,
        silent=True if cobra.is_reply else False,
        hide_via=True,
    )
    await cobra.delete()
    

CmdHelp("anime").add_command(
  "anime", "<anime name>", "Searches for the given anime and sends the details."
).add()
