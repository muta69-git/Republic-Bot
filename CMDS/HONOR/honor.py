async def run(discord, message, args, qik, embed_colors):
  # Functions
  async def embedsend(discord_embed):
    await message.channel.send(embed = discord_embed);

  def get_rank(user):
    return "Placeholder";
  
  def has_mention(arg):
    if arg.startswith("<@!") and len(arg) == 22:
      return True;
    else:
      return False;
  
  def _pment_(mention):
    for i in mention:
      if str.isnumeric(i):
        pass;
      else:
        mention = mention.replace(i, "")

  # Main command code
  if len(args) <= 0:
    user = message.author;
    honor = qik.get(f'honor.{user.id}');

    honor_embed = discord.Embed(title = f"*<@!{user.id}>\'s honor:*", description = f"*Rank: `{get_rank(user)}`\n\nHonor: `{honor}`*", color = embed_colors["honor"]["view"]);

    await embedsend(honor_embed);
  elif has_mention(args[0]): 
    ment_user = _pment_(args[0]);
    if not qik.exists(f'honor.{ment_user}'):
      db_missing_embed = discord.Embed(title = "*invalid arg signature:*", description = "*`arg1 == user value`\nproper use:  `!honor`  or  `!honor <@user (arg1)>`\nuser may also not be in database*", color = embed_colors["err"]);

      await embedsend(db_missing_embed);
    else:
      honor = qik.get(f'honor.{ment_user}');

      honor_embed = discord.Embed(title = f"*{args[0]}\'s honor:*", description = f"*Rank: `{get_rank(ment_user)}`\n\nHonor: `{honor}`*", color = embed_colors["honor"]["view"]);

      await embedsend(honor_embed);
  else:
    invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signature:*", description = "*`arg1 == user value`\nproper use:  `!honor` or `!honor <@user (arg1)>`*", color = embed_colors["err"]);

    await embedsend(invalid_arg_sig_embed);