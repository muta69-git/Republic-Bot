# Imports
from datetime import datetime;
from commands import bot_commands;
# fucktion
async def run(discord, message, args, qik, embed_colors):
  # Variables
  now = datetime.now();
  current_time = now.strftime("%H:%M:%S");


  # Functions
  async def embedsend(discord_embed):
    await message.channel.send(embed = discord_embed);

  # Main command code
  if len(args) <= 0:
    help_embed = discord.Embed(title = "**CURRENT COMMMANDS**", color = embed_colors["info"]);

    for cmd in bot_commands:
      help_embed.add_field(name = cmd['name'], value = f"*{cmd['description']}*", inline = False);
          
      help_embed.set_footer(text = f'time sent: {current_time}');
      await embedsend(help_embed);
  elif len(args) > 0:
    for cmd in bot_commands:
      if hasattr(cmd, "aliases"):
        for alias in cmd:
          if alias == args[0]:
            cmd_params = "";
            cmd_aliases = "";

            for alias in cmd['aliases']:
              cmd_aliases = cmd_aliases + " " + alias;
              for param in cmd['params']:
                cmd_params = cmd_params + " " + param;

                help_embed = discord.Embed(title = f"**{alias.upper()}**", description = f"description: {cmd['description']}\n\naliases: {cmd_aliases}\n\nparams: {cmd_params}", color = embed_colors['info']);
                help_embed.set_footer(text = current_time);
                await embedsend(help_embed);
                return;
        command_not_found_embed = discord.Embed(title = "**ALIAS NOT FOUND**", description = f"**command not found**\n*entered alias \"{args[0]}\" not found.*", color = embed_colors['err']);
        await embedsend(command_not_found_embed)