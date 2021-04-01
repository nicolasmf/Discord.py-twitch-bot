import discord
import asyncio
import requests

from discord.ext import commands
import datetime


intents = discord.Intents.default()
intents.members = True
intents.reactions = True

bot = commands.Bot(command_prefix="$", intents=intents)

# https://twitchtokengenerator.com
YOURCLIENTID = 0
AUTHORIZATION = 0

API_HEADERS = {
    'client-id': YOURCLIENTID,
    'Authorization': AUTHORIZATION
}

# Initialization
stream = False
reqSession = requests.Session()


@bot.event
async def on_ready():
    while True:
        # returns true if online, false if not
        async def checkUser(username, stream):
            url = 'https://api.twitch.tv/helix/streams?user_login=' + username

            req = reqSession.get(url, headers=API_HEADERS)
            jsondata = req.json()

            # print(jsondata)

            if len(jsondata.get("data")) != 0 and stream == False:
                print("Log: [{}] stream started.".format(
                    datetime.datetime.now()))

                # WRITE AND SEND YOUR EMBED / MESSAGE HERE

                stream = True
                return stream

            elif len(jsondata.get("data")) == 0 and stream is True:
                print("Log: [{}] stream finished.".format(
                    datetime.datetime.now()))
                stream = False
                return stream
            else:
                return stream

        stream = await checkUser("username", stream)

        await asyncio.sleep(5)
