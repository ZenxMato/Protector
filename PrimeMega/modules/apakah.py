import random
from PrimeMega.events import register
from PrimeMega import telethn

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Ngapa tanya gua, pikir pake otak", 
                 "Bisa jadi", 
                 "Gatau bro, soalnya lu wibu",
                 "Cukup bro",
                 "Bisa jadi sih, soalnya gua ngasal",
                 "Kamu sedang bertanya siapa.?",
                 "Apa iya?",
                 "Saya bingung apa yang terjadi?",
                 "Apakah aku juga seperti itu?"
                 "Ndak tau ya kok tanya saya"
                 "Seperti nya iya, tetapi saya ngasal"
                 "Hmmm saya pikir itu kamu"
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('🤚Give I have a question and it will be answered')
        return
    await event.reply(random.choice(APAKAH_STRING))
