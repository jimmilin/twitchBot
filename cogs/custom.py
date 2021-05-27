from twitchio.ext import commands
import json

class CustomCMD:
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        with open('cogs/customCommands.json','r') as customCommands:
            self.cmd = json.load(customCommands)


    @commands.command(name="add")
    async def add_command(self, ctx):
        context = ctx.content.split(" ")
        split = " "
        response = split.join(context[2:len(context)])
        newCommand = "!" + context[1]
        
        if self.cmd.get(newCommand):
            await ctx.channel.send(f"Command {newCommand}.")
        else:
            self.cmd[newCommand] = response
            print(f"adding {newCommand}")
            with open('cogs/customCommands.json','w') as customCommands:
                json.dump(self.cmd, customCommands)

    @commands.command(name="remove")
    async def remove_command(self, ctx):
        context = ctx.content.split(" ")
        newCommand = "!" + context[1]
        
        if not self.cmd.get(newCommand):
            await ctx.channel.send(f"Command {newCommand} does not exist.")
        else:
            del self.cmd[newCommand]
            print(f"removing {newCommand}")
            with open('cogs/customCommands.json','w') as customCommands:
                json.dump(self.cmd, customCommands)
        



    '''
    def customCommand(*.args, **kwargs):

        @commands.command(name=f"{args}")
        async def command(self, ctx):
            await ctx.channel.send(args)

        return command
    '''

def prepare(bot: commands.Bot) -> None:
    bot.add_cog(CustomCMD(bot))