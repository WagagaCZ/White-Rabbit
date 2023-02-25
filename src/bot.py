from discord.ext import commands

class WhiteRabbit(commands.Bot):
    async def setup_hook(self) -> None:
        # here, we are loading extensions prior to sync to ensure we are syncing interactions defined in those extensions.

        # Load all extensions
        PLUGINS = ["about", "admin", "debug", "export", "game", "manual", "players", "settings"]
        for plugin in PLUGINS:
            await self.load_extension(f"cogs.{plugin}")
