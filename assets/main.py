import discord 

intents = discord.Intents.all()

client = discord.Client(intents=intents)


@client.event 
async def on_ready():
  print("We Have Logged in as: {0.user}".format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  
  if message.content.startswith("$hello"):
    await message.channel.send("Hello!")
    
  #if message.author.name.startswith('jzr33_10506'):
    #await message.channel.send("Welcome Mr.Z")
  
  
  if message.content.endswith('#'):
    await message.channel.send("I'm Rabin, the discord bot created by Mr.Z!")
  
  #print(message.author.name)
    
client.run('MTI0MTIwNjUwMzcwMTIyMTQzNw.G8HcCg.5z2JjB2VXIRxGuTIwOHPmqRmwql__2womD6wzU')