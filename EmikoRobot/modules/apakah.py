import random
from EmikoRobot.events import register
from EmikoRobot import telethn

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "YNTKTS",
                 "Pala bapak kau pecah",
                 "Apa iya?",
                 "Tanya aja sama mamak kau tu pler"
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
    
import random
from EmikoRobot.events import register
from EmikoRobot import telethn

KAPAN_STRING = ["Besok kali", 
                 "Kalok ga mager", 
                 "Kapan Kapan", 
                 "Nanya Mulu", 
                 "Tahun Depan", 
                 "Kalau ga sabtu ya minggu",
                 "1 Jam lagi",
                 "Mungkin sekarang",
                 "8 Jam lagi",
                 "Sebulan lagi",
                 "Tahun lalu"
                 ]


@register(pattern="^/kapan ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(KAPAN_STRING))

import random
from EmikoRobot.events import register
from EmikoRobot import telethn

DIMANA_STRING = ["Dimana mana hatiku senang", 
                 "Di rumah kali", 
                 "Kepo banget luhk", 
                 "Di jonggol", 
                 "Di rumah bapak lo", 
                 "Ya mana gue tau anj",
                 "Di goa",
                 "Di mana hayo?",
                 "Di rumah ku",
                 "Di jalanan",
                 "Dimana hayo kamu kepo yaa"
                 ]


@register(pattern="^/dimana ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(DIMANA_STRING))

import random
from EmikoRobot.events import register
from EmikoRobot import telethn

KENAPA_STRING = ["Gatau", 
                 "Ntahlah", 
                 "Karena because tidak pernah never", 
                 "Bodoamat", 
                 "Apasih wibu nanya nanya", 
                 "Tanya orang lain aja",
                 "Pikir sendiri aja",
                 "Karna aku mencintai bapakmu",
                 "Tanya google aja ya",
                 "Tanya orang lain aja ya",
                 "Karna lo wibu"
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Mana pertanyaan nya tod')
        return
    await event.reply(random.choice(KENAPA_STRING))
