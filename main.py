import time

import discord

import credentials_manager
from moodle import upcoming_events
from utils import format_timestamp, time_remaining

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content != "!up":
        return

    now = time.time()
    for e in upcoming_events():
        embed = discord.Embed(title=e.name, description=e.description, url=e.url)
        embed.add_field(name='Course', value=e.course.short_name)
        embed.add_field(name='Due Date', value=format_timestamp(e.time_sort))
        embed.add_field(name='Time Left', value=time_remaining(now, e.time_sort))
        await message.channel.send(embed=embed)


if __name__ == '__main__':
    client.run(credentials_manager.get_discord_bot_token())
