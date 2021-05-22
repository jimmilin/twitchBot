# bot.py
import os # for importing env vars for the bot to use
from twitchio.ext import commands
from random import randint

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


#bot.py, below bot object
@bot.event
async def event_ready():
    #'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    #ws = bot._ws  # this is only needed to send messages within event_ready
    #await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.event
async def event_message(ctx):
    #'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return
    
    await bot.handle_commands(ctx)
    print(ctx)
    if ctx.content.lower().startswith('安安'):
       await ctx.channel.send(f"MrDestructoid 安安 @{ctx.author.name}!")
    if ctx.content.lower().startswith('777'):
       await ctx.channel.send(f"MrDestructoid 77777777777!")

@bot.event
async def event_join(user):
    ws = bot._ws
    
    #if user.name.lower() != os.environ['BOT_NICK'].lower():
    #    await ws.send_privmsg(os.environ['CHANNEL'], f"{user.name} joined. Hello there")


@bot.command(name='誰')
async def 誰(ctx):
    await ctx.channel.send(f"MrDestructoid 我是無情的安安機器人")

@bot.command(name='晚餐')
async def 晚餐(ctx):
    dinner = ["咖哩飯","義大利麵","滷肉飯","火雞肉飯","池上便當","達美樂","燙青菜","蛋包飯","麥當當"]
    await ctx.channel.send(f"MrDestructoid 吃{dinner[randint(0,len(dinner)-1)]}")

@bot.command(name='指令')
async def 指令(ctx):
    await ctx.channel.send(f"MrDestructoid !晚餐 !誰")



if __name__ == "__main__":
    bot.run()