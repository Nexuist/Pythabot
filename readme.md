#Pythabot v3.6
###IRC Framework for Bots

Setting Up
==========
Make sure you have Python 2.7.2 installed. You may also have other python versions but 2.7.2 is the one Pythabot was 
developed and tested on. To begin, create a new .py file in the same directory as Pythabot.py and write the following:

```python
#!/usr/bin/env python

import pythabot
```

Configuration
=============
Pythabot's way of configuration is a dictionary which is passed on to the main class when created. 
This dictionary is called "config" and contains configuration details:

```python
config = {\
    "host":"", # the IRC server to connect to
    "port":6667, # the port of the host to connect to
    "nick":"", # bot's nickname, can be anything as long as it is not registered
    "ident":"", # bot's client, e.g. Pythabot, can be anything
    "realname":"", # can be anything
    "pass":"", # the password, if the bot is registered
    "chans":[""], # the channels to join when started up
    "admins":[""], # masks who have access to admin commands
    "ownermask":"", # your mask - complete control over bot
    "prefix":"^", # what to say when you want to contact your bot 
    "quitmsg":"" # bot's quit message when leaving
    }
```


Getting up and running
======================
In your python file, add the following code:

```python
bot = pythabot.Pythabot(config)
bot.connect()
bot.listen()
```

This creates a new Pythabot class, tells it to connect to the host you gave it, and then start listening for commands.
There's only one problem: there are no commands yet. Here's a diagram of how commands work:

1. Create the command function
2. Call the addCommand function
3. Initialize the bot with the code above

###Create the command function

```python
def hi(parseinfo):
	bot.privmsg(parseinfo["chan"],"Hi!")
```

Privmsg is a function declared in the bot framework: it makes the bot say something in a specific channel.
To find out which channel someone said  "hi" in, we use parseinfo. More about parseinfo is located in the wiki.

```python
bot = pythabot.Pythabot(config)
bot.addCommand("hi",hi,"all",1)
bot.connect()
bot.listen()
```

###Call the addCommand function
Here's how addCommand works:

```python
bot.addCommand(text,function,permission,length)
```

Where text is what is needed to be spoken - "hi" in our case,
function is the function to be executed - hi in our case,
permission is the permission such as all,
and length is how long the string needs to be.

Remember when we made the hi function earlier? This
is where it comes into play. Using addCommand basically
added a trigger: Whenever anyone says "hi", the hi
function gets executed.


Permissions
===========
Permissions are what define user groups for
the bot. There are 3 user groups:

	* Owner
	* Admin
	* All 
 
Owner, in this case, would be you. You would basically want yourself to have access to all commands. 
You can decide admins with judgement. Of course, you control the commands, so you don't need to give
any commands to admins if you so choose.

You can make somebody an admin by adding them to the admin
list. Here's some code that shows how do do that:

```python
def admin(parseinfo):
    bot.config["admins"].append(parseinfo["args"][1])
```

...and in the bot initialization section:

```python
bot.addCommand("admin",admin,"admins",2)
```

Whenever an admin calls this admin command, the nick defined after
the command will become an admin. For example:

^admin joey

In this case, the nick joey will become an admin and be 
able to use admin commands.


String lengths
==============
Before being processed, strings are split into
pieces. Pythabot has to make sure you supply enough
arguments to a command to prevent it from crashing.
If you use the ^admin command from before without
giving it a name, it will add nothing to the admin list.
It will also error, because no piece will exist that
contains the name. There will always be at least 1 piece
in the string. If you have a function - for example,
an op function - that requires a name, then use 2 for
the string length. Otherwise, you might be oping nothing
and causing the bot to crash. If you have a kick command
that needs a name and a reason, use 3. (Remember: there
will be one extra because the command name itself counts.)


Parse info
==========
So you've made a few commands, set up your bot,
added triggers with proper string lengths and such. 
Now what? Well, there's a lot more. Each command gets
passed a dictionary - yep, another one! - which contains
information gatherered from the string. Here's the
specification:

sender - The sender's nick, ex. "techboy6601"
ident - The sender's IDENT, ex. "IceChat77"
mask - The sender's mask, ex. "1.33.7.0@lol.net"
chan - The channel the message was sent from, ex. "#botters"
msg - The message, ex. "hi lol"
firstarg - The first argument, ex. "hi"
args - A list containing the message split into pieces, ex. 
["hi","lol"]

You can use these to your advantage to get the most out of
your bot!


Next steps
==========
With the ability to use Python, you can make your bot do anything!
This includes shutting off your computer, running shell commands,
sending mail, and anything else that is possible with Python.

Also keep in mind that Pythabot is completely open-source. Feel free to modify
it, but please give me (Techboy6601) credit.


Happy bot building!

- Techboy6601



