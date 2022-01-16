import discord

import credentials_manager
from moodle import upcoming_events

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content != "!up":
        return

    for e in upcoming_events():
        embed = discord.Embed(title=e.name, description=e.description, url=e.url)
        embed.add_field(name='Course', value=e.course.full_name)
        embed.add_field(name='Due', value=f'<t:{e.time_sort}:R>', inline=True)
        await message.channel.send(embed=embed)


if __name__ == '__main__':
    client.run(credentials_manager.get_discord_bot_token())
