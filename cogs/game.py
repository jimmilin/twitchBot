from twitchio.ext import commands


class Game:
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="大冒險")
    async def 大冒險_command(self, ctx):
        await ctx.send(
            "指令: {}".format(
                " • ".join(
                    "|".join([cmd.name, *(cmd.aliases or [])])
                    for cmd in self.bot.commands.values()
                )
            )
        )

def prepare(bot: commands.Bot) -> None:
    bot.add_cog(Game(bot))