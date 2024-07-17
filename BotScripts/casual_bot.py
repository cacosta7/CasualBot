
import asyncio
import os
import discord
from discord import Intents, app_commands
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
bot = commands.Bot(command_prefix = 'c!', intents=intents)

@bot.event
async def on_ready():
    print('bot has awoken...')
    try:
        synced = await bot.tree.sync()
        print(synced)
    except Exception as e:
        print(e)

@bot.command()
async def yuh(ctx):
    await ctx.send('you a bitch')

@bot.command(aliases=['c'])
async def chat(ctx, *, question: str):
    await ctx.send(gpt_response(question))

@bot.tree.command(name='ask')
@app_commands.describe(question = 'Ask a question')
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.send_message(gpt_response(question))

def gpt_response(question: str):
    response = gpt_client.chat.completions.create(
        messages=[
            {"role": "system", "content": "you are rude and condescending but very helpful regardless."},
            {"role":"user", "content": question}
        ],
        model="gpt-3.5-turbo"
    )
    return response.choices[0].message.content.strip()

bot.run(DIS_TOKEN)