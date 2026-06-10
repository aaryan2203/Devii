import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio

# 1. Setup & Configuration
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SECRET_ROLE_NAME = "padhai paglu"

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
logging.basicConfig(level=logging.INFO, handlers=[handler])

intents = discord.Intents.default()
intents.message_content = True  # Allows bot to read message content
intents.members = True          # Allows bot to see joins and manage roles

bot = commands.Bot(command_prefix='', intents=intents) # Added a prefix '!' to avoid accidental triggers
bot.remove_command('help')

# 2. Profanity Filter List (Reduces code bloat)
BAD_WORDS = [
     'bhadwa', 'bc', 'randi', 'bhenchod', 'madarchod', 'bkl', 'nigga', 
    'fuck', 'mc', '🖕', 'nigger', 'lodey', 'bhadwo', 'bhosdi', 'niggga', 
    'chamar', 'sex', 'mkc', 'mkb', 'lodu'
]
   
# 3. Events
@bot.event
async def on_ready():
    print(f"✅ We are ready to launch! Logged in as {bot.user.name}")
    print("---------------------------------")

@bot.event
async def on_message(message):
    # Ignore the bot's own messages to avoid infinite loops
    if message.author == bot.user:
        return

    # Check for abusive language
    content_lower = message.content.lower()
    if any(word in content_lower for word in BAD_WORDS):
        try:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, don't use abusive language here.", delete_after=10)
            return # Stop processing this message
        except discord.Forbidden:
            print(f"Error: Missing permissions to delete message in {message.channel.name}")

    # Required to make commands work when using on_message
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    print(f"Member joined: {member.name} (ID: {member.id})")
    
    # DM the user
    try:
        await member.send(f"Hello **{member.name}**! Welcome to the **{member.guild.name}** server! Check the rules.")
    except discord.Forbidden:
        print(f"Could not DM {member.name}.")

    # Public Welcome
    welcome_channel = discord.utils.get(member.guild.channels, name='🗨️︱general-chat')
    if welcome_channel:
        await welcome_channel.send(f"Please welcome our newest member, {member.mention}! 👋 check rules and roles.")

# 4. Commands - Greetings (Using Aliases to save space)
@bot.command(aliases=['Motivate', 'MOTIVATE'])
async def motivate(ctx):
    await ctx.send(f"{ctx.author.mention} you worked hard today, it's time to rest now 💗!")

@bot.command(aliases=['Hello', 'hii', 'Hii', 'hi', 'Hi', 'HII', 'heya', 'heyaa'])
async def hello(ctx):
    await ctx.send(f"hihihihihih suppppp, {ctx.author.mention}!")

@bot.command()
async def namaste(ctx):
    await ctx.send(f"namaste 🙏🏻🙏🏻 kese hoo, {ctx.author.mention}!")

@bot.command(aliases=['yoo', 'Yo', 'Yoo'])
async def yo(ctx):
    await ctx.send(f"yoooooooooooo {ctx.author.mention}!")

@bot.command(aliases=['hola', 'Hola', 'holaa'])
async def hi_spanish(ctx):
    await ctx.send(f"Holaaaaa, {ctx.author.mention}!")

# 5. Utility & Moderation
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=SECRET_ROLE_NAME)
    if role:
        try:
            await ctx.author.add_roles(role)
            await ctx.send(f"Success! {ctx.author.mention} is now assigned to **{SECRET_ROLE_NAME}**.")
        except discord.Forbidden:
            await ctx.send("Error: Check my role hierarchy.")
    else:
        await ctx.send(f"Error: Role **{SECRET_ROLE_NAME}** doesn't exist.")

@bot.command()
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"📸 {member.display_name}'s Avatar", color=discord.Color.blue())
    embed.set_image(url=member.display_avatar.url)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason"):
    await member.kick(reason=reason)
    await ctx.send(f"👢 {member} was kicked.\nReason: {reason}")

@bot.command()
async def helpp(ctx):
    embed = discord.Embed(title="🤖 Bot Help Menu", color=discord.Color.green())
    embed.add_field(name="👋 Greetings", value="`hello`, `namaste`, `yo`, `motivate`", inline=False)
    embed.add_field(name="⚙️ Roles", value="`assign`, `avatar`", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def vix(ctx):

    await ctx.send(f"Hello, @everyone!")



# 6. Run Bot
if TOKEN:
    bot.run("your discord bot token")
else:
    print("FATAL ERROR: DISCORD_TOKEN not found.")

DISCORD_TOKEN="your bot token"