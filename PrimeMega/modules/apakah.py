import random
from PrimeMega.events import register
from PrimeMega import telethn

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "Tidak tau.",
                 "Kamu sedang bertanya siapa.?",
                 "Apa iya?",
                 "Saya bingung apa yang terjadi?",
                 "Apakah aku juga seperti itu?"
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('🤚Give I have a question and it will be answered')
        return
    await event.reply(random.choice(APAKAH_STRING))
