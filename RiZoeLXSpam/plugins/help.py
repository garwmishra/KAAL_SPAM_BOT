from .. import Riz, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
    
HELP_PIC = "https://telegra.ph/file/725fa8c7b8fc5831d0c23.jpg"

Riz_Help = "๐ฅ ๐๐๐๐ ๐๐๐๐ ๐๐๐ ๐ฅ\n\n"
 
Riz_Help += f"__๐๐ฆ๐๐ฌ ๐๐ฏ๐๐ข๐ฅ๐๐๐ฅ๐ ๐ข๐ง ๐๐๐๐ ๐๐๐๐ ๐๐๐__\n\n"

Riz_Help += f" โง ๐๐๐ด๐๐ฑ๐พ๐ ๐ฒ๐ผ๐ณ๐ โง\n\n"

Riz_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots\n\n"
 
Riz_Help += f" โง ๐ป๐ด๐ฐ๐๐ด ๐ฒ๐ผ๐ณ โง\n\n"

Riz_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
Riz_Help += f" โง ๐๐ฟ๐ฐ๐ผ ๐ฒ๐ผ๐ณ๐ โง\n\n"

Riz_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n\n"
 
Riz_Help += f"แดสษชแดแด สแดสแดแดก สแดแดแดแดษด าแดส แดแดสแด ษชษดาแด.\n\n"

Riz_Help += f"ยฉ @KAALNETWORK | @TEAM_KAAL_RIDER\n"


@Riz.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Riz_Help,
                                  buttons=[
        [
        Button.url("แดสส แดแดแดs", "https://t.me/ITS_HEAVEN_KING")
        ],
        [
        Button.url("แดสแดษดษดแดส", "https//t.me/KAALNETWORK")
        ] 
        ]
        )                                                         
