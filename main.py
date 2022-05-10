import discord
from discord.ext import commands
import random
import config

client = commands.Bot(command_prefix = config.config["PREFIX"], intents = discord.Intents.all())
client.remove_command("help")
GAME = discord.Game(config.config["GAME"])


@client.event
async def on_ready():
    print("The bot was connected to the server under the tag {0.user}!".format(client))
    await client.change_presence(status = discord.Status.online, activity = GAME)



@client.command()
async def help(ctx):    #help
    emb = discord.Embed(title = "Help", color = config.config["DEFAULTCOLOR"])
    f = open("text/help.txt", "r", encoding = "utf-8")
    text = f.read().split(" >")
    for i in range(len(text)):
        newtext = text[i].split(" | ")
        emb.add_field(name = f"{newtext[0]}".format(config.config["PREFIX"]), value = f"{newtext[1]}")
    emb.add_field(name = "Open source", value = "[GitHub project](https://github.com/Belyanchik/miniGamesDiscordBot)")
    await ctx.send(embed = emb)


#I wrote this piece of code a long time ago, perhaps it needs optimization in the future
@client.command()
async def ttt(ctx, member: discord.Member):     #Tic-tac-toe
    emb = discord.Embed(title = "Offer to play Tic-Tac-Toe!", color = config.config["DEFAULTCOLOR"])
    emb.add_field(name = "Yes: ✅", value="No: ❌")
    message = await ctx.send(f"<@{member.id}>", embed = emb)
    await message.add_reaction("✅")
    await message.add_reaction("❌")

    reaction_vib = ["✅", "❌"]

    yes = "✅"
    no = "❌"

    def check(reaction, user):
        return user == member and str(reaction.emoji) in reaction_vib

    def checkx(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reaction_vib

    reaction, user = await client.wait_for('reaction_add', timeout = 15.0, check = check)  #setting the time for the reaction of the cross

    if str(reaction.emoji) == yes:
        emb = discord.Embed(title = "The game begins!", color = config.config["GREENCOLOR"])
        await ctx.send(embed = emb)

        str1 = ["1️⃣", "2️⃣", "3️⃣"]
        str2 = ["4️⃣", "5️⃣", "6️⃣"]
        str3 = ["7️⃣", "8️⃣", "9️⃣"]

        str1b = "1"
        str2b = "2"
        str3b = "3"
        str4b = "4"
        str5b = "5"
        str6b = "6"
        str7b = "7"
        str8b = "8"
        str9b = "9"

        win = False
        hodx = True

        x = ctx.author.id
        o = member.id

        emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
        emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
        message = await ctx.send("Preparing the playing field, wait!", embed = emb)

        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")
        await message.add_reaction("4️⃣")
        await message.add_reaction("5️⃣")
        await message.add_reaction("6️⃣")
        await message.add_reaction("7️⃣")
        await message.add_reaction("8️⃣")
        await message.add_reaction("9️⃣")

        reaction_vib = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]

        while (win != True):
            if (str1b == "x" and str4b == "x" and str7b == "x" or str1b == "o" and str4b == "o" and str7b == "o"):
                if (hodx == False):
                    emb = discord.Embed(title = "The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{x}>")
                    await ctx.send(embed = emb)
                    break
                elif (hodx == True):
                    emb = discord.Embed(title=f"The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{o}>")
                    await ctx.send(embed = emb)
                    break

            elif (str2b == "x" and str5b == "x" and str8b == "x" or str2b == "o" and str5b == "o" and str8b == "o"):
                if (hodx == False):
                    emb = discord.Embed(title = "The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{x}>")
                    await ctx.send(embed = emb)
                    break
                elif (hodx == True):
                    emb = discord.Embed(title = f"The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{o}>")
                    await ctx.send(embed = emb)
                    break

            elif (str3b == "x" and str6b == "x" and str9b == "x" or str3b == "o" and str6b == "o" and str9b == "o"):
                if (hodx == False):
                    emb = discord.Embed(title = "The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{x}>")
                    await ctx.send(embed = emb)
                    break
                elif (hodx == True):
                    emb = discord.Embed(title = f"The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{o}>")
                    await ctx.send(embed = emb)
                    break

            elif (str1b == "x" and str2b == "x" and str3b == "x" or str1b == "o" and str2b == "o" and str3b == "o"):
                if (hodx == False):
                    emb = discord.Embed(title = "The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{x}>")
                    await ctx.send(embed = emb)
                    break
                elif (hodx == True):
                    emb = discord.Embed(title = f"The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{o}>")
                    await ctx.send(embed=emb)
                    break

            elif (str4b == "x" and str5b == "x" and str6b == "x" or str4b == "o" and str5b == "o" and str6b == "o"):
                if (hodx == False):
                    emb = discord.Embed(title = "The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{x}>")
                    await ctx.send(embed = emb)
                    break
                elif (hodx == True):
                    emb = discord.Embed(title = f"The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{o}>")
                    await ctx.send(embed = emb)
                    break

            elif (str7b == "x" and str8b == "x" and str9b == "x" or str7b == "o" and str8b == "o" and str9b == "o"):
                if (hodx == False):
                    emb = discord.Embed(title = "The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{x}>")
                    await ctx.send(embed = emb)
                    break
                elif (hodx == True):
                    emb = discord.Embed(title = f"The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{o}>")
                    await ctx.send(embed = emb)
                    break

            elif (str1b == "x" and str5b == "x" and str9b == "x" or str1b == "o" and str5b == "o" and str9b == "o"):
                if (hodx == False):
                    emb = discord.Embed(title = "The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{x}>")
                    await ctx.send(embed = emb)
                    break
                elif (hodx == True):
                    emb = discord.Embed(title = f"The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{o}>")
                    await ctx.send(embed = emb)
                    break

            elif (str3b == "x" and str5b == "x" and str7b == "x" or str3b == "o" and str5b == "o" and str7b == "o"):
                if (hodx == False):
                    emb = discord.Embed(title = "The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{x}>")
                    await ctx.send(embed = emb)
                    break
                elif (hodx == True):
                    emb = discord.Embed(title = f"The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner", value = f"<@{o}>")
                    await ctx.send(embed = emb)
                    break

            elif (reaction_vib == []):
                emb = discord.Embed(title = "Draw!", color = config.config["DEFAULTCOLOR"])
                await ctx.send(embed = emb)
                break

            else:
                None

            if (hodx == True):  #the move of the cross
                one = "1️⃣"
                two = "2️⃣"
                three = "3️⃣"
                four = "4️⃣"
                five = "5️⃣"
                six = "6️⃣"
                seven = "7️⃣"
                eight = "8️⃣"
                nine = "9️⃣"

                await message.edit(content = f"He's walking now <@{x}> (❌)")
                reaction, user = await client.wait_for('reaction_add', timeout = 15.0, check = checkx)  #setting the reaction time

                if str(reaction.emoji) == one:
                    str1.pop(0)
                    str1.insert(0, "❌")
                    str1b = "x"
                    reaction_vib.remove("1️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == two:
                    str1.pop(1)
                    str1.insert(1, "❌")
                    str2b = "x"
                    reaction_vib.remove("2️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == three:
                    str1.pop(2)
                    str1.append("❌")
                    str3b = "x"
                    reaction_vib.remove("3️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == four:
                    str2.pop(0)
                    str2.insert(0, "❌")
                    str4b = "x"
                    reaction_vib.remove("4️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == five:
                    str2.pop(1)
                    str2.insert(1, "❌")
                    str5b = "x"
                    reaction_vib.remove("5️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == six:
                    str2.pop(2)
                    str2.append("❌")
                    str6b = "x"
                    reaction_vib.remove("6️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == seven:
                    str3.pop(0)
                    str3.insert(0, "❌")
                    str7b = "x"
                    reaction_vib.remove("7️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == eight:
                    str3.pop(1)
                    str3.insert(1, "❌")
                    str8b = "x"
                    reaction_vib.remove("8️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == nine:
                    str3.pop(2)
                    str3.append("❌")
                    str9b = "x"
                    reaction_vib.remove("9️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                hodx = False

            elif (hodx == False):  #zero stroke
                one = "1️⃣"
                two = "2️⃣"
                three = "3️⃣"
                four = "4️⃣"
                five = "5️⃣"
                six = "6️⃣"
                seven = "7️⃣"
                eight = "8️⃣"
                nine = "9️⃣"

                await message.edit(content = f"He's walking now <@{o}> (⭕)")
                reaction, user = await client.wait_for('reaction_add', timeout = 15.0, check = check)  #setting the reaction time

                if str(reaction.emoji) == one:
                    str1.pop(0)
                    str1.insert(0, "⭕")
                    str1b = "o"
                    reaction_vib.remove("1️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == two:
                    str1.pop(1)
                    str1.insert(1, "⭕")
                    str2b = "o"
                    reaction_vib.remove("2️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == three:
                    str1.pop(2)
                    str1.append("⭕")
                    str3b = "o"
                    reaction_vib.remove("3️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == four:
                    str2.pop(0)
                    str2.insert(0, "⭕")
                    str4b = "o"
                    reaction_vib.remove("4️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == five:
                    str2.pop(1)
                    str2.insert(1, "⭕")
                    str5b = "o"
                    reaction_vib.remove("5️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == six:
                    str2.pop(2)
                    str2.append("⭕")
                    str6b = "o"
                    reaction_vib.remove("6️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == seven:
                    str3.pop(0)
                    str3.insert(0, "⭕")
                    str7b = "o"
                    reaction_vib.remove("7️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == eight:
                    str3.pop(1)
                    str3.insert(1, "⭕")
                    str8b = "o"
                    reaction_vib.remove("8️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                elif str(reaction.emoji) == nine:
                    str3.pop(2)
                    str3.append("⭕")
                    str9b = "o"
                    reaction_vib.remove("9️⃣")
                    emb = discord.Embed(title = "Playing field", color = config.config["DEFAULTCOLOR"])
                    emb.add_field(name = f"""{", ".join(str1)}
{", ".join(str2)}
{", ".join(str3)}""", value = "15 seconds per turn")
                    await message.edit(embed = emb)

                hodx = True

    elif str(reaction.emoji) == no:
        emb = discord.Embed(title = "Game canceled!", color = config.config["REDCOLOR"])
        return await ctx.send(embed = emb)


@ttt.error
async def ttt_error(ctx, error):    #tic-tac-toe error handling
    if isinstance(error, commands.MissingRequiredArgument):
        emb = discord.Embed(title = "Missing mention!", color = config.config["REDCOLOR"])
        await ctx.send(embed = emb)
    elif isinstance(error, commands.CommandInvokeError):
        emb = discord.Embed(title = "Response waiting time is out!", color = config.config["REDCOLOR"])
        await ctx.send(embed = emb)



@client.command()
async def rps(ctx, member: discord.Member):     #Rock Paper Scissors
    emb = discord.Embed(title = "Offer to play Rock Paper Scissors!", color = config.config["DEFAULTCOLOR"])
    emb.add_field(name = "Yes: ✅", value = "No: ❌")
    message = await ctx.send(f"<@{member.id}>", embed = emb)
    await message.add_reaction("✅")
    await message.add_reaction("❌")

    reaction_vib = ["✅", "❌"]

    yes = "✅"
    no = "❌"

    def check(reaction, user):
        return user == member and str(reaction.emoji) in reaction_vib

    def checkx(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reaction_vib

    reaction, user = await client.wait_for('reaction_add', timeout = 15.0, check = check)  #setting the time for the reaction

    if str(reaction.emoji) == yes:
        emb = discord.Embed(title = "The game is starting, please check your private messages", color = config.config["GREENCOLOR"])
        servermessage = await ctx.send(embed = emb)

        player1 = 0
        player2 = 0
        round = 1
        game = True

        reaction_vib = ["🪨", "📄", "✂"]

        while (game == True):   #Game cycle
            emb = discord.Embed(title = "Wait until your opponent comes down", color = config.config["DEFAULTCOLOR"])
            await member.send(embed = emb)

            emb = discord.Embed(title = f"Round: {round} | {player1} : {player2}", color = config.config["DEFAULTCOLOR"])
            emb.add_field(name = "Please click on one of the reactions below", value = """:rock: - Rock
:page_facing_up: - Paper
:scissors: - Scissors
5 seconds per turn""")
            message = await ctx.author.send(embed = emb)
            await message.add_reaction("🪨")
            await message.add_reaction("📄")
            await message.add_reaction("✂")

            reaction_vib = ["🪨", "📄", "✂"]
            rock = "🪨"
            paper = "📄"
            scissors = "✂"

            reaction, user = await client.wait_for('reaction_add', timeout = 5.0, check = checkx)
            if str(reaction.emoji) == rock:     #Choosing the first player
                player1emoji = "🪨"
            elif str(reaction.emoji) == paper:
                player1emoji = "📄"
            elif str(reaction.emoji) == scissors:
                player1emoji = "✂"

            emb = discord.Embed(title = "Wait until your opponent comes down", color = config.config["DEFAULTCOLOR"])
            await ctx.author.send(embed = emb)

            emb = discord.Embed(title = f"Round: {round} | {player2} : {player1}", color = config.config["DEFAULTCOLOR"])
            emb.add_field(name = "Please click on one of the reactions below", value = """:rock: - Rock
:page_facing_up: - Paper
:scissors: - Scissors
5 seconds per turn""")
            message = await member.send(embed = emb)
            await message.add_reaction("🪨")
            await message.add_reaction("📄")
            await message.add_reaction("✂")

            reaction, user = await client.wait_for('reaction_add', timeout = 5.0, check = check)
            if str(reaction.emoji) == rock:     #The choice of the second player
                player2emoji = "🪨"
            elif str(reaction.emoji) == paper:
                player2emoji = "📄"
            elif str(reaction.emoji) == scissors:
                player2emoji = "✂"

            if(player1emoji == player2emoji):   #Round results
                emb = discord.Embed(title = "Draw in the round", color = config.config["DEFAULTCOLOR"])
                emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                await ctx.author.send(embed = emb)
                await member.send(embed = emb)
                emb = discord.Embed(title = "Game result", color = config.config["DEFAULTCOLOR"])
                emb.add_field(name = f"Round: {round}", value = f"{player1} <@{ctx.author.id}> {player1emoji} VS {player2emoji} <@{member.id}> {player2}")
                await servermessage.edit(embed = emb)
            elif(player1emoji == "🪨"):
                if(player2emoji == "✂"):
                    emb = discord.Embed(title = "You won this round!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                    await ctx.author.send(embed = emb)
                    emb = discord.Embed(title = "You've lost this round", color = config.config["REDCOLOR"])
                    emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                    await member.send(embed = emb)
                    player1 = player1 + 1
                elif(player2emoji == "📄"):
                    emb = discord.Embed(title = "You've lost this round", color = config.config["REDCOLOR"])
                    emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                    await ctx.author.send(embed = emb)
                    emb = discord.Embed(title = "You won this round!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                    await member.send(embed = emb)
                    player2 = player2 + 1
                emb = discord.Embed(title = "Game result", color = config.config["DEFAULTCOLOR"])
                emb.add_field(name = f"Round: {round}", value = f"{player1} <@{ctx.author.id}> {player1emoji} VS {player2emoji} <@{member.id}> {player2}")
                await servermessage.edit(embed = emb)
            elif(player1emoji == "📄"):
                if(player2emoji == "🪨"):
                    emb = discord.Embed(title = "You won this round!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                    await ctx.author.send(embed = emb)
                    emb = discord.Embed(title = "You've lost this round", color = config.config["REDCOLOR"])
                    emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                    await member.send(embed = emb)
                    player1 = player1 + 1
                elif (player2emoji == "✂"):
                    emb = discord.Embed(title = "You've lost this round", color = config.config["REDCOLOR"])
                    emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                    await ctx.author.send(embed = emb)
                    emb = discord.Embed(title = "You won this round!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                    await member.send(embed = emb)
                    player2 = player2 + 1
                emb = discord.Embed(title = "Game result", color = config.config["DEFAULTCOLOR"])
                emb.add_field(name = f"Round: {round}", value = f"{player1} <@{ctx.author.id}> {player1emoji} VS {player2emoji} <@{member.id}> {player2}")
                await servermessage.edit(embed = emb)
            elif (player1emoji == "✂"):
                if (player2emoji == "📄"):
                    emb = discord.Embed(title = "You won this round!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                    await ctx.author.send(embed = emb)
                    emb = discord.Embed(title = "You've lost this round", color = config.config["REDCOLOR"])
                    emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                    await member.send(embed = emb)
                    player1 = player1 + 1
                elif (player2emoji == "🪨"):
                    emb = discord.Embed(title = "You've lost this round", color = config.config["REDCOLOR"])
                    emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                    await ctx.author.send(embed = emb)
                    emb = discord.Embed(title = "You won this round!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Round result", value = f"You {player1emoji} VS {player2emoji} Opponent")
                    await member.send(embed = emb)
                    player2 = player2 + 1
                emb = discord.Embed(title = "Game result", color = config.config["DEFAULTCOLOR"])
                emb.add_field(name = f"Round: {round}", value = f"{player1} <@{ctx.author.id}> {player1emoji} VS {player2emoji} <@{member.id}> {player2}")
                await servermessage.edit(embed = emb)

            if(player1 == 3 or player2 == 3 or round == 10):    #End-of-game check
                game = False
                if(player1 == 3):
                    emb = discord.Embed(title = "You've won this game!", color = config.config["GREENCOLOR"])
                    await ctx.author.send(embed = emb)
                    emb = discord.Embed(title = "You lost in this game", color = config.config["REDCOLOR"])
                    await member.send(embed = emb)
                    emb = discord.Embed(title = "The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner:", value = f"<@{ctx.author.id}>")
                    await servermessage.edit(content = f"<@{ctx.author.id}> <@{member.id}>")
                    await servermessage.edit(embed = emb)
                elif(player2 == 3):
                    emb = discord.Embed(title = "You lost in this game", color = config.config["REDCOLOR"])
                    await ctx.author.send(embed = emb)
                    emb = discord.Embed(title = "You've won this game!", color = config.config["GREENCOLOR"])
                    await member.send(embed = emb)
                    emb = discord.Embed(title = "The game is over!", color = config.config["GREENCOLOR"])
                    emb.add_field(name = "Winner:", value = f"<@{member.id}>")
                    await servermessage.edit(content = f"<@{ctx.author.id}> <@{member.id}>")
                    await servermessage.edit(embed = emb)
                elif(round == 10):
                    if(player1 == player2):
                        emb = discord.Embed(title = "This game ended in a draw!", color = config.config["DEFAULTCOLOR"])
                        await ctx.author.send(embed = emb)
                        await member.send(embed = emb)
                        await servermessage.edit(content = f"<@{ctx.author.id}> <@{member.id}>")
                        await servermessage.edit(embed = emb)
                    elif(player1 > player2):
                        emb = discord.Embed(title = "You've won this game!", color = config.config["GREENCOLOR"])
                        await ctx.author.send(embed = emb)
                        emb = discord.Embed(title = "You lost in this game", color = config.config["REDCOLOR"])
                        await member.send(embed = emb)
                        emb = discord.Embed(title = "The game is over!", color = config.config["GREENCOLOR"])
                        emb.add_field(name = "Winner:", value = f"<@{ctx.author.id}>")
                        await servermessage.edit(content = f"<@{ctx.author.id}> <@{member.id}>")
                        await servermessage.edit(embed = emb)
                    elif(player1 < player2):
                        emb = discord.Embed(title = "You lost in this game", color = config.config["REDCOLOR"])
                        await ctx.author.send(embed = emb)
                        emb = discord.Embed(title = "You've won this game!", color = config.config["GREENCOLOR"])
                        await member.send(embed = emb)
                        emb = discord.Embed(title = "The game is over!", color = config.config["GREENCOLOR"])
                        emb.add_field(name = "Winner:", value = f"<@{member.id}>")
                        await servermessage.edit(content = f"<@{ctx.author.id}> <@{member.id}>")
                        await servermessage.edit(embed = emb)
            else:
                round = round + 1
    elif str(reaction.emoji) == no:
        emb = discord.Embed(title = "Game canceled!", color = config.config["REDCOLOR"])
        await ctx.send(embed = emb)


@rps.error
async def rps_error(ctx, error):    #Rock Paper Scissors error handling
    if isinstance(error, commands.MissingRequiredArgument):
        emb = discord.Embed(title = "Missing mention!", color = config.config["REDCOLOR"])
        await ctx.send(embed = emb)
    elif isinstance(error, commands.CommandInvokeError):
        emb = discord.Embed(title = "Response waiting time is out!", color = config.config["REDCOLOR"])
        await ctx.send(embed = emb)



@client.command()
async def slot(ctx):    #Slots
    emoji = ["7️⃣", "🍋", "🍒", "🍎", "🍉", "🍓", "🍌"]
    emoji1 = emoji[random.randint(1, len(emoji)) - 1]
    emoji2 = emoji[random.randint(1, len(emoji)) - 1]
    emoji3 = emoji[random.randint(1, len(emoji)) - 1]
    if(emoji1 == emoji2 and emoji1 == emoji3):
        emb = discord.Embed(title = f"{emoji1} | {emoji2} | {emoji3}", color = config.config["GREENCOLOR"])
    elif(emoji1 != emoji2 and emoji1 != emoji3 and emoji2 != emoji3):
        emb = discord.Embed(title = f"{emoji1} | {emoji2} | {emoji3}", color = config.config["REDCOLOR"])
    else:
        emb = discord.Embed(title = f"{emoji1} | {emoji2} | {emoji3}", color = config.config["DEFAULTCOLOR"])
    await ctx.send(embed = emb)



@client.command()
async def coin(ctx):    #Coin flip
    emb = discord.Embed(title = "Choose a side", color = config.config["DEFAULTCOLOR"])
    emb.add_field(name = "😉 - Heads", value = "🦎 - Tails")
    emb.set_footer(text = "5 seconds per turn")
    message = await ctx.send(embed = emb)
    await message.add_reaction("😉")
    await message.add_reaction("🦎")

    reaction_vib = ["😉", "🦎"]

    heads = "😉"
    tails = "🦎"

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reaction_vib

    reaction, user = await client.wait_for('reaction_add', timeout = 5.0, check = check)    #setting the time for the reaction

    if str(reaction.emoji) == heads:
        userside = "😉 Heads"
        side = 1
    elif str(reaction.emoji) == tails:
        userside = "🦎 Tails"
        side = 2

    if(side == random.randint(1,2)):
        emb = discord.Embed(title = "Game result", color = config.config["GREENCOLOR"])
        emb.add_field(name = f"Your side: {userside}", value = f"Coin side: {userside}")
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title = "Game result", color = config.config["REDCOLOR"])
        if(side == 1):
            emb.add_field(name = f"Your side: {userside}", value = f"Coin side: 🦎 Tails")
        else:
            emb.add_field(name = f"Your side: {userside}", value = f"Coin side: 😉 Heads")
        await ctx.send(embed = emb)


@coin.error
async def coin_error(ctx, error):   #Coin flip error handling
    if isinstance(error, commands.CommandInvokeError):
        emb = discord.Embed(title = "Response waiting time is out!", color = config.config["REDCOLOR"])
        await ctx.send(embed = emb)



@client.command()
async def roulette(ctx):    #Roulette
    emb = discord.Embed(title = "Choose a color", color = config.config["DEFAULTCOLOR"])
    message = await ctx.send(embed = emb)

    await message.add_reaction("🟥")
    await message.add_reaction("⬛")
    await message.add_reaction("🟩")

    reaction_vib = ["🟥", "⬛", "🟩"]

    red = "🟥"
    black = "⬛"
    green = "🟩"

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reaction_vib

    reaction, user = await client.wait_for('reaction_add', timeout = 5.0, check = check)    #setting the time for the reaction

    if str(reaction.emoji) == red:
        usercolor = "🟥 Red"
    elif str(reaction.emoji) == black:
        usercolor = "⬛ Black"
    elif str(reaction.emoji) == green:
        usercolor = "🟩 Green"

    rednumber = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    blacknumber = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    generate = random.randint(1, 37)

    if(generate == 37):
        color = "🟩 Green"
    elif(generate in rednumber):
        color = "🟥 Red"
    elif(generate in blacknumber):
        color = "⬛ Black"

    if(usercolor == color):
        emb = discord.Embed(title = "Game result", color = config.config["GREENCOLOR"])
        emb.add_field(name = f"Your color: {usercolor}", value = f"Dropped color: {color}")
    else:
        emb = discord.Embed(title = "Game result", color = config.config["REDCOLOR"])
        emb.add_field(name = f"Your color: {usercolor}", value = f"Dropped color: {color}")
    await ctx.send(embed = emb)


@roulette.error
async def roulette_error(ctx, error):   #Roulette error handling
    if isinstance(error, commands.CommandInvokeError):
        emb = discord.Embed(title = "Response waiting time is out!", color = config.config["REDCOLOR"])
        await ctx.send(embed = emb)



client.run(config.config["TOKEN"])
