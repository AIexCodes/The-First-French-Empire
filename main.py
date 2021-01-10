import discord
import datetime
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(
        type=discord.ActivityType.watching, name="The First French Emprie"
    ))
    print("Viva La France")


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)
    await ctx.message.channel.send("Messages purged.")

@client.event
async def on_member_join(member):
    embed = discord.Embed(colour=0x95efcc, description=f"Welcome to the French Empire! You are the {len(list(member.guild.members))}rd/th/nd member!")
    embed.set_thumbnail(url=f"{member.guild.icon_url}")
    embed.set_author(name=f"{member.name}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    channel = client.get_channel(id=797853274484113418)

    await channel.send(embed=embed)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason="No reason provided"):
    await member.send("You have been kicked from the French Empire, Because:"+reason)
    await member.kick(reason=reason)
    await ctx.message.channel.send("Use has been kicked.")

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason="No reason provided"):
    await member.send("You have been banned from the French Empire, Because:"+reason)
    await member.ban(reason=reason)
    await ctx.message.channel.send("Use has been banned.")

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx, user: discord.Object):
    await ctx.guild.unban(user)
    await ctx.send(f"Unbanned user with id {user.id}")

@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(797896541871538218)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " has been muted")

@client.command(aliases=['um'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(797896541871538218)

    await member.remove_roles(muted_role)

    await ctx.send(member.mention + " has been unmuted")

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Users name:", value=member.display_name)

    embed.add_field(name="Account Created at:", value=member.created_at.strftime("%a, %d, %B, %I:%M %p UTC"))
    embed.add_field(name="Server Joined at:", value=member.joined_at.strftime("%a, %d, %B, %I:%M %p UTC"))

    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embed)


client.run("Nzk3ODM5ODQ5OTM5Nzk1OTg4.X_sUQw.1N5FfCJikxnc1ajdHSAhlhCpwSw")