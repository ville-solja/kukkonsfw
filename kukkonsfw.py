import discord
import requests
import sys
import os
import datetime

TOKEN = os.environ['TOKEN']    
if os.environ.get('KEY') is not None:
    KEY = os.environ['KEY']
    AzureFilterEnabled = True
    headers = {
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": KEY
    }
    azure_url_ext = "https://northeurope.api.cognitive.microsoft.com/vision/v1.0/analyze?visualFeatures=adult"
else: 
    AzureFilterEnabled = False

emoji_checkmark = '✅'
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    for guild in client.guilds:
        print(guild.name)
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if AzureFilterEnabled == True:
        if len(message.attachments) > 0:
            data = {'url': '{0}'.format(message.attachments[0].url)}
            r = requests.post(azure_url_ext, json=data, headers=headers)
            if r.json()['adult']['isAdultContent'] is True:
                if message.channel.is_nsfw() is False:
                    await message.delete()
                    msg = 'Image was deleted due to Adultscore: {0}.\nPlease repost to NSFW'.format(r.json()['adult']['adultScore'])
                    await message.channel.send(msg)
            else:
                await message.add_reaction(emoji_checkmark)

client.run(TOKEN)