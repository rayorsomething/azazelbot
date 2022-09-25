import discum   
import os
import time
from discum.utils.slash import SlashCommander
from discum.utils.embed import Embedder

TOKEN = os.environ.get("DISCORD_TOKEN")
bot=discum.Client(token=TOKEN)

@bot.gateway.command
def help(resp):
    if resp.event.message:
        message = resp.parsed.auto()
        if message['content'].startswith('me.help'):
            username = message['author']['username']
            if username == "Azazel":
                bot.sendMessage(message['channel_id'], 'bro just look at the code its not that hard... its on the github if u dumbass deleted it')
            print(username + "used help command")
            
@bot.gateway.command
def owohnb(resp):
    if resp.event.message:
        message = resp.parsed.auto()
        if message['content'] == ('owo h'):
            username = message['author']['username']
            if username == "Azazel":
                bot.sendMessage(message['channel_id'], 'owo b')
            print(username + "used owo hnb :)")

@bot.gateway.command
def owohnb(resp):
    if resp.event.message:
        message = resp.parsed.auto()
        if message['content'] == ('me.weird'):
            username = message['author']['username']
            if username == "Azazel":
                bot.sendMessage(message['channel_id'], '+play nothing is safe')
                bot.sendMessage(message['channel_id'], '+play https://www.youtube.com/watch?v=j8tNmJwDMzA')
                bot.sendMessage(message['channel_id'], '+play https://www.youtube.com/watch?v=x8foyxXyEM8')
            print(username + "used weird playlist")

bot.gateway.run(auto_reconnect=True)