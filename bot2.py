# bot.py
import os # for importing env vars for the bot to use
from twitchio.ext import commands
from random import randint
from pathlib import Path
import time
import json

class Bot(commands.Bot):
    def __init__(self):
        self._cogs = [p.stem for p in Path(".").glob("./cogs/*.py")]
        with open('customCommands.json','r') as customCommands:
            self.cmd = json.load(customCommands)

        super().__init__(
            irc_token=os.environ['TMI_TOKEN'],
            client_id=os.environ['CLIENT_ID'],
            nick=os.environ['BOT_NICK'],
            prefix=os.environ['BOT_PREFIX'],
            initial_channels=[os.environ['CHANNEL']]
        )
    
    def setup(self):
        print("runing setup...")

        for cog in self._cogs:
            self.load_module(f"cogs.{cog}")
            print(f"loaded '{cog}'' cog.")
        print("setup completed.")

    def run(self):
        self.setup()

        print("Running bot...")
        super().run()


    async def event_ready(self):
        #'Called once when the bot goes online.'
        print(f"The bot is online! at {os.environ['CHANNEL']}")
        self.channel = self.get_channel(os.environ['CHANNEL'])
        #await self.channel.send("MrDestructoid up and ready to go")

    
    async def event_command_error(self, ctx, err):
        return
    
    async def event_error(self, err, data):
        print(err)

    async def event_message(self, ctx):
    #'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
        #if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        #    return

        await self.handle_commands(ctx)
        
        if ctx.content.lower().startswith('安安'):
            time.sleep(1)
            await ctx.channel.send(f"MrDestructoid 安安 @{ctx.author.name}!")

        with open('customCommands.json','r') as customCommands:
            cmd = json.load(customCommands)
        
        if ctx.content.startswith("!") and not(ctx.content.startswith("!add")):
            userCommand = ctx.content
            
            if cmd.get(ctx.content):
                msg = cmd[f"{ctx.content}"]
                await ctx.channel.send(f"{msg}")



        '''
        if ctx.content.lower().startswith('777'):
            time.sleep(1)
            await ctx.channel.send(f"mayshow777 mayshow777 mayshow777 ")
        '''

        #if ctx.content.lower().startswith('MrDestructoid'):
        #    await ctx.channel.send(f"MrDestructoid ")
            



    @commands.command(name='誰')
    async def 誰(self, ctx):
        time.sleep(1)
        await self.channel.send(f"MrDestructoid 我是無情的安安機器人")

    @commands.command(name='add')
    async def add(self, ctx):

        userCommand = ctx.content.split(' ')[1]
        userContext = ctx.content.split(' ')[2]

        self.cmd[f"!{userCommand}"] = userContext
        
        with open('customCommands.json','w') as customCommands:
            json.dump(self.cmd, customCommands)

    @commands.command(name='remove')
    async def remove(self, ctx):
        temp = "!" + ctx.content.split(' ')[1]

        if self.cmd.get(temp):
            del self.cmd[temp]
    
            with open('customCommands.json','w') as customCommands:
                json.dump(self.cmd, customCommands)

            await ctx.channel.send(f"removed {temp}")


    @commands.command(name='吃')
    async def 吃(self, ctx):
        time.sleep(1)
        dinner = ["咖哩飯","義大利麵","滷肉飯","火雞肉飯","池上便當","達美樂","肯德基","蛋包飯","麥當當"]
        await ctx.channel.send(f"MrDestructoid 吃{dinner[randint(0,len(dinner)-1)]}")

    @commands.command(name='抽')
    async def 抽(self, ctx):
        time.sleep(1)
        pool = ["mayshowFat","mayshowFat","mayshowFat","mayshowFat","mayshowFat","mayshowFat","mayshow87","mayshow87","mayshow87","mayshow777"]
        await ctx.channel.send(f"( つ•̀ω•́)つ {pool[randint(0,len(pool)-1)]} {pool[randint(0,len(pool)-1)]} {pool[randint(0,len(pool)-1)]} {pool[randint(0,len(pool)-1)]} {pool[randint(0,len(pool)-1)]}")



bot = Bot()
bot.run()


