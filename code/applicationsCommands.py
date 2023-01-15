#測試applications.commands斜線指令

from discord.ext import commands
import requests

my_application_id = "703163210282303608"
guild_id = "703086612757872710"

class appcmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#url = "https://discord.com/api/v8/applications/" + my_application_id + "/guilds/" + guild_id + "/commands"
url = "https://discord.com/api/v8/applications/<my_application_id>/guilds/<guild_id>/commands"

# This is an example USER command, with a type of 2
json = {
    "name": "permissions",
    "description": "Get or edit permissions for a user or a role",
    "options": []
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot <my_bot_token>"
}

# or a client credentials token for your app with the applications.commands.update scope
headers = {
    "Authorization": "Bearer <my_credentials_token>"
}

r = requests.post(url, headers=headers, json=json)

def setup(bot):
    bot.add_cog(appcmds(bot))