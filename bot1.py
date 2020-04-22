import discord
import youtube_dl
from discord.ext import commands

TOKEN = 'NzAyMDU4NTYxNzk0MjExOTAw.Xp6hJg.RL9V2n4zXYdTj-Uo6bff9o-lOPA'

client = commands.Bot(commands_prefix = '.')

players = {}

@client.event
async def on_ready():
    print('Bot is online.')

    @client.command(pass_context=True)
    async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

    @client.command(pass_context=True)
    async def leave(ctx):
        server = ctx.message.server
        voice_client = client.voice_client(server)
        await voice_channel.disconnect()


    @client.command(pass_context=True)
    async def play(ctx, url):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()

        @client.command(pass_context=True)
        async def pause(ctx):
            id = ctx.message.server.id
            player[id].pause()

        @client.command(pass_context=True)
        async def stop(ctx):
            id = ctx.message.server.id
            player[id].stop()


@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    player[id].resume()



client.run(TOKEN)
