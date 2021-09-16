  # general imports 
import discord;
import os;
from qikdb import DB;
from server import ping_server;
from ro_py import Client as cli;

from CMDS.HONOR.honor import run as honor_run;
from CMDS.HONOR.honor_add import run as honor_add_run;
from CMDS.HONOR.honor_del import run as honor_del_run;
from CMDS.HONOR.honor_set import run as honor_set_run; 
from CMDS.MISC.help import run as help_run;
from CMDS.MISC.restart import run as restart_run;
from CMDS.MISC.kill import run as kill_run;
from CMDS.MOD.mute import run as mute_run;
from CMDS.MOD.kick import run as kick_run;
from CMDS.MOD.ban import run as ban_run;

roco = os.environ['COOKIE'];
ro_cli = cli();

qik = DB(config = {
  "name": "database",
  "directory": "DB",
  "path": 'database'
});

client = discord.Client();

@client.event 
async def on_ready():
  os.system("clear");
  print('logged in as {0.user}'.format(client));
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="myself doing ur mom"));

@client.event
async def on_message(message):
  if message.author == client.user:
    return;

  if not qik.exists(f'honor.{message.author.id}'):
    qik.set(f'honor.{message.author.id}', 0);
  honor = qik.get(f'honor.{message.author.id}');

  # Essential variables
  pfx = os.environ["PREFIX"];
  msg = message.content;
  args = msg.split(" ");
  admin_role = "allah";
  command = args[0].replace(pfx, ""); args.pop(0);
  chansend = lambda string: message.channel.send(string);
  #dpy = DPY(pfx, message, client); #Not needed for now, trynna fix still.
  embed_colors = {"err": discord.Color.from_rgb(255, 144, 97), "info": discord.Color.from_rgb(255, 255, 255), "honor": {"view": discord.Color.from_rgb(247, 199, 54), "modified": discord.Color.from_rgb(92, 250, 75)}, "moderation": discord.Color.from_rgb(4, 19, 191)};

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

  def get_rank(user_id):
    return "Placeholder"; #placeholder until ranks and rank xp is made.

  if msg.startswith(pfx): 
    
    # Help command #
    if command == "help":
      help_run(discord, message, args, qik, embed_colors);
      

     
    # Honor command #
    elif command == "honor":
      honor_run(discord, message, args, qik, embed_colors);

    # Honor add command #
    elif command == "honor.add":
      honor_add_run(discord, message, args, qik, embed_colors, admin_role);

    # Honor remove command #
    elif command == "honor.del":
     honor_del_run(discord,message, args, admin_role, embed_colors, qik);

    # Honor set command #
    elif command == "honor.set":
      honor_set_run(discord, message, args, embed_colors, admin_role, qik);

    # Ban command #
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
              kicked_embed = discord.Embed(title = "*moderation:*", description = f"you have been kicked from {message.guild.name} for: {given_reason}.", color = embed_colors["moderation"]);

              await client.send_message(ment_user, kicked_embed);
              
              async def kick_user(ment_user: discord.Member):
                await ment_user.kick(reason = given_reason);
              
              kick_user(ment_user);

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
            given_reason = args[1:];

            warned_embed = discord.Embed(title = "*moderation:*", description = f"you have been warned in {message.guild.name} for {given_reason}.", color = embed_colors["moderation"]);

            client.send_message(ment_user, warned_embed);
            
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

        embedsend(invalid_perms_embed);

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
        
    elif command == "mute": # Work In Progress.
      mute_run(discord, client, message, args, qik, admin_role, embed_colors);
  
    elif command == "close" or command == "logout" or command == "kill":
      kill_run(message, client);
    
    elif command == "restart":
      restart_run(discord, message);
      
        




    else: # Acts as a default if no command found.
      command_not_found_embed = discord.Embed(title = "*invalid command:*", description = f"*`{pfx}{command}`is not a command please use {pfx}help for the list of commands.");

      embedsend(command_not_found_embed);
  else:
    return;
    
ping_server();
client.run(os.environ['TOKEN']);