#    This file is part of the CompressorBot distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/wahebtalal/VideoCompressBot/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.reply(
        f"Welcome `{ok.user.first_name}`\nThis is a video compression bot.\nIt reduces the size of the video while maintaining its accuracy.\nYou can create screenshots/sample of the video.",
        buttons=[
            [Button.inline("help", data="ihelp")],
            [
                Button.url("source code", url="github.com/wahebtalal/VideoCompressBot"),
                Button.url("Developer", url="t.me/Wahiebtalal"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**🐠 Video Compress Bot**\n\n+This bot compresses videos with little change in quality.\n+Create a compressed video sample\n+Easy to use\n-Due to the quality settings, the bot takes time to compress.\nSo Be patient and send the videos one by one after you're done.\nDon't spam to avoid getting banned.\n\nJust forward the video"
                      )


async def ihelp(event):
    await event.edit(
        "**🐠 Video Compress Bot**\n\n+This bot compresses videos with little change in quality.\n+Create a compressed video sample\n+Easy to use\n-Due to the quality settings, the bot takes time to compress.\nSo Be patient and send the videos one by one after you're done.\nDon't spam to avoid getting banned.\n\nJust forward the video",
        buttons=[Button.inline("Revert", data="beck")],
    )


async def beck(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.edit(
        f"Welcome `{ok.user.first_name}`Hi,\nThis is a video compression bot.\nIt reduces video size while maintaining its accuracy.\nYou can create video/sample screenshots.",
             buttons=[
            [Button.inline("help", data="ihelp")],
            [
                Button.url("source code", url="github.com/wahebtalal/VideoCompressBot"),
                Button.url("Developer", url="t.me/Wahiebtalal"),
            ],
        ],
    )


async def sencc(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "Choose method",
        buttons=[
            [
                Button.inline("default", data=f"encc{key}"),
                Button.inline("Customize", data=f"ccom{key}"),
            ],
            [Button.inline("Revert", data=f"back{key}")],
        ],
    )


async def back(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "🐠 **What do you want** 🐠",
        buttons=[
            [
                Button.inline("Create sample ", data=f"gsmpl{key}"),
                Button.inline("Screenshots ", data=f"sshot{key}"),
            ],
            [Button.inline("compression", data=f"sencc{key}")],
        ],
    )


async def ccom(e):
    await e.edit("Send file name ")
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    chat = e.sender_id
    async with e.client.conversation(chat) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=chat))
        repl = await reply
        if "." in repl.text:
            q = repl.text.split(".")[-1]
            g = repl.text.replace(q, "mkv")
        else:
            g = repl.text + ".mkv"
        outt = f"encode/{chat}/{g}"
        x = await repl.reply(
            f"File name : {g}\n\nSend a thumbnail Thumbnail ."
        )
        replyy = cv.wait_event(events.NewMessage(from_users=chat))
        rep = await replyy
        if rep.media:
            tb = await e.client.download_media(rep.media, f"thumb/{chat}.jpg")
        elif rep.text and not (rep.text).startswith("/"):
            url = rep.text
            os.system(f"wget {url}")
            tb = url.replace("https://telegra.ph/file/", "")
        else:
            tb = thum
        omk = await rep.reply(f"Thumbnail {tb} Setted Successfully")
        hehe = f"{outt};{dl};{tb};{dtime}"
        key = code(hehe)
        await customenc(omk, key)
