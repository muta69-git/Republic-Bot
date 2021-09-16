# Imports
import os;
import sys;

def run(discord, message):
  # Functions
  chansend = lambda string: message.channel.send(string);

  # Main command code
  if message.author.id == "512659924073840644":
    chansend("Restarting bot.");
    return os.execv("__main__", sys.argv);