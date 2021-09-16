async def run(discord, client, message, args, qik, admin_role, embed_colors):
  
  # Functions
  async def embedsend(discord_embed):
    await message.channel.send(embed = discord_embed);
  
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

  def has_mention(arg):
    if arg.startswith("<@!") and len(arg) == 22:
      return True;
    else:
      return False;

  # Main command code
  if _hasr_(admin_role):
    if has_mention(args[0]):
      if str.isnumeric(args[1]) and bool(args[2]):
        ment_user = _pment_(args[0]);
        current_roles = [];

        def get_roles(mention: discord.Member):
          for role in mention.roles:
            current_roles.append(role);
              
            qik.set(f"roles.{ment_user}", current_roles);

        async def remove_roles(mention: discord.Member):
          for role in mention.roles:
            await client.remove_roles(mention, role);
    else:
      invalid_arg_sig_embed = discord.Embed(title = "*invalid args signature:*", description = "*invalid arg signature:  `arg1 == user value`\nproper use:  `!mute <@user (arg1)> <reason (arg2)>`*", color = embed_colors["err"]);

      embedsend(invalid_arg_sig_embed);
  else:
    invalid_perms_embed = discord.Embed(title = "*invalid permissions:*", description = "*invalid permissions:  `message.author != guild.admin*", color = embed_colors["err"]);

    embedsend(invalid_perms_embed);
