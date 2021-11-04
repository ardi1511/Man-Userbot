# Credits: @mrismanaziz
# API by @tofik_dn || https://github.com/tofikdn
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import requests

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import man_cmd
from userbot.utils import edit_or_reply


@bot.on(man_cmd(outgoing=True, pattern=r"lyrics(?:\s|$)([\s\S]*)"))
async def _(event):
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("**Silahkan Masukan Judul Lagu**")
    try:
        xxnx = await edit_or_reply(event, "`Searching Lyrics...`")
        respond = requests.get(
            f"https://api-tede.herokuapp.com/api/lirik?l={query}"
        ).json()
        result = f"{respond['data']}"
        await xxnx.edit(result)
    except Exception:
        await xxnx.edit(f"**Lirik lagu tidak ditemukan.**")


CMD_HELP.update(
    {
        "lyrics": f"**Plugin : **`lyrics`\
        \n\n  •  **Syntax :** `{cmd}lyrics` <judul lagu>\
        \n  •  **Function : **Dapatkan lirik lagu yang cocok dengan judul lagu.\
    "
    }
)
