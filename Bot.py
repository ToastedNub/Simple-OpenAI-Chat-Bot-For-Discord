import discord
import openai
import os

openai.api_key = 'API_KEY'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

conversation_log = [
    "ADD YOUR PERSONALITY HERE",

    "ADD YOUR PERSONALITY HERE",
    
    "ADD YOUR PERSONALITY HERE"
]

async def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    try:
        if message.author.bot:
            return
        if message.content.startswith("!"):
            return
        conversation_log.append(f"User: {message.content}")
        async with message.channel.typing():
            bot_response = await get_openai_response(" ".join(conversation_log))
            await message.channel.send(bot_response)
        conversation_log.append(f"Bot: {bot_response}")
    except Exception as e:
        print(f"An error occurred: {e}")

client.run('BOT_TOKEN')
