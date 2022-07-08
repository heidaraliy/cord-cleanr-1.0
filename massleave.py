import discord

client = discord.Client()
token = "your-client-token"

whitelist = [
    #id list of cord servers that survive chop
]


@client.event
async def mass_leave():
    for guild in client.guilds:
        try:
            if guild.id not in whitelist:
                server = client.get_guild(guild.id)
                await server.leave()
        except Exception as e:
            print(e)


client.run(token, bot=False)
