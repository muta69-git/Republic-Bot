# Imports
import sys;

def run(message, client):
  # Functions
  chansend = lambda string: message.channel.send(string);
  
  # Main command code
  if message.author.id == "512659924073840644":
    chansend("Going offline.");
    client.close();
    sys.exit("Kill switch activated.");
  else:
    return;