from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/725fa8c7b8fc5831d0c23.jpg"
  

          
rizoel = "β§ ππππ πππ΄π πΌππ π΄πΏπΌππΈ β§\n\n"

rizoel += f"ββββββββββββββββββββ\n"

rizoel += f"β£β£ **α΄Κα΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄** : `3.9.6`\n"

rizoel += f"β£β£ **α΄α΄Κα΄α΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄** : `{version.__version__}`\n"

rizoel += f"β£β£ **πππππππππππ α΄ α΄ΚsΙͺα΄Ι΄**  : `{kaalversion}`\n"

rizoel += f"ββββββββββββββββββββ\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel,
                                  buttons=[
        [
        Button.url("α΄Κα΄Ι΄Ι΄α΄Κ", "https://t.me/KAALNETWORK"),
        Button.url("sα΄α΄α΄α΄Κα΄", "https://t.me/TEAM_KAAL_RIDER")
        ],
        [
        Button.url("β’ Κα΄α΄α΄ β’", "https://github.com/garwmishra/kaal_spam_bot")
        ]
        ]
        )
    
