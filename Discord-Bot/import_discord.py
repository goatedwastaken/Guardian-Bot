from sys import argv
import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents = intents)
tree = app_commands.CommandTree

client.remove_command('help')

global usa_res
usa_res = False

global uk_res
uk_res = False

global france_res
france_res = False

global germany_res
germany_res = False

global japan_res
japan_res = False

global italy_res
italy_res = False

global ussr_res
ussr_res = False

global poland_res
poland_res = False

global china_res
china_res = False

global sweden_res
sweden_res = False

global norway_res
norway_res = False

global finland_res
finland_res = False

global denmark_res
denmark_res = False

global estonia_res
estonia_res = False

global latvia_res
latvia_res = False

global lithuania_res
lithuania_res = False

global netherlands_res
netherlands_res = False

global belgium_res
belgium_res = False

global luxembourg_res
luxembourg_res = False

global ireland_res
ireland_res = False

global iceland_res
iceland_res = False

global czechoslovakia_res
czechoslovakia_res = False

global austria_res
austria_res = False

global hungary_res
hungary_res = False

global romania_res
romania_res = False

global yugoslavia_res
yugoslavia_res = False

global bulgaria_res
bulgaria_res = False

global albania_res
albania_res = False

global greece_res
greece_res = False

global turkey_res
turkey_res = False

global spain_res
spain_res = False

global portugal_res
portugal_res = False

global switzerland_res
switzerland_res = False

#americas

global argentina_res
argentina_res = False

global bolivia_res
bolivia_res = False

global brazil_res
brazil_res = False

global chile_res
chile_res = False

global colombia_res
colombia_res = False

global cuba_res
cuba_res = False

global dominica_res
dominica_res = False

global ecuador_res
ecuador_res = False

global elsalvador_res
elsalvador_res = False

global guatamela_res
guatamela_res = False

global haiti_res
haiti_res = False

global honduras_res
honduras_res = False

global mexico_res
mexico_res = False

global paraguay_res
paraguay_res = False

global peru_res
peru_res = False

global uruguay_res
uruguay_res = False

global venezuela_res
venezuela_res = False

global panama_res
panama_res = False

global costarica_res
costarica_res = False

global nicaragua_res
nicaragua_res = False

global canada_res
canada_res = False

#asia and africa

global tannutuva_res
tannutuva_res = False

global mongolia_res
mongolia_res = False

global manchukuo_res
manchukuo_res = False

global mengkukuo_res
mengkukuo_res = False

global prc_res
prc_res = False

global indochina_res
indochina_res = False

global siam_res
siam_res = False

global britishraj_res
britishraj_res = False

global australia_res
australia_res = False

global malaya_res
malaya_res = False

global indonesia_res
indonesia_res = False

global afghanistan_res
afghanistan_res = False

global iran_res
iran_res = False

global iraq_res
iraq_res = False

global palestine_res
palestine_res = False

global egypt_res
egypt_res = False

global southafrica_res
southafrica_res = False

global ethiopia_res
ethiopia_res = False

@client.event
async def on_ready():
    print("The bot is now ready")
    try:
        synced = await tree.sync(guild=discord.Object(id=1201569190826483812))
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.command()
async def host(ctx, time=None):

    role = await ctx.guild.create_role(name="Game")
    
    role = discord.utils.get(ctx.guild.roles, name="Host")
    if role in ctx.author.roles:
        pass
    else:
        await ctx.send(f"<@{ctx.author.id}> You need Host role to do this!")
        return

    with open("template.txt") as f:
        detail = f.readlines()
    details_embed = discord.Embed(title="Details")
    for details in detail:
        details_embed.add_field(name=details, value="N/A")
    message = await ctx.send(embed=details_embed)
    with open('message0.txt', 'w') as f:
        f.write(str(message.id))
    
    channel = client.get_channel(1201575035706548445)
    with open("message0.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    host_field = country_embed.fields[0]
    country_embed.remove_field(0)
    new_value = ""
    if host_field.value == "N/A":
        new_value = (f"<@{ctx.author.id}>")
        country_embed.insert_field_at(0, name=host_field.name, value=new_value)
        await message.edit(embed=country_embed)
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message0.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    time_field = country_embed.fields[1]
    country_embed.remove_field(1)
    new_value = ""
    if time_field.value == "N/A":
        new_value = (time)
        country_embed.insert_field_at(1, name=time_field.name, value=new_value)
        await message.edit(embed=country_embed)
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message0.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    rules_field = country_embed.fields[2]
    country_embed.remove_field(2)
    new_value = ""
    if rules_field.value == "N/A":
        new_value = "https://docs.google.com/document/d/1W_tkNrsK-4aX4sYHCyexLi0D39VLSs5AZrnqu2tcfs8/edit?usp=sharing"
        country_embed.insert_field_at(2, name=rules_field.name, value=new_value)
        await message.edit(embed=country_embed)
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message0.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    mods_field = country_embed.fields[3]
    country_embed.remove_field(3)
    new_value = ""
    if mods_field.value == "N/A":
        new_value = "https://steamcommunity.com/sharedfiles/filedetails/?id=2790635823 \n https://steamcommunity.com/sharedfiles/filedetails/?id=820260968"
        country_embed.insert_field_at(3, name=mods_field.name, value=new_value)
        await message.edit(embed=country_embed)
    else:
        pass

    with open("major-nations.txt") as f:
        countries = f.readlines()
    country_embed = discord.Embed(title="Major Nations")
    for country in countries:
        country_embed.add_field(name=country, value="N/A")
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
    
    with open("america-minors.txt") as f:
        countries = f.readlines()
    country_embed = discord.Embed(title="Americas")
    for country in countries:
        country_embed.add_field(name=country, value="N/A")
    message = await ctx.send(embed=country_embed)
    with open('message3.txt', 'w') as f:
        f.write(str(message.id))

    with open("asia-africa-minors.txt") as f:
        countries = f.readlines()
    country_embed = discord.Embed(title="Asia and Africa")
    for country in countries:
        country_embed.add_field(name=country, value="N/A")
    message = await ctx.send(embed=country_embed)
    with open('message4.txt', 'w') as f:
        f.write(str(message.id))

    channel = client.get_channel(1201575035706548445)
    message = await channel.send("To reserve, do '!reserve_Nation' in any chat. The command is case-sensitive! To unreserve, do !unreserve. The bot is slow, by the way.")
    with open('message5.txt', 'w') as f:
        f.write(str(message.id))
    
@client.command()
async def unreserve(ctx):
    author = (ctx.author.id)
    
    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{ctx.author.id}> Please wait...")

    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    usa_field = country_embed.fields[0]
    country_embed.remove_field(0)
    new_value = ""
    if usa_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(0, name=usa_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global usa_res
        usa_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    uk_field = country_embed.fields[1]
    country_embed.remove_field(1)
    new_value = ""
    if uk_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(1, name=uk_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global uk_res
        uk_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    france_field = country_embed.fields[2]
    country_embed.remove_field(2)
    new_value = ""
    if france_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(2, name=france_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global france_res
        france_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    germany_field = country_embed.fields[3]
    country_embed.remove_field(3)
    new_value = ""
    if germany_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(3, name=germany_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global germany_res
        germany_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    japan_field = country_embed.fields[4]
    country_embed.remove_field(4)
    new_value = ""
    if japan_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(4, name=japan_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global japan_res
        japan_res = False
    else:
        pass
    
    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    italy_field = country_embed.fields[5]
    country_embed.remove_field(5)
    new_value = ""
    if italy_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(5, name=italy_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global italy_res
        italy_res = False
    else:
        pass
    
    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    ussr_field = country_embed.fields[6]
    country_embed.remove_field(6)
    new_value = ""
    if ussr_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(6, name=ussr_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global ussr_res
        ussr_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    poland_field = country_embed.fields[7]
    country_embed.remove_field(7)
    new_value = ""
    if poland_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(7, name=poland_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global poland_res
        poland_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    china_field = country_embed.fields[8]
    country_embed.remove_field(8)
    new_value = ""
    if china_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(8, name=china_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global china_res
        china_res = False
    else:
        pass

    #Europe Minors

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    sweden_field = country_embed.fields[0]
    country_embed.remove_field(0)
    new_value = ""
    if sweden_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(0, name=sweden_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global sweden_res
        sweden_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    norway_field = country_embed.fields[1]
    country_embed.remove_field(1)
    new_value = ""
    if norway_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(1, name=norway_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global norway_res
        norway_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    finland_field = country_embed.fields[2]
    country_embed.remove_field(2)
    new_value = ""
    if finland_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(2, name=finland_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global finland_res
        finland_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    denmark_field = country_embed.fields[3]
    country_embed.remove_field(3)
    new_value = ""
    if denmark_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(3, name=denmark_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global denmark_res
        denmark_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    estonia_field = country_embed.fields[4]
    country_embed.remove_field(4)
    new_value = ""
    if estonia_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(4, name=estonia_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global estonia_res
        estonia_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    latvia_field = country_embed.fields[5]
    country_embed.remove_field(5)
    new_value = ""
    if latvia_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(5, name=latvia_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global latvia_res
        latvia_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    lithuania_field = country_embed.fields[6]
    country_embed.remove_field(6)
    new_value = ""
    if lithuania_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(6, name=lithuania_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global lithuania_res
        lithuania_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    netherlands_field = country_embed.fields[7]
    country_embed.remove_field(7)
    new_value = ""
    if netherlands_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(7, name=netherlands_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global netherlands_res
        netherlands_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    belgium_field = country_embed.fields[8]
    country_embed.remove_field(8)
    new_value = ""
    if belgium_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(8, name=belgium_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global belgium_res
        belgium_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    luxembourg_field = country_embed.fields[9]
    country_embed.remove_field(9)
    new_value = ""
    if luxembourg_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(9, name=luxembourg_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global luxembourg_res
        luxembourg_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    ireland_field = country_embed.fields[10]
    country_embed.remove_field(10)
    new_value = ""
    if ireland_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(10, name=ireland_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global ireland_res
        ireland_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    iceland_field = country_embed.fields[11]
    country_embed.remove_field(11)
    new_value = ""
    if iceland_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(11, name=iceland_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global iceland_res
        iceland_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    czechoslovakia_field = country_embed.fields[12]
    country_embed.remove_field(12)
    new_value = ""
    if czechoslovakia_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(12, name=czechoslovakia_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global czechoslovakia_res
        czechoslovakia_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    austria_field = country_embed.fields[13]
    country_embed.remove_field(13)
    new_value = ""
    if austria_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(13, name=austria_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global austria_res
        austria_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    hungary_field = country_embed.fields[14]
    country_embed.remove_field(14)
    new_value = ""
    if hungary_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(14, name=hungary_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global hungary_res
        hungary_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    romania_field = country_embed.fields[15]
    country_embed.remove_field(15)
    new_value = ""
    if romania_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(15, name=romania_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global romania_res
        romania_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    yugoslavia_field = country_embed.fields[16]
    country_embed.remove_field(16)
    new_value = ""
    if yugoslavia_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(16, name=yugoslavia_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global yugoslavia_res
        yugoslavia_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    bulgaria_field = country_embed.fields[17]
    country_embed.remove_field(17)
    new_value = ""
    if bulgaria_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(17, name=bulgaria_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global bulgaria_res
        bulgaria_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    albania_field = country_embed.fields[18]
    country_embed.remove_field(18)
    new_value = ""
    if albania_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(18, name=albania_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global albania_res
        albania_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    greece_field = country_embed.fields[19]
    country_embed.remove_field(19)
    new_value = ""
    if greece_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(19, name=greece_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global greece_res
        greece_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    turkey_field = country_embed.fields[20]
    country_embed.remove_field(20)
    new_value = ""
    if turkey_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(20, name=turkey_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global turkey_res
        turkey_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    spain_field = country_embed.fields[21]
    country_embed.remove_field(21)
    new_value = ""
    if spain_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(21, name=spain_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global spain_res
        spain_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    portugal_field = country_embed.fields[22]
    country_embed.remove_field(22)
    new_value = ""
    if portugal_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(22, name=portugal_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global portugal_res
        portugal_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    switzerland_field = country_embed.fields[23]
    country_embed.remove_field(23)
    new_value = ""
    if switzerland_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(23, name=switzerland_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global switzerland_res
        switzerland_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    argentina_field = country_embed.fields[0]
    country_embed.remove_field(0)
    new_value = ""
    if argentina_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(0, name=argentina_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global argentina_res
        argentina_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    bolivia_field = country_embed.fields[1]
    country_embed.remove_field(1)
    new_value = ""
    if bolivia_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(1, name=bolivia_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global bolivia_res
        bolivia_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    brazil_field = country_embed.fields[2]
    country_embed.remove_field(2)
    new_value = ""
    if brazil_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(2, name=brazil_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global brazil_res
        brazil_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    chile_field = country_embed.fields[3]
    country_embed.remove_field(3)
    new_value = ""
    if chile_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(3, name=chile_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global chile_res
        chile_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    colombia_field = country_embed.fields[4]
    country_embed.remove_field(4)
    new_value = ""
    if colombia_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(4, name=colombia_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global colombia_res
        colombia_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    cuba_field = country_embed.fields[5]
    country_embed.remove_field(5)
    new_value = ""
    if cuba_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(5, name=cuba_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global cuba_res
        cuba_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    dominica_field = country_embed.fields[6]
    country_embed.remove_field(6)
    new_value = ""
    if dominica_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(6, name=dominica_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global dominica_res
        dominica_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    ecuador_field = country_embed.fields[7]
    country_embed.remove_field(7)
    new_value = ""
    if ecuador_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(7, name=ecuador_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global ecuador_res
        ecuador_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    elsalvador_field = country_embed.fields[8]
    country_embed.remove_field(8)
    new_value = ""
    if elsalvador_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(8, name=elsalvador_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global elsalvador_res
        elsalvador_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    guatamela_field = country_embed.fields[9]
    country_embed.remove_field(9)
    new_value = ""
    if guatamela_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(9, name=guatamela_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global guatamela_res
        guatamela_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    haiti_field = country_embed.fields[10]
    country_embed.remove_field(10)
    new_value = ""
    if haiti_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(10, name=haiti_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global haiti_res
        haiti_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    honduras_field = country_embed.fields[11]
    country_embed.remove_field(11)
    new_value = ""
    if honduras_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(11, name=honduras_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global honduras_res
        honduras_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    mexico_field = country_embed.fields[12]
    country_embed.remove_field(12)
    new_value = ""
    if mexico_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(12, name=mexico_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global mexico_res
        mexico_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    paraguay_field = country_embed.fields[13]
    country_embed.remove_field(13)
    new_value = ""
    if paraguay_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(13, name=paraguay_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global paraguay_res
        paraguay_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    peru_field = country_embed.fields[14]
    country_embed.remove_field(14)
    new_value = ""
    if peru_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(14, name=peru_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global peru_res
        peru_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    uruguay_field = country_embed.fields[15]
    country_embed.remove_field(15)
    new_value = ""
    if uruguay_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(15, name=uruguay_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global uruguay_res
        uruguay_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    venezuela_field = country_embed.fields[16]
    country_embed.remove_field(16)
    new_value = ""
    if venezuela_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(16, name=venezuela_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global venezuela_res
        venezuela_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    panama_field = country_embed.fields[17]
    country_embed.remove_field(17)
    new_value = ""
    if panama_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(17, name=panama_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global panama_res
        panama_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    costarica_field = country_embed.fields[18]
    country_embed.remove_field(18)
    new_value = ""
    if costarica_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(18, name=costarica_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global costarica_res
        costarica_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    nicaragua_field = country_embed.fields[19]
    country_embed.remove_field(19)
    new_value = ""
    if nicaragua_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(19, name=nicaragua_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global nicaragua_res
        nicaragua_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    canada_field = country_embed.fields[20]
    country_embed.remove_field(20)
    new_value = ""
    if canada_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(20, name=canada_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global canada_res
        canada_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    tannutuva_field = country_embed.fields[0]
    country_embed.remove_field(0)
    new_value = ""
    if tannutuva_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(0, name=tannutuva_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global tannutuva_res
        tannutuva_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    mongolia_field = country_embed.fields[1]
    country_embed.remove_field(1)
    new_value = ""
    if mongolia_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(1, name=mongolia_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global mongolia_res
        mongolia_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    manchukuo_field = country_embed.fields[2]
    country_embed.remove_field(2)
    new_value = ""
    if manchukuo_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(2, name=manchukuo_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global manchukuo_res
        manchukuo_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    mengkukuo_field = country_embed.fields[3]
    country_embed.remove_field(3)
    new_value = ""
    if mengkukuo_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(3, name=mengkukuo_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global mengkukuo_res
        mengkukuo_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    prc_field = country_embed.fields[4]
    country_embed.remove_field(4)
    new_value = ""
    if prc_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(4, name=prc_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global prc_res
        prc_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    indochina_field = country_embed.fields[5]
    country_embed.remove_field(5)
    new_value = ""
    if indochina_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(5, name=indochina_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global indochina_res
        indochina_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    siam_field = country_embed.fields[6]
    country_embed.remove_field(6)
    new_value = ""
    if siam_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(6, name=siam_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global siam_res
        siam_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    britishraj_field = country_embed.fields[7]
    country_embed.remove_field(7)
    new_value = ""
    if britishraj_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(7, name=britishraj_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global britishraj_res
        britishraj_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    australia_field = country_embed.fields[8]
    country_embed.remove_field(8)
    new_value = ""
    if australia_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(8, name=australia_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global australia_res
        australia_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    malaya_field = country_embed.fields[9]
    country_embed.remove_field(9)
    new_value = ""
    if malaya_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(9, name=malaya_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global malaya_res
        malaya_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    indonesia_field = country_embed.fields[10]
    country_embed.remove_field(10)
    new_value = ""
    if indonesia_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(10, name=indonesia_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global indonesia_res
        indonesia_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    afghanistan_field = country_embed.fields[11]
    country_embed.remove_field(11)
    new_value = ""
    if afghanistan_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(11, name=afghanistan_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global afghanistan_res
        afghanistan_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    iran_field = country_embed.fields[12]
    country_embed.remove_field(12)
    new_value = ""
    if iran_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(12, name=iran_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global iran_res
        iran_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    iraq_field = country_embed.fields[13]
    country_embed.remove_field(13)
    new_value = ""
    if iraq_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(13, name=iraq_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global iraq_res
        iraq_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    palestine_field = country_embed.fields[14]
    country_embed.remove_field(14)
    new_value = ""
    if palestine_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(14, name=palestine_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global palestine_res
        palestine_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    egypt_field = country_embed.fields[15]
    country_embed.remove_field(15)
    new_value = ""
    if egypt_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(15, name=egypt_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global egypt_res
        egypt_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    southafrica_field = country_embed.fields[16]
    country_embed.remove_field(16)
    new_value = ""
    if southafrica_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(16, name=southafrica_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global southafrica_res
        southafrica_res = False
    else:
        pass

    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    country_embed = message.embeds[0]
    ethiopia_field = country_embed.fields[17]
    country_embed.remove_field(17)
    new_value = ""
    if ethiopia_field.value == (f"<@{author}>"):
        new_value = "N/A"
        country_embed.insert_field_at(17, name=ethiopia_field.name, value=new_value)
        await message.edit(embed=country_embed)
        global ethiopia_res
        ethiopia_res = False
    else:
        pass

    guild = discord.utils.get(client.guilds, name="Guardian")
    role = discord.utils.get(guild.roles, name="Game")
    await ctx.author.remove_roles(role)

    with open(f"ReservedUsers.txt", "r") as f:
        lines = f.readlines()
    with open(f"ReservedUsers.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != str(author):
                f.write(line)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now unreserved!")




@client.command()
async def reserve_USA(ctx):

    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global usa_res

    if usa_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        usa_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)

    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

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

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for the USA! You're boutta have a lame-ass game :joy:")

@client.command()
async def reserve_UK(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global uk_res

    if uk_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        uk_res = True
        
    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")
    
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

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for the UK! Have a nice time sitting on your island for 6 hours :joy:")

@client.command()
async def reserve_France(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global france_res

    if france_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        france_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)

    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")
    
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

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for France! Good luck with Germany!")

@client.command()
async def reserve_Germany(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global germany_res

    if germany_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        germany_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    germany_field = country_embed.fields[3]
    country_embed.remove_field(3)
    new_value = ""
    if germany_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{germany_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(3, name=germany_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Germany... Good luck man.")

@client.command()
async def reserve_Japan(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global japan_res

    if japan_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        japan_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    japan_field = country_embed.fields[4]
    country_embed.remove_field(4)
    new_value = ""
    if japan_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{japan_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(4, name=japan_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Japan! Please have game impact :joy:")

@client.command()
async def reserve_Italy(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global italy_res

    if italy_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        italy_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    italy_field = country_embed.fields[5]
    country_embed.remove_field(5)
    new_value = ""
    if italy_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{italy_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(5, name=italy_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Italy, aka little Germany! Good luck with game impact, lil bro :joy:")

@client.command()
async def reserve_USSR(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
    
    global ussr_res

    if ussr_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        ussr_res = True

    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")
    
    country_embed = message.embeds[0]
    ussr_field = country_embed.fields[6]
    country_embed.remove_field(6)
    new_value = ""
    if ussr_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ussr_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(6, name=ussr_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for the USSR... Do or die, lil bro...")

@client.command()
async def reserve_Poland(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global poland_res

    if poland_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        poland_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)

    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    poland_field = country_embed.fields[7]
    country_embed.remove_field(7)
    new_value = ""
    if poland_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{poland_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(7, name=poland_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Poland! You must be INSANE :joy:")

@client.command()
async def reserve_China(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global china_res

    if china_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        china_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    china_field = country_embed.fields[8]
    country_embed.remove_field(8)
    new_value = ""
    if china_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{china_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(8, name=china_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for China! Have a nice time larping as a brick wall :joy:")

#EUROPE

@client.command()
async def reserve_Sweden(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global sweden_res

    if sweden_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        sweden_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    sweden_field = country_embed.fields[0]
    country_embed.remove_field(0)
    new_value = ""
    if sweden_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{sweden_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(0, name=sweden_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Sweden!")

@client.command()
async def reserve_Norway(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global norway_res

    if norway_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        norway_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    norway_field = country_embed.fields[1]
    country_embed.remove_field(1)
    new_value = ""
    if norway_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{norway_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(1, name=norway_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Norway!")

@client.command()
async def reserve_Finland(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global finland_res

    if finland_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        finland_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    finland_field = country_embed.fields[2]
    country_embed.remove_field(2)
    new_value = ""
    if finland_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{finland_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(2, name=finland_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Finland!")

@client.command()
async def reserve_Denmark(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global denmark_res

    if denmark_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        denmark_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    denmark_field = country_embed.fields[3]
    country_embed.remove_field(3)
    new_value = ""
    if denmark_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{denmark_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(3, name=denmark_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Denmark!")

@client.command()
async def reserve_Estonia(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global estonia_res

    if estonia_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        estonia_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    estonia_field = country_embed.fields[4]
    country_embed.remove_field(4)
    new_value = ""
    if estonia_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{estonia_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(4, name=estonia_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Estonia!")

@client.command()
async def reserve_Latvia(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global latvia_res

    if latvia_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        latvia_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    latvia_field = country_embed.fields[5]
    country_embed.remove_field(5)
    new_value = ""
    if latvia_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{latvia_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(5, name=latvia_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Latvia!")

@client.command()
async def reserve_Lithuania(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global lithuania_res

    if lithuania_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        lithuania_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    lithuania_field = country_embed.fields[6]
    country_embed.remove_field(6)
    new_value = ""
    if lithuania_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{lithuania_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(6, name=lithuania_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Lithuania!")

@client.command()
async def reserve_Netherlands(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global netherlands_res

    if netherlands_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        netherlands_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    netherlands_field = country_embed.fields[7]
    country_embed.remove_field(7)
    new_value = ""
    if netherlands_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{netherlands_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(7, name=netherlands_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for the Netherlands!")

@client.command()
async def reserve_Belgium(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global belgium_res

    if belgium_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        belgium_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    belgium_field = country_embed.fields[8]
    country_embed.remove_field(8)
    new_value = ""
    if belgium_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{belgium_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(8, name=belgium_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Belgium!")

@client.command()
async def reserve_Luxembourg(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global luxembourg_res

    if luxembourg_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        luxembourg_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    luxembourg_field = country_embed.fields[9]
    country_embed.remove_field(9)
    new_value = ""
    if luxembourg_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{luxembourg_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(9, name=luxembourg_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Luxembourg!")

@client.command()
async def reserve_Ireland(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global ireland_res

    if ireland_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        ireland_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    ireland_field = country_embed.fields[10]
    country_embed.remove_field(10)
    new_value = ""
    if ireland_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ireland_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(10, name=ireland_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Ireland!")

@client.command()
async def reserve_Iceland(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global iceland_res

    if iceland_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        iceland_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    iceland_field = country_embed.fields[11]
    country_embed.remove_field(11)
    new_value = ""
    if iceland_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{iceland_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(11, name=iceland_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Iceland!")

@client.command()
async def reserve_Czechoslovakia(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global czechoslovakia_res

    if czechoslovakia_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        czechoslovakia_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    czechoslovakia_field = country_embed.fields[12]
    country_embed.remove_field(12)
    new_value = ""
    if czechoslovakia_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{czechoslovakia_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(12, name=czechoslovakia_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Czechoslovakia!")

@client.command()
async def reserve_Austria(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global austria_res

    if austria_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        austria_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    austria_field = country_embed.fields[13]
    country_embed.remove_field(13)
    new_value = ""
    if austria_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{austria_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(13, name=austria_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Austria!")

@client.command()
async def reserve_Hungary(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global hungary_res

    if hungary_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        hungary_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    hungary_field = country_embed.fields[14]
    country_embed.remove_field(14)
    new_value = ""
    if hungary_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{hungary_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(14, name=hungary_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Hungary!")

@client.command()
async def reserve_Romania(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global romania_res

    if romania_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        romania_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    romania_field = country_embed.fields[15]
    country_embed.remove_field(15)
    new_value = ""
    if romania_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{romania_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(15, name=romania_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Romania!")

@client.command()
async def reserve_Yugoslavia(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global yugoslavia_res

    if yugoslavia_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        yugoslavia_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    yugoslavia_field = country_embed.fields[16]
    country_embed.remove_field(16)
    new_value = ""
    if yugoslavia_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{yugoslavia_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(16, name=yugoslavia_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Yugoslavia!")

@client.command()
async def reserve_Bulgaria(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global bulgaria_res

    if bulgaria_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        bulgaria_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    bulgaria_field = country_embed.fields[17]
    country_embed.remove_field(17)
    new_value = ""
    if bulgaria_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{bulgaria_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(17, name=bulgaria_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Bulgaria!")

@client.command()
async def reserve_Albania(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global albania_res

    if albania_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        albania_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    albania_field = country_embed.fields[18]
    country_embed.remove_field(18)
    new_value = ""
    if albania_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{albania_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(18, name=albania_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Albania!")

@client.command()
async def reserve_Greece(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global greece_res

    if greece_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        greece_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    greece_field = country_embed.fields[19]
    country_embed.remove_field(19)
    new_value = ""
    if greece_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{greece_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(19, name=greece_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Greece!")

@client.command()
async def reserve_Turkey(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global turkey_res

    if turkey_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        turkey_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    turkey_field = country_embed.fields[20]
    country_embed.remove_field(20)
    new_value = ""
    if turkey_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{turkey_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(20, name=turkey_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Turkey!")

@client.command()
async def reserve_Spain(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global spain_res

    if spain_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        spain_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    spain_field = country_embed.fields[21]
    country_embed.remove_field(21)
    new_value = ""
    if spain_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{spain_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(21, name=spain_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Spain!")

@client.command()
async def reserve_Portugal(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global portugal_res

    if portugal_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        portugal_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    portugal_field = country_embed.fields[22]
    country_embed.remove_field(22)
    new_value = ""
    if portugal_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{portugal_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(22, name=portugal_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Portugal!")

@client.command()
async def reserve_Switzerland(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global switzerland_res

    if switzerland_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        switzerland_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    switzerland_field = country_embed.fields[23]
    country_embed.remove_field(23)
    new_value = ""
    if switzerland_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{switzerland_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(23, name=switzerland_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Switzerland!")

#Americas   
    
@client.command()
async def reserve_Argentina(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global argentina_res

    if argentina_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        argentina_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    argentina_field = country_embed.fields[0]
    country_embed.remove_field(0)
    new_value = ""
    if  argentina_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ argentina_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(0, name= argentina_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Argentina!")

@client.command()
async def reserve_Bolivia(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global bolivia_res

    if bolivia_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        bolivia_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    bolivia_field = country_embed.fields[1]
    country_embed.remove_field(1)
    new_value = ""
    if   bolivia_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{bolivia_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(1, name=bolivia_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Bolivia!")

@client.command()
async def reserve_Brazil(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global brazil_res

    if brazil_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        brazil_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    brazil_field = country_embed.fields[2]
    country_embed.remove_field(2)
    new_value = ""
    if  brazil_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ brazil_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(2, name= brazil_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Brazil!")

@client.command()
async def reserve_Chile(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global chile_res

    if chile_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        chile_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    chile_field = country_embed.fields[3]
    country_embed.remove_field(3)
    new_value = ""
    if  chile_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ chile_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(3, name= chile_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Chile!")

@client.command()
async def reserve_Colombia(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global colombia_res

    if colombia_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        colombia_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    colombia_field = country_embed.fields[4]
    country_embed.remove_field(4)
    new_value = ""
    if  colombia_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ colombia_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(4, name= colombia_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Colombia!")

@client.command()
async def reserve_Cuba(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global cuba_res

    if cuba_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        cuba_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    cuba_field = country_embed.fields[5]
    country_embed.remove_field(5)
    new_value = ""
    if  cuba_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ cuba_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(5, name= cuba_field.name, value=new_value)
    await message.edit(embed=country_embed)
    
    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Cuba!")

@client.command()
async def reserve_Dominica(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global dominica_res

    if dominica_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        dominica_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    dominica_field = country_embed.fields[6]
    country_embed.remove_field(6)
    new_value = ""
    if  dominica_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ dominica_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(6, name= dominica_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Dominica!")

@client.command()
async def reserve_Ecuador(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global ecuador_res

    if ecuador_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        ecuador_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    ecuador_field = country_embed.fields[7]
    country_embed.remove_field(7)
    new_value = ""
    if  ecuador_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ ecuador_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(7, name= ecuador_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Ecuador!")

@client.command()
async def reserve_El_Salvador(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global elsalvador_res

    if elsalvador_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        elsalvador_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    el_salvador_field = country_embed.fields[8]
    country_embed.remove_field(8)
    new_value = ""
    if  el_salvador_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ el_salvador_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(8, name= el_salvador_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for El Salvador!")

@client.command()
async def reserve_Guatamela(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global guatamela_res

    if guatamela_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        guatamela_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    guatamela_field = country_embed.fields[9]
    country_embed.remove_field(9)
    new_value = ""
    if  guatamela_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ guatamela_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(9, name= guatamela_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Guatamela!")

@client.command()
async def reserve_Haiti(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global haiti_res

    if haiti_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        haiti_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    haiti_field = country_embed.fields[10]
    country_embed.remove_field(10)
    new_value = ""
    if  haiti_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ haiti_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(10, name= haiti_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Haiti!")

@client.command()
async def reserve_Honduras(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global honduras_res

    if honduras_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        honduras_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    honduras_field = country_embed.fields[11]
    country_embed.remove_field(11)
    new_value = ""
    if   honduras_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{  honduras_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(11, name= honduras_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Honduras!")

@client.command()
async def reserve_Mexico(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global mexico_res

    if mexico_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        mexico_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    mexico_field = country_embed.fields[12]
    country_embed.remove_field(12)
    new_value = ""
    if  mexico_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ mexico_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(12, name= mexico_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Mexico!")

@client.command()
async def reserve_Paraguay(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global paraguay_resres

    if paraguay_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        paraguay_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    paraguay_field = country_embed.fields[13]
    country_embed.remove_field(13)
    new_value = ""
    if  paraguay_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{paraguay_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(13, name=paraguay_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Paraguay!")

@client.command()
async def reserve_Peru(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global peru_res

    if peru_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        peru_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    peru_field = country_embed.fields[14]
    country_embed.remove_field(14)
    new_value = ""
    if  peru_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ peru_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(14, name= peru_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Peru!")

@client.command()
async def reserve_Uruguay(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global uruguay_res

    if uruguay_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        uruguay_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    uruguay_field = country_embed.fields[15]
    country_embed.remove_field(15)
    new_value = ""
    if uruguay_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{uruguay_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(15, name=uruguay_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Uruguay!")
    
@client.command()
async def reserve_Venezuela(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global venezuela_res

    if venezuela_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        venezuela_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    venezuela_field = country_embed.fields[16]
    country_embed.remove_field(16)
    new_value = ""
    if venezuela_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{venezuela_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(16, name=venezuela_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Venezuela!")
    
@client.command()
async def reserve_Panama(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global panama_res

    if panama_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        panama_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    panama_field = country_embed.fields[17]
    country_embed.remove_field(17)
    new_value = ""
    if panama_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{panama_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(17, name=panama_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Panama!")
    
@client.command()
async def reserve_Costa_Rica(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global costarica_res

    if costarica_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        costarica_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    costa_rica_field = country_embed.fields[18]
    country_embed.remove_field(18)
    new_value = ""
    if costa_rica_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{costa_rica_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(18, name=costa_rica_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Costa Rica!")
    
@client.command()
async def reserve_Nicaragua(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global nicaragua_res

    if nicaragua_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        nicaragua_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    nicaragua_field = country_embed.fields[19]
    country_embed.remove_field(19)
    new_value = ""
    if nicaragua_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{nicaragua_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(19, name=nicaragua_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Nicaragua!")
    
@client.command()
async def reserve_Canada(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global canada_res

    if canada_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        canada_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    canada_field = country_embed.fields[21]
    country_embed.remove_field(21)
    new_value = ""
    if canada_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{canada_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(21, name=canada_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Canada!")

#Asia

@client.command()
async def reserve_Tannu_Tuva(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global tannutuva_res

    if tannutuva_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        tannutuva_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    tannu_tuva_field = country_embed.fields[0]
    country_embed.remove_field(0)
    new_value = ""
    if  tannu_tuva_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ tannu_tuva_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(0, name= tannu_tuva_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Tannu Tuva!")

@client.command()
async def reserve_Mongolia(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global mongolia_res

    if mongolia_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        mongolia_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    mongolia_field = country_embed.fields[1]
    country_embed.remove_field(1)
    new_value = ""
    if mongolia_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{mongolia_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(1, name=mongolia_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Mongolia!")
    
@client.command()
async def reserve_Manchukuo(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global manchukuo_res

    if manchukuo_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        manchukuo_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    manchukuo_field = country_embed.fields[2]
    country_embed.remove_field(2)
    new_value = ""
    if manchukuo_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{manchukuo_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(2, name=manchukuo_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Manchukuo!")
    
@client.command()
async def reserve_Mengkukuo(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global mengkukuo_res

    if mengkukuo_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        mengkukuo_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    mengkukuo_field = country_embed.fields[3]
    country_embed.remove_field(3)
    new_value = ""
    if mengkukuo_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{mengkukuo_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(3, name=mengkukuo_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Mengkukuo!")
    
@client.command()
async def reserve_PRC(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global prc_res

    if prc_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        prc_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    prc_field = country_embed.fields[4]
    country_embed.remove_field(4)
    new_value = ""
    if prc_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{prc_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(4, name=prc_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for the PRC!")
    
@client.command()
async def reserve_Indochina(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global indochina_res

    if indochina_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        indochina_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    indochina_field = country_embed.fields[5]
    country_embed.remove_field(5)
    new_value = ""
    if indochina_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{indochina_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(5, name=indochina_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for French Indochina!")
    
@client.command()
async def reserve_Siam(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global siam_res

    if siam_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        siam_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    siam_field = country_embed.fields[6]
    country_embed.remove_field(6)
    new_value = ""
    if siam_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{siam_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(6, name=siam_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Siam!")
    
@client.command()
async def reserve_British_Raj(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global britishraj_res

    if britishraj_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        britishraj_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    british_raj_field = country_embed.fields[7]
    country_embed.remove_field(7)
    new_value = ""
    if british_raj_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{british_raj_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(7, name=british_raj_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for the British Raj!")
    
@client.command()
async def reserve_Australia(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global australia_res

    if australia_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        australia_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    australia_field = country_embed.fields[8]
    country_embed.remove_field(8)
    new_value = ""
    if australia_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ australia_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(8, name= australia_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Australia!")
    
@client.command()
async def reserve_Malaya(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global malaya_res

    if malaya_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        malaya_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    malaya_field = country_embed.fields[9]
    country_embed.remove_field(9)
    new_value = ""
    if malaya_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{malaya_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(9, name=malaya_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Malaya!")

@client.command()
async def reserve_Indonesia(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global indonesia_res

    if indonesia_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        indonesia_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    indonesia_field = country_embed.fields[10]
    country_embed.remove_field(10)
    new_value = ""
    if indonesia_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{indonesia_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(10, name=indonesia_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for the Dutch East Indies!")
    
@client.command()
async def reserve_Afghanistan(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global afghanistan_res

    if afghanistan_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        afghanistan_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    afghanistan_field = country_embed.fields[11]
    country_embed.remove_field(11)
    new_value = ""
    if afghanistan_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{afghanistan_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(11, name=afghanistan_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)
    
    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Afghanistan!")

@client.command()
async def reserve_Iran(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global iran_res

    if iran_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        iran_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    iran_field = country_embed.fields[12]
    country_embed.remove_field(12)
    new_value = ""
    if iran_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{iran_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(12, name=iran_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Iran!")
    
@client.command()
async def reserve_Iraq(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global iraq_res

    if iraq_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        iraq_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    iraq_field = country_embed.fields[13]
    country_embed.remove_field(13)
    new_value = ""
    if  iraq_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ iraq_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(13, name= iraq_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Iraq!")
    
@client.command()
async def reserve_Palestine(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global palestine_res

    if palestine_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        palestine_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    palestine_field = country_embed.fields[14]
    country_embed.remove_field(14)
    new_value = ""
    if  palestine_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{palestine_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(14, name= palestine_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Palestine!")
    
@client.command()
async def reserve_Egypt(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global egypt_res

    if egypt_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        egypt_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    egypt_field = country_embed.fields[15]
    country_embed.remove_field(15)
    new_value = ""
    if egypt_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{egypt_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(15, name=egypt_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Egypt!")
    
@client.command()
async def reserve_South_Africa(ctx):

    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global southafrica_res

    if southafrica_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        southafrica_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    south_africa_field = country_embed.fields[16]
    country_embed.remove_field(16)
    new_value = ""
    if south_africa_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{south_africa_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(16, name=south_africa_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for South Africa!")
    
@client.command()
async def reserve_Ethiopia(ctx):



    author = (ctx.author.id)
    with open("ReservedUsers.txt") as f:
        if str(author) in f.read():
            await ctx.send(f"<@{ctx.author.id}> You're already reserved, dum-dum :joy:")
            return
        
    global ethiopia_res

    if ethiopia_res == True:
        this_channel = ctx.channel.id
        channel = client.get_channel(int(this_channel))
        await channel.send(f"<@{ctx.author.id}> TAKEN!")
        return
    else:
        ethiopia_res = True
    
    channel = client.get_channel(1201575035706548445)
    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    
    with open("ReservedUsers.txt", "a") as f:
        f.write(str(author) + "\n")

    country_embed = message.embeds[0]
    ethiopia_field = country_embed.fields[17]
    country_embed.remove_field(17)
    new_value = ""
    if ethiopia_field.value == "N/A":
        new_value = (f"<@{author}>")
    else:
        new_value = f"{ethiopia_field.value}\n" + (f"<@{author}>")
    country_embed.insert_field_at(17, name=ethiopia_field.name, value=new_value)
    await message.edit(embed=country_embed)

    role = discord.utils.get(message.guild.roles, name="Game")
    await ctx.author.add_roles(role)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{author}> You're now reserved for Ethiopia!")

@client.command()
async def unreserve_Poland(ctx, user=None):

    role = discord.utils.get(ctx.guild.roles, name="Host")
    if role in ctx.author.roles:
        pass
    else:
        await ctx.send(f"<@{ctx.author.id}> You need Host role to do this!")
        return
        
    global ethiopia_res
    ethiopia_res = False
    
    channel = client.get_channel(1201575035706548445)
    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)

    country_embed = message.embeds[0]
    poland_field = country_embed.fields[7]
    country_embed.remove_field(7)
    new_value = ""
    if poland_field.value == (f"<@{user}>"):
        new_value = "N/A"
        country_embed.insert_field_at(7, name=poland_field.name, value=new_value)
        await message.edit(embed=country_embed)
    else:
        pass

    guild = discord.utils.get(client.guilds, name="Guardian")
    role = discord.utils.get(guild.roles, name="Game")
    await ctx.author.remove_roles(role)

    with open(f"ReservedUsers.txt", "r") as f:
        lines = f.readlines()
    with open(f"ReservedUsers.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != str(user):
                f.write(line)

    this_channel = ctx.channel.id
    channel = client.get_channel(int(this_channel))
    await channel.send(f"<@{user}> Unreserved!")
    

#Ending

@client.command()
async def endhost(ctx):

    channel = client.get_channel(1201575035706548445)

    role = discord.utils.get(ctx.guild.roles, name="Host")
    if role in ctx.author.roles:
        pass
    else:
        await ctx.send(f"<@{ctx.author.id}> You need Host role to do this!")
        return

    with open("ReservedUsers.txt", "w") as f:
        f.truncate

    with open("message0.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    await message.delete()

    with open("message.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    await message.delete()

    with open("message2.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    await message.delete()

    with open("message3.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    await message.delete()

    with open("message4.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    await message.delete()

    with open("message5.txt", "r") as f:
        message_id = int(f.read())
    message = await channel.fetch_message(message_id)
    await message.delete()

    role = discord.utils.get(ctx.message.guild.roles, name="Game")
    await role.delete()

    global usa_res
    usa_res = False

    global uk_res
    uk_res = False

    global france_res
    france_res = False

    global germany_res
    germany_res = False

    global japan_res
    japan_res = False

    global italy_res
    italy_res = False

    global ussr_res
    ussr_res = False

    global poland_res
    poland_res = False

    global china_res
    china_res = False

    global sweden_res
    sweden_res = False

    global norway_res
    norway_res = False

    global finland_res
    finland_res = False

    global denmark_res
    denmark_res = False

    global estonia_res
    estonia_res = False

    global latvia_res
    latvia_res = False

    global lithuania_res
    lithuania_res = False

    global netherlands_res
    netherlands_res = False

    global belgium_res
    belgium_res = False

    global luxembourg_res
    luxembourg_res = False

    global ireland_res
    ireland_res = False

    global iceland_res
    iceland_res = False

    global czechoslovakia_res
    czechoslovakia_res = False

    global austria_res
    austria_res = False

    global hungary_res
    hungary_res = False

    global romania_res
    romania_res = False

    global yugoslavia_res
    yugoslavia_res = False

    global bulgaria_res
    bulgaria_res = False

    global albania_res
    albania_res = False

    global greece_res
    greece_res = False

    global turkey_res
    turkey_res = False

    global spain_res
    spain_res = False

    global portugal_res
    portugal_res = False

    global switzerland_res
    switzerland_res = False

    #americas

    global argentina_res
    argentina_res = False

    global bolivia_res
    bolivia_res = False

    global brazil_res
    brazil_res = False

    global chile_res
    chile_res = False

    global colombia_res
    colombia_res = False

    global cuba_res
    cuba_res = False

    global dominica_res
    dominica_res = False

    global ecuador_res
    ecuador_res = False

    global elsalvador_res
    elsalvador_res = False

    global guatamela_res
    guatamela_res = False

    global haiti_res
    haiti_res = False

    global honduras_res
    honduras_res = False

    global mexico_res
    mexico_res = False

    global paraguay_res
    paraguay_res = False

    global peru_res
    peru_res = False

    global uruguay_res
    uruguay_res = False

    global venezuela_res
    venezuela_res = False

    global panama_res
    panama_res = False

    global costarica_res
    costarica_res = False

    global nicaragua_res
    nicaragua_res = False

    global canada_res
    canada_res = False

    #asia and africa

    global tannutuva_res
    tannutuva_res = False

    global mongolia_res
    mongolia_res = False

    global manchukuo_res
    manchukuo_res = False

    global mengkukuo_res
    mengkukuo_res = False

    global prc_res
    prc_res = False

    global indochina_res
    indochina_res = False

    global siam_res
    siam_res = False

    global britishraj_res
    britishraj_res = False

    global australia_res
    australia_res = False

    global malaya_res
    malaya_res = False

    global indonesia_res
    indonesia_res = False

    global afghanistan_res
    afghanistan_res = False

    global iran_res
    iran_res = False

    global iraq_res
    iraq_res = False

    global palestine_res
    palestine_res = False

    global egypt_res
    egypt_res = False

    global southafrica_res
    southafrica_res = False

    global ethiopia_res
    ethiopia_res = False


BOTTOKEN = ('')


client.run(BOTTOKEN)