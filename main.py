import discord
import os
import requests
import json
import random
from discord.ext import commands



#client = discord.Client()
client = commands.Bot(command_prefix = '$')

sad_words =["depressed", "sad", "unhappy", "miserable", "depressing", "angry"]

starter_encouragements = [
  "Cheer up Jit",
  "You got this Crodie",
  "You are the GOAT",
  "You have to believe in yourself",
  "Have the Mamba Mentality"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.command(name = 'version')
async def version(context):
  myEmbed = discord.Embed(title="Current Version", description = "This is the beta version of the bot", color = 0x00ff00)
  myEmbed.add_field(name = "Version Code:", value="v1.0.0", inline=False)
  myEmbed.add_field(name = "Date Released:", value="April 15th, 2021", inline = False)
  myEmbed.set_footer(text="Sample footer")
  myEmbed.set_author(name = "Raquib Alam")
  await context.message.channel.send(embed=myEmbed)


  

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    practice_commands_channel = client.get_channel(832039463483211830)
    await practice_commands_channel.send("Iridium Bot is Online")

@client.command(pass_context = True)
async def join(ctx):
  channel = ctx.message.author.voice.channel
  await client.channel(channel)

@client.command(pass_context = True)
async def leave(ctx):
  server = ctx.message.server
  voice_client = client.voice_client_in(server)


@client.event
async def on_disconnect():
  practice_commands_channel = client.get_channel(832039463483211830)
  practice_commands_channel.send("Iridium Bot has disconnected")



@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if msg.startswith('$hello'):
    await message.channel.send('Hello!')


  if msg.startswith('$inspiration'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))
  
  
  
  
  await client.process_commands(message)




 
client.run(os.getenv('TOKEN'))  