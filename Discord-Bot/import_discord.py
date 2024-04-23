import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents = intents)
tree = app_commands.CommandTree

@client.event
async def on_ready():
    print("The bot is now ready")
    try:
        synced = await tree.sync(guild=discord.Object(id=1210361385112961024))
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.command()
async def host(ctx):
    with open("major-nations.txt") as f:
        countries = f.readlines()
    country_embed = discord.Embed(title="Major Nations")
    for country in countries:
        country_embed.add_field(name=country, value="N/A") # we can edit the N/A later with our list of members
    message = await ctx.send(embed=country_embed)
    with open('message.txt', 'w') as f:
        f.write(str(message.id))

    with open("europe-minors.txt") as f:
        countries = f.readlines()
    country_embed = discord.Embed(title="Europe")
    for country in countries:
        country_embed.add_field(name=country, value="N/A")
    message = await ctx.send(embed=country_embed)
    with open('message2.txt', 'w') as f:
        f.write(str(message.id))
    
@client.command()
async def unreserve(ctx):
    channel = client.get_channel(1229703484992000032)
    with open('ReservedUsers.txt', 'r') as f:
        f.read(int())
    

@client.command()
#@commands.has_role('Goblin') ..........................................................
async def reserve_USA(ctx):
    channel = client.get_channel(1229703484992000032)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    author = (ctx.author.id)

    with open("ReservedUsers.txt", "w") as f:
        f.write(str(author))

    country_embed = message.embeds[0]
    usa_field = country_embed.fields[0]
    country_embed.remove_field(0)
    new_value = ""
    if usa_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{usa_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(0, name=usa_field.name, value=new_value)
    await message.edit(embed=country_embed)

@client.command()
async def reserve_UK(ctx):
    channel = client.get_channel(1229703484992000032)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    author = (ctx.author.id)
    
    with open("ReservedUsers.txt", "w") as f:
        f.write(str(author))
    
    country_embed = message.embeds[0]
    UK_field = country_embed.fields[1]
    country_embed.remove_field(1)
    new_value = ""
    if UK_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{UK_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(1, name=UK_field.name, value=new_value)
    await message.edit(embed=country_embed)

@client.command()
async def reserve_France(ctx):
    channel = client.get_channel(1229703484992000032)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    author = (ctx.author.id)

    with open("ReservedUsers.txt", "w") as f:
        f.write(str(author))
    
    country_embed = message.embeds[0]
    france_field = country_embed.fields[2]
    country_embed.remove_field(2)
    new_value = ""
    if france_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{france_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(2, name=france_field.name, value=new_value)
    await message.edit(embed=country_embed)

@client.command()
async def reserve_Germany(ctx):
    channel = client.get_channel(1229703484992000032)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    author = (ctx.author.id)
    
    with open("ReservedUsers.txt", "w") as f:
        f.write(str(author))

    country_embed = message.embeds[0]
    germany_field = country_embed.fields[4]
    country_embed.remove_field(4)
    new_value = ""
    if germany_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{germany_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(4, name=germany_field.name, value=new_value)
    await message.edit(embed=country_embed)

@client.command()
async def reserve_Japan(ctx):
    channel = client.get_channel(1229703484992000032)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    author = (ctx.author.id)
    
    with open("ReservedUsers.txt", "w") as f:
        f.write(str(author))

    country_embed = message.embeds[0]
    japan_field = country_embed.fields[5]
    country_embed.remove_field(5)
    new_value = ""
    if japan_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{japan_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(5, name=japan_field.name, value=new_value)
    await message.edit(embed=country_embed)

@client.command()
async def reserve_Italy(ctx):
    channel = client.get_channel(1229703484992000032)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    author = (ctx.author.id)
    
    with open("ReservedUsers.txt", "w") as f:
        f.write(str(author))

    country_embed = message.embeds[0]
    italy_field = country_embed.fields[6]
    country_embed.remove_field(6)
    new_value = ""
    if italy_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{italy_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(6, name=italy_field.name, value=new_value)
    await message.edit(embed=country_embed)

@client.command()
async def reserve_USSR(ctx):
    channel = client.get_channel(1229703484992000032)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    author = (ctx.author.id)
    
    with open("ReservedUsers.txt", "w") as f:
        f.write(str(author))
    
    country_embed = message.embeds[0]
    ussr_field = country_embed.fields[7]
    country_embed.remove_field(7)
    new_value = ""
    if ussr_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ussr_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(7, name=ussr_field.name, value=new_value)
    await message.edit(embed=country_embed)

@client.command()
async def reserve_Poland(ctx):
    channel = client.get_channel(1229703484992000032)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    author = (ctx.author.id)

    with open("ReservedUsers.txt", "w") as f:
        f.write(str(author))

    country_embed = message.embeds[0]
    poland_field = country_embed.fields[8]
    country_embed.remove_field(8)
    new_value = ""
    if poland_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{poland_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(8, name=poland_field.name, value=new_value)
    await message.edit(embed=country_embed)

@client.command()
async def reserve_China(ctx):
    channel = client.get_channel(1229703484992000032)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    author = (ctx.author.id)
    
    with open("ReservedUsers.txt", "w") as f:
        f.write(str(author))

    country_embed = message.embeds[0]
    china_field = country_embed.fields[9]
    country_embed.remove_field(9)
    new_value = ""
    if china_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{china_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(9, name=china_field.name, value=new_value)
    await message.edit(embed=country_embed)



BOTTOKEN = ('MTIxMDM2Mzc3ODM0MDc0OTM4Mg.GfebOP.OpzDrJ2ccZjz0YvWsQAEgT0jEjvNCFH8kz3Tgk')


client.run(BOTTOKEN)