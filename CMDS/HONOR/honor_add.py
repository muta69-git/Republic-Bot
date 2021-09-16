async def run(discord, message, args, qik, embed_colors, admin_role):
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
        mention = mention.replace(i, "");

  def _hasr_(name):
    for x in message.author.roles:
      if x.name == name:
        return True;
    return False;

  # Main command code
  if _hasr_(admin_role):
    if len(args) <= 1:
      invalid_arg_index_embed = discord.Embed(title = "*invalid args index:*", description = f"*`provided args: {len(args)}`\nproper use:  `!honor.add <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]);

      await embedsend(invalid_arg_index_embed);
    else:
      if has_mention(args[0]):
        ment_user = _pment_(args[0]);
        if str.isnumeric(args[1]):
          honor_sum = int(args[1]);
          if not qik.exists(f'honor.{ment_user}'):
            invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signatures:*", description = "*invalid arg signatures:  `arg1 == user value, arg2 == int value`\nproper use:  `!honor.add <@user (arg1)> <int (arg2)>`\nuser may also not be in database*", color = embed_colors["err"]);

            await embedsend(invalid_arg_sig_embed);
          else:
            honor = qik.add(f'honor.{ment_user}',  honor_sum);

            honor_added_embed = discord.Embed(title = "*added honor:*", description = f"*<@!{message.author.id}> has added {honor_sum} honor to <@!{ment_user}>.\nthey now have {honor} honor.*", color = embed_colors["honor"]["modified"]);

            await embedsend(honor_added_embed);
        else:
          invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signature:*", description = "*`arg2 == int value`\nproper use:  `!honor.add <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]); 

          await embedsend(invalid_arg_sig_embed);
      else:
        if not has_mention(args[0]) and not str.isnumeric(args[1]):
          invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signatures:*", description = "*`arg1 == user value, arg2 == int value`\nproper use:  `!honor.add <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]);

          await embedsend(invalid_arg_sig_embed);
        elif not has_mention(args[0]):
          invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signature:*", description = "*`arg1 == user value`\nproper use:  `!honor.add <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]);

          await embedsend(invalid_arg_sig_embed);
        else:
          invalid_perms_embed = discord.Embed(title = "*invalid permissions:*", description = "*`message.author != guild.admin`\nproper use:  `!honor.add <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]);

          await embedsend(invalid_perms_embed);