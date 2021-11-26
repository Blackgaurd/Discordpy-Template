import discord
from discord.ext import commands

class CustomBot(commands.Bot):
    def __init__(self, command_prefix, help_command=..., description=None, **options):
        super().__init__(command_prefix, help_command=help_command, description=description, **options)
    
    async def on_ready(self):
        print("Online!")
    
    async def on_message(self, message):
        return await super().on_message(message)
    
    async def on_message_delete(self, message):
        pass
    
    def add_commands(self):
        @self.command
        async def sample_command(ctx):
            pass
        
        self.add_command(sample_command)