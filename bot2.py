# bot.py
import os # for importing env vars for the bot to use
from twitchio.ext import commands
from random import randint

from twitchio.ext import commands


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            irc_token=os.environ['TMI_TOKEN'],
            client_id=os.environ['CLIENT_ID'],
            nick=os.environ['BOT_NICK'],
            prefix=os.environ['BOT_PREFIX'],
            initial_channels=[os.environ['CHANNEL']]
        )


    async def event_ready(self):
        #'Called once when the bot goes online.'
        print(f"{os.environ['BOT_NICK']} is online!")
        self.channel = self.get_channel(os.environ['CHANNEL'])
        await self.channel.send("MrDestructoid up and ready to go")

    async def event_message(self, ctx):
    #'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
        if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
            return

        await self.handle_commands(ctx)
        
        #if ctx.content.lower().startswith('安安'):
        #    await ctx.channel.send(f"MrDestructoid 安安 @{ctx.author.name}!")
        if ctx.content.lower().startswith('777'):
            await ctx.channel.send(f"MrDestructoid mayshow777 mayshow777 mayshow777 ")



    @commands.command(name='誰')
    async def 誰(self, ctx):
        await ctx.channel.send(f"MrDestructoid 我是無情的安安機器人")

    @commands.command(name='晚餐')
    async def 晚餐(self, ctx):
        dinner = ["咖哩飯","義大利麵","滷肉飯","火雞肉飯","池上便當","達美樂","燙青菜","蛋包飯","麥當當"]
        await ctx.channel.send(f"MrDestructoid 吃{dinner[randint(0,len(dinner)-1)]}")
'''
    @commands.command(name='指令')
    async def 指令(self, ctx):
        await ctx.channel.send(f"MrDestructoid !晚餐 !誰")
'''
bot = Bot()
bot.run()


