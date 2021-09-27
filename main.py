import discord;

# discord imports #

import discord.ext;
from discord.utils import get;
from discord.ext import commands, tasks;
from discord.ext.commands import has_permissions,  CheckFailure, check;

# general imports #
import os;
import json;
from node_py import static, cons, typeof, color, math, contains
from qikdb import DB;
from server import ping_server;
from ro_py import Client as cli;
from datetime import datetime;
from dpy import DPY;
from time import sleep;
now = datetime.now();

print("boot?")
password_ = input('pass: ')
if password_ == str(os.environ['password']):
  cons.log('OK')
  sleep(0.5)
  cons.clear()
if not password_ == str(os.environ['password']):
  cons.log('NO')
  sleep(0.5)
  cons.clear()
  exit("Incorrect boot password.")

current_time = now.strftime("%H:%M:%S");

roco = os.environ['COOKIE'];
client = discord.Client();

qik = DB(config = {
  "name": "database",
  "path": "database",
  "directory": "DB"
});

@client.event
async def on_ready():
  cons.log('LOADING: [----------] 000%');
  sleep(0.1)
  cons.clear()
  cons.log('LOADING: [#---------] 010%');
  sleep(0.1)
  cons.clear()
  cons.log('LOADING: [##--------] 020%');
  sleep(0.1)
  cons.clear()
  cons.log('LOADING: [###-------] 030%');
  sleep(0.1)
  cons.clear()
  cons.log('LOADING: [####------] 040%');
  sleep(0.1)
  cons.clear()
  cons.log('LOADING: [#####-----] 050%');
  sleep(0.1)
  cons.clear()
  cons.log('LOADING: [######----] 060%');
  sleep(0.1)
  cons.clear()
  cons.log('LOADING: [#######---] 070%');
  sleep(0.1)
  cons.clear()
  cons.log('LOADING: [########--] 080%');
  sleep(0.1)
  cons.clear()
  cons.log('LOADING: [#########-] 090%');
  sleep(0.1)
  cons.clear()
  cons.log('LOADING: [##########] 100%');
  sleep(0.1)
  cons.clear()
  cons.log('PROCESS COMPLETED')
  sleep(1)
  cons.clear()
  cons.log(f' > logged in as {client.user}');
  sleep(0.25)
  cons.log(f' - time started: {current_time}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return;

  if not qik.exists(f'honor.{message.author.id}'):
    qik.set(f'honor.{message.author.id}', 0);
  honor = qik.get(f'honor.{message.author.id}');

  # Essential variables
  pfx = "!";
  msg = message.content;
  args = msg.split(" ");
  admin_role = "allah";
  command = args[0].replace(pfx, ""); args.pop(0);

  #group_id = 0;
  #global group;
 # group = await roblox.get_group(group_id);
  chansend = lambda string: message.channel.send(string)

  embedsend = lambda discord_embed: message.channel.send(embed = discord_embed)

  #dpy = DPY(pfx, message, client);

  embed_colors = {
    "err": discord.Color.from_rgb(252, 62, 28), 
    "info": discord.Color.from_rgb(255, 255, 255), "honor": {
      "view": discord.Color.from_rgb(247, 199, 54), "modified": discord.Color.from_rgb(92, 250, 75)
    }, 
    "moderation": discord.Color.from_rgb(4, 19, 191)
  };

  # Functions
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

  def get_rank(user_id):
    pass;

  if msg.startswith(pfx): 
    
      # ===== HELP COMMAND ============================================================== #
    if command == "help":
      help_embed = discord.Embed(title = "**CURRENT COMMANDS**", color = embed_colors["info"]);

      help_embed.add_field(name = f"{pfx}honor or {pfx}honor <@user>", value = "*will return requested user\'s honor.*", inline = False);

      help_embed.add_field(name = f"{pfx}honor.add <@user> <int>", value = "*will add honor to requested user.*", inline = False);

      help_embed.add_field(name = f"{pfx}honor.del <@user> <int>", value = "*will remove honor from requested user.*");

      help_embed.add_field(name = f"{pfx}honor.set <@user> <int>", value = "*will set the honor of requested user*");

      help_embed.set_footer(text = f'time sent: {current_time}');
      
      await embedsend(help_embed);

      # ===== HONOR COMMAND ============================================================== #
    elif command == "honor":
      if len(args) <= 0:
        user = message.author;
        honor = qik.get(f'honor.{user.id}');

        honor_embed = discord.Embed(title = f"*<@!{user}>\'s honor:*", description = f"*Rank: `{get_rank(user)}`\n\nHonor: `{honor}`*", color = embed_colors["honor"]["view"]);

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

      # ===== HONOR ADDING COMMAND ======================================================= #
    elif command == "honor.add":
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

      # ===== HONOR REMOVE COMMAND ======================================================= #
    elif command == "honor.del":
      if _hasr_(admin_role):
        if len(args) <= 1:
          invalid_arg_index_embed = discord.Embed(title = "*invalid arg index:*", description = "*`provided args: {len(args)}`\nproper use:  `!honor.del <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]);

          await embedsend(invalid_arg_index_embed);
        else:
          if has_mention(args[0]): 
            ment_user = _pment_(args[0]);
            if str.isnumeric(args[1]):
              honor_sum = int(args[1]);
              if not qik.exists(f'honor.{ment_user}'):
                invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signatures:*", description = "*`arg1 == user value, arg2 == int value`\nproper use:  `!honor.del <@user (arg1)> <int (arg2)>`\nuser may also not be in database*", color = embed_colors["err"]);

                await embedsend(invalid_arg_sig_embed);
              else:
                honor = qik.subtract(f'honor.{ment_user}',  honor_sum);

                honor_subtracted_embed = discord.Embed(title = "*honor subtracted:*", description = f"<@!{message.author.id}> has removed {honor_sum} honor from <@!{ment_user}>.\nthey now have {honor} honor.*", color = embed_colors["honor"]["modified"]);

                await embedsend(honor_subtracted_embed);
            else: 
              invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signature:*", description = "*invalid arg signature:  `arg2 == int value`\nproper use:  `!honor.del <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]);

              await embedsend(invalid_arg_sig_embed);
          else:
            if not has_mention(args[0]) and not str.isnumeric(args[1]):
              invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signatures:*", description = "*`arg1 == user value, arg2 == int value`\nproper use:  `!honor.del <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]);

              await embedsend(invalid_arg_sig_embed);
            elif not has_mention(args[0]):
              invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signature:*", description = "*`arg1 == user value`\nproper use:  `!honor.del <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]);

              await embedsend(invalid_arg_sig_embed);
      else:
        invalid_perms_embed = discord.Embed(title = "*invalid permissions:*", description = "*`message.author != guild.admin`\nproper use:  `!honor.del <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]);

        await embedsend(invalid_perms_embed);

      # ===== HONOR SET COMMAND ========================================================== #
    elif command == "honor.set":
      if _hasr_(admin_role):
        if len(args) < 1:
          invalid_arg_index_embed = discord.Embed(title = "*invalid arg index:*", description = "*`provided args: {len(args)}`\nproper use:  `!honor.set <@user (arg1)> <int (arg2)>", color = embed_colors["err"]);
          
          await embedsend(invalid_arg_index_embed);
        else:
          if has_mention(args[0]): 
            ment_user = _pment_(args[0]);
            if str.isnumeric(args[1]):
              honor_sum = int(args[1]);
              if not qik.exists(f'honor.{ment_user}'):
                invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signatures:*", description = "*signatures:  `arg1 == user value, arg2 == int value`\nproper use:  `!honor.set <@user (arg1)> <int (arg2)>`\nuser may also not be in database*", color = embed_colors["err"]);

                await embedsend(invalid_arg_sig_embed);
              else:
                honor = qik.set(f'honor.{ment_user}',  honor_sum);

                honor_set_embed = discord.Embed(title = "*set honor:*", description = f"*<@!{message.author.id}> has set {honor_sum} honor to <@!{ment_user}>.\nthey now have {honor} honor.*", color = embed_colors["honor"]["modified"]);

                await embedsend(honor_set_embed);
            else: 
              invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signature:*", description = "*`arg2 == int value`\nproper use:  `!honor.set <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]);

              await embedsend(invalid_arg_sig_embed);
          else:
            if not has_mention(args[0]) and not str.isnumeric(args[1]):
              invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signatures:*", description = "*`arg1 == user value, arg2 == int value`\nproper use:  `!honor.set <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]);

              await embedsend(invalid_arg_sig_embed);
            elif not has_mention(args[0]):
              invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signature:*", description = "*`arg1 == user value`\nproper use:  `!honor.set <@user (arg1)> <int (arg2)>`*");

              await embedsend(invalid_arg_sig_embed);
      else:
        invalid_perms_embed = discord.Embed(title = "*invalid permissions:*", description = "`message.author != guild.admin`\nproper use:  `!honor.set <@user (arg1)> <int (arg2)>`*", color = embed_colors["err"]);

        await embedsend(invalid_perms_embed);

    elif command == "ban":
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
              
    elif command == "kick":
      if _hasr_(admin_role):
        if len(args) < 1:
          invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signature:*", description = "*`arg1 == user value`\nproper use:  `!ban <@user (arg1)>`*", color = embed_colors["err"]);

          await embedsend(invalid_arg_sig_embed);
        else:
          if has_mention(args[0]): 
            ment_user = _pment_(args[0]);
            given_reason = args[1:];
            try:
              
              async def kick_user(ment_user: discord.Member):
                await ment_user.kick(reason = given_reason);
              
              await kick_user(ment_user);

              kicked_user_embed = discord.Embed(title = "*moderation:*", description = f"succesfully, kicked {args[0]} for: {given_reason}", color = embed_colors["moderation"]);

              embedsend(kicked_user_embed);
            except:
              kick_error_embed = discord.Embed(title = "*unable to ban:*", description = f"*i was unable to kick mentioned user: {args[0]}, this could be due to having a higher role than me, or admin permissions.*", color = embed_colors["err"]);

              await embedsend(kick_error_embed);
      else:
        invalid_perms_embed = discord.Embed(title = "*invalid permissions:*", description = "*`message.author != guild.admin`\nproper use:  `!ban <@user (arg1)>`*", color = embed_colors["err"]);

        await embedsend(invalid_perms_embed);
    
      # I AM WORKING ON THE WARN AND WARNS COMMANDS
    elif command == "warn":
      if _hasr_(admin_role):
        if len(args) < 1:
          invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signature:*", description = "*`arg1 == user value`\nproper use:  `!warn <@user (arg1)> <reason (arg2)>`*", color = embed_colors["err"]);

          await embedsend(invalid_arg_sig_embed);
        else:
          if has_mention(args[0]):
            ment_user = _pment_(args[0]);
            given_reason = " ".join(args[1:]);

            warned_embed = discord.Embed(title = "*moderation:*", description = f"you have been warned in {message.guild.name} for {given_reason}.", color = embed_colors["moderation"]);

            message.author.send(ment_user, warned_embed);
            
            if not qik.exists(f'warns.{ment_user}'):
              qik.set(f'warns.{ment_user}', []);
            
            warns = qik.get(f"warns.{ment_user}");
            warning = {"moderator": message.author.id, "reason": given_reason};
            warns.append(warning);
            
            qik.set(f"warns.{ment_user}", warns);

            warned_user_embed = discord.Embed(title = "*moderation:*", description = f"<@!{ment_user}> has been warned for {warning.reason}", color = embed_colors["moderation"]);

            await embedsend(warned_user_embed);
          else:
            invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signature:*", description = "*`arg1 == user value`\nproper use:  `!warn <@user (arg1)> <reason (arg2)>`*", color = embed_colors["err"]);

            await embedsend(invalid_arg_sig_embed);
      else:
        invalid_perms_embed = discord.Embed(title = "*invalid permissions:*", description = "*`message.author != guild.admin`\nproper use:  `!warn <@user (arg1)> <reason (arg2)>`*", color = embed_colors["err"]);

        await embedsend(invalid_perms_embed);

    elif command == "warns":
      if _hasr_(admin_role):
        if len(args) < 1:
          warns = qik.get(f'warns.{message.author.id}');

          warnings_embed = discord.Embed(title = "*warnings:*", description = f"<@!{message.author.id}> has {len(warns)} warnings", color = embed_colors["info"])

          warning_num = 1;
          for warning in warns:
            warnings_embed.add_field(name = f"*warning {warning_num}:*", value = warning["reason"]);
            warning_num += 1;

          await embedsend(warnings_embed);
        else:
          if has_mention(args[0]):
            ment_user = _pment_(args[0]);
            if not qik.exists(f'warns.{ment_user}'):
              await chansend(f'<@!{ment_user}> has no warnings.');
            else:
              warns = qik.get(f'warns.{ment_user}');

              warnings_embed = discord.Embed(title = "*warnings:*", description = f"<@!{ment_user}> has {len(warns)} warnings", color = embed_colors["info"]);

              warning_num = 1;
              for warning in warns:
                warnings_embed.add_field(name = f"*warning {warning_num}:*", value = warning["reason"]);
                warning_num += 1;

              await embedsend(warnings_embed);
          else:
            invalid_arg_sig_embed = discord.Embed(title = "*invalid arg signature:*", description = "*`arg1 == user value`\nproper use:  `!warn <@user (arg1)>`*", color = embed_colors["err"]);

            await embedsend(invalid_arg_sig_embed);
      else:
        invalid_perms_embed = discord.Embed(title = "*invalid permissions:*", description = "*`message.author != guild.admin`\nproper use:  `!warns <@user (arg1)>`*", color = embed_colors["err"]);

        await embedsend(invalid_perms_embed);
        
    elif command == "test":
      get_rank(0);
    


    else: # Default
      command_not_found_embed = discord.Embed(title = "**COMMAND NOT FOUND:**", description = f"command - {pfx}{command}, not found.", color = embed_colors["err"]);
      embedsend(command_not_found_embed);
    
ping_server();
client.run(os.environ['TOKEN']);

