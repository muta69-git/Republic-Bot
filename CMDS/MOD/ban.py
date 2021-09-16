async def run(discord, client, message, args, embed_colors, admin_role):
  # Functions
  async def embedsend(discord_embed):
    await message.channel.send(embed = discord_embed);

  def _hasr_(name):
    for x in message.author.roles:
      if x.name == name:
        return True;
    return False;

  def _pment_(mention):
    for i in mention:
      if str.isnumeric(i):
        pass;
      else:
        mention = mention.replace(i, "")
  
  def has_mention(arg):
    if arg.startswith("<@!") and len(arg) == 22:
      return True;
    else:
      return False;
  
  # Main command code
  if _hasr_(admin_role):
    if len(args) < 1:
      invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signature:*", description = "*`arg1 == user value`\nproper use:  `!ban <@user (arg1)>`*", color = embed_colors["err"]);

      await embedsend(invalid_arg_sig_embed);
    else:
      if has_mention(args[0]): 
        ment_user = _pment_(args[0]);
        given_reason = args[1:];
        try:
          banned_embed = discord.Embed(title = "*moderation:*", description = f"you have been banned from {message.guild.name} for: {given_reason}.", color = embed_colors["moderation"]);

          await client.send_message(ment_user, banned_embed);

          async def ban_user(ment_user: discord.Member):
            await ment_user.ban(reason = given_reason);

            ban_user(ment_user);

            banned_user_embed = discord.Embed(title = "*moderation:*", description = f"succesfully, banned {args[0]} for: {given_reason}", color = embed_colors["moderation"]);

            await embedsend(banned_user_embed);
        except:
          ban_error_embed = discord.Embed(title = "*unable to ban:*", description = f"*i was unable to ban mentioned user: {args[0]}, this could be due to having a higher role than me, or admin permissions.*", color = embed_colors["err"]);

          await embedsend(ban_error_embed);
  else:
    invalid_perms_embed = discord.Embed(title = "*invalid permissions:*", description = "*`message.author != guild.admin`\nproper use:  `!ban <@user (arg1)>`*", color = embed_colors["err"]);

    await embedsend(invalid_perms_embed);