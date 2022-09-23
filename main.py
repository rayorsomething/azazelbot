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
                bot.sendMessage(message['channel_id'], 'bro just look at the code its not that hard... its on the discord if u dumbass deleted it')
            print(username + "used help command")
            
@bot.gateway.command
def owohnb(resp):
    if resp.event.message:
        message = resp.parsed.auto()
        if message['content'].startswith('owo h'):
            username = message['author']['username']
            if username == "Azazel":
                bot.sendMessage(message['channel_id'], 'owo b')
            print(username + "used owo hnb :)")

bot.gateway.run(auto_reconnect=True)