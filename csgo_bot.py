import discord
from discord.ext import commands
import pip._vendor.requests as requests

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print("Bot logged in as {0.user}".format(bot))

@bot.command()
async def test(ctx):
    await ctx.send(":moyai:")

@bot.event
async def on_message(message):
    if message.content.startswith("$hltvresults"):
        try:
            num_games = int(message.content[12:])
            game_requests = requests.get("https://hltv-api.vercel.app/api/results.json")
            game_data = game_requests.json()
            for i in game_data[0:num_games]:
                await message.channel.send("Event: " + str(i["event"]) + "\n" + "Teams: " + str(i["team1"]["name"]) + " - " + str(i["team2"]["name"]) + "\n" + "Score: " + str(i["team1"]["result"]) + " - " + str(i["team2"]["result"]))
        except:
            await message.channel.send("Incorrect command usage. Proper usage: $hltvresults [number]")

    await bot.process_commands(message)

token = ""

with open("token.txt","r") as file:
    token = file.readline()

bot.run(token)