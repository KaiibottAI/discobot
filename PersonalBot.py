#!/usr/bin/env python3

import discord, dotenv, os, random
from dotenv import load_dotenv

load_dotenv()


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))
        print("")

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))
        if message.author == client.user:
            return
        if message.content.startswith("$hello"):
            await message.channel.send("Hello!", mention_author=True)

        if message.content.startswith("$rps"):
            await message.channel.send("Rock Paper Scissors, GO!")
            await message.channel.send("1. Rock\n2. Paper\n3. Scissors")

            # TODO

            # possible_choices = [1, 2, 3, "rock", "paper", "scissors"]

            # if (player.message.content).lower() not in possible_choices:
            #     await message.channel.send(
            #         "Pick a choice from {}".format(possible_choices)
            #     )


client = MyClient()
client.run(os.environ.get("TOKEN"))

if __name__ == "__main__":
    MyClient()
