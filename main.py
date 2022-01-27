import discord

import credentials_manager
from moodle import upcoming_events_for_user

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user = message.author.id

    if message.content.startswith("!enrol"):
        tokens = message.content.split(" ")
        if len(tokens) != 3:
            await message.channel.send("!enrol <_akshay_IRIS_session> <remember_user_token_iris_prod>")
        else:
            credentials_manager.register_user(user, tokens[2], tokens[1])
            await message.channel.send("Registered successfully.")
        return

    if message.content != "!up":
        return

    if not credentials_manager.is_user_registered(user):
        await message.channel.send("!enrol <_akshay_IRIS_session> <remember_user_token_iris_prod>")
        return

    try:
        for e in upcoming_events_for_user(user):
            embed = discord.Embed(title=e.name, description=e.description, url=e.url)
            embed.add_field(name="Course", value=e.course.full_name)
            embed.add_field(name="Due", value=f"<t:{e.time_sort}:R>", inline=True)
            await message.channel.send(embed=embed)
    except Exception:
        await message.channel.send("An error occurred!")


if __name__ == "__main__":
    client.run(credentials_manager.get_discord_bot_token())
