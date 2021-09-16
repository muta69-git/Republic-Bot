import os;

pfx = os.environ["PREFIX"];

bot_commands = [
  {"name": f"{pfx}honor", 
  "aliases": "honor", 
  "alias_params": ["<@user>"], 
  "description": "will return requested user\'s honor.",
  "file_name": "honor.py"
  },
  {"name": f"{pfx}honor.add <@user> <int>", 
  "description": "will add honor to requested user.",
  "file_name": "honor.add.py"
  },
  {"name": f"{pfx}honor.del <@user> <int>", 
  "description": "will remove honor from requested user.",
  "file_name": "honor.del.py"
  },
  {"name": f"{pfx}honor.set <@user> <int>", 
  "description": "will set the honor of requested user."
  },
  {"name": f"{pfx}kick <@user>", 
  "description": "will kick the mentioned user.",
  "file_name": "kick.py"
  },
  {"name": f"{pfx}ban <@user>", 
  "description": "will ban the mentioned user.",
  "file_name": "ban.py"
  }
];