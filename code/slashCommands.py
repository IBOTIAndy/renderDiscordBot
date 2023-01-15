from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext

class slashCmds(intents=Intents.default()):
    def __init__(self, bot):
        self.bot = bot

    @slash.slash(name="test")
    async def test(ctx: SlashContext):
        embed = Embed(title="Embed Test")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(slahsCmds(bot))
