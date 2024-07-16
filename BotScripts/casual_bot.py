
import os
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
DIS_TOKEN = os.getenv('DISCORD_TOKEN')
GPT_TOKEN = os.getenv('CHATGPT_TOKEN')

gpt_client = OpenAI(
    api_key=GPT_TOKEN
)

intents = Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix = 'c! ', intents=intents)

@bot.command()
async def yuh(ctx):
    await ctx.send('yuh')

@bot.command()
async def chat(ctx, *, question: str):
    response = gpt_client.chat.completions.create(
        messages=[
            {"role": "system", "content": "you are rude and condescending but very helpful regardless."},
            {"role":"user", "content": question}
        ],
        model="gpt-3.5-turbo"
    )
    await ctx.send(response.choices[0].message.content.strip())

bot.run(DIS_TOKEN)