from .aimee import AIMEE


async def setup(bot: Red) -> None:
    cog = AIMEE(bot)
    await bot.add_cog(cog)
    cog.start_up_task()
