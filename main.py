import os
import discord
import requests
import json
import random
from replit import db


client = discord.Client()

sad_words = ["sad" ,"motivation" ,"unhappy","miserable","dukh","dard","peeda"]

starter_encouragement = ["cheer up!","Hang in there.","You are a great person / bot!"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in message.content for word in sad_words):
    await message.channel.send(random.choice(starter_encouragement))

client.run(os.environ['TOKEN'])
