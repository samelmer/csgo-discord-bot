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
                embedVar = discord.Embed(title="Match Info", description=str(i["event"]), color=0x1289c9)
                embedVar.set_author(name="HLTV.org", icon_url="https://www.hltv.org/img/static/favicon/favicon-16x16.png")
                embedVar.add_field(name="Teams: ", value=str(i["team1"]["name"]) + " - " + str(i["team2"]["name"]), inline=False)
                embedVar.add_field(name="Type: ", value=str(i["maps"]), inline=False)
                embedVar.add_field(name="Score: ", value=str(i["team1"]["result"]) + " - " + str(i["team2"]["result"]), inline=False)
                await message.channel.send(embed=embedVar)
        except:
            await message.channel.send("Incorrect command usage. Proper usage: $hltvresults [number]")

    if message.content.startswith("$hltvnews"):
        try:
            num_news = int(message.content[9:])
            news_requests = requests.get("https://hltv-api.vercel.app/api/news")
            news_data = news_requests.json()
            for i in news_data[0:num_news]:
                embedVar = discord.Embed(title=str(i["title"]), description=str(i["description"]), color=0x1289c9)
                embedVar.set_author(name="HLTV.org", icon_url="https://www.hltv.org/img/static/favicon/favicon-16x16.png")
                embedVar.add_field(name="Link: ", value=str(i["link"]), inline=False)
                embedVar.add_field(name="Date: ", value=str(i["date"]), inline=False)
                await message.channel.send(embed=embedVar)
        except:
            await message.channel.send("Incorrect command usage. Proper usage: $hltvnews [number]")
        

client.run("Token")
