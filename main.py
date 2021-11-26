from bot import CustomBot

bot = CustomBot('>', help_command=None)

with open("token.txt", "r") as f:
    TOKEN = f.readline().strip()
    
if __name__ == "__main__":
    bot.run(TOKEN)