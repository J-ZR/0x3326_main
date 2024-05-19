# Discord Bot

This Bot will use the discord.py documentation. 

 # Client Event
`@client.event`<br/>
`async def on_ready():`

This is the **Client Event** which is responsible for showing that there has been a succesful login.
The following code would go under that: <br /> 
`print("We Have Logged in as: {0.user}".format(client))
`<br />

### Following that,
outside of that function, there's another client event.<br />
```
@client.event
async def on_message(message):
  if message.author == client.user:
    return 

```
<br />
This indicates that if the message is from the bot, the bot should not respond to its own message.

# Messages

The following line of code: <br />
```
if message.content.startswith("$hello"):
    await message.channel.send("Hello!") 
```
It shows that the bot should respond to the message **starting wiht** a specified character/s, hence `content.startswith()`. <br />
In this case, the bot responds to the message if it starts with `$hello` with the response of `Hello!`.
