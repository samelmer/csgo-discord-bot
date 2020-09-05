import discord
import pip._vendor.requests as requests

client = discord.Client()

@client.event
async def on_ready():
    print("Bot logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hltvresults"):
        try:
            num_games = int(message.content[12:])
            game_requests = requests.get("https://hltv-api.vercel.app/api/results")
            game_data = game_requests.json()
            for i in game_data[0:num_games]:
                await message.channel.send("Event: " + str(i["event"]) + "\n" + "Teams: " + str(i["team1"]["name"]) + " - " + str(i["team2"]["name"]) + "\n" + "Score: " + str(i["team1"]["result"]) + " - " + str(i["team2"]["result"]))
        except:
            await message.channel.send("Incorrect command usage. Proper usage: $hltvresults [number]")

client.run("Token")