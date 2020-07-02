import discord
import json
import db

CREDENTIALS_FILENAME = 'credentials.json'
CREDENTIALS_FILE = open(CREDENTIALS_FILENAME, 'r')
CREDENTIALS_JSON = json.loads(CREDENTIALS_FILE.read())

BOT_TOKEN = CREDENTIALS_JSON['BOT_TOKEN']
assert(BOT_TOKEN)

client = discord.Client()
db.initialize_database()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot == True:
        return

    elif message.content.startswith('$$'):
        if message.content == '$$help':
            await message.channel.send(
'''
Help:
To join the hivemind, type "$$join"
To leave the hivemind, type "$$leave"
To talk through the hivemind, just prepend your message with "$$"
''')
        elif message.content == '$$join':
            db.add_user(str(message.author.id))
            await message.channel.send('You have been added to the hivemind!')
        elif message.content == '$$leave':
            db.remove_user(str(message.author.id))
            await message.channel.send('We don\'t want you anymore anyway, scum.')
        elif db.user_in_hivemind(str(message.author.id)):
            await message.channel.send(message.content[2:])
            await message.delete()

client.run(BOT_TOKEN)
