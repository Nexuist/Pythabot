Pythabot v3.6
IRC Framework for Bots
Instruction Manual

Setting up
==========
Make sure you have Python 2.7.2 installed. You may also have other python versions but 2.7.2 is the one Pythabot was developed and tested on. To begin, create a new .py file in the same directory as Pythabot.py and write the following:

-------------------------------------------------
#!/usr/bin/env python

import pythabot
-------------------------------------------------

Configuration
=============
Pythabot's way of configuration is a dictionary which is passed on to the main class when created. This dictionary is called "config" and contains configuration details:

--------------------------------------------------
config = {\
    "host":"", 
    "port":6667,
    "nick":"",
    "ident":"",
    "realname":"",
    "pass":"",
    "chans":[""],
    "admins":[""],
    "ownermask":"",
    "prefix":"^",
    "quitmsg":""
    }
--------------------------------------------------

Make sure you include the tabs. If you haven't 
noticed, Python is a completely tab-based language.
Anyways, lets go over this. What this code does is
make a dictionary called config. A dictionary is
a special term in Python that refers to a gathering
of key:pair values. For example: if you were to
call config["host"], you would get the value of host,
which right now is empty. Let's fix that up. In the 
quotes, type in the host address (ex. irc.freenode.n-
et). You won't need to change the port unless it is
some special type of IRC server. Make nick the bot's
nick (ex. pythabot). Ident can be anything you'd like,
such as "Pythabot" or "bot". Realname can also be an-
ything you want. Pass, however, cannot. Make sure you
register your bot before running it! If you have, pass
should be the password you used to register your bot's
nick. Chans is a list of channels you want the bot to
join when it connects to the server (ex. ["#lol","#b-
otters-test"]). Admins is a list of nicks that you
want to hand administrator privileges to. Put them in
the same way as you did the chans. Finally, ownermask
is your hostmask. When doing owner commands Pythabot
checks for the mask instead of the nick. This is so
someone cannot just /nick and instantly gain owner
privileges. Prefix is what you'll start commands 
with (ex. "^","."). It can be as long as you like.
Quitmsg is the message you want to display
when the bot quits. This can be anything you'd like.


Getting up and running
======================
	In your python file, add the following code:

-----------------------------------------------------
bot = pythabot.Pythabot(config)
bot.connect()
bot.listen()
-----------------------------------------------------

What does this do? Simple, really - first, we make a
starter bot in the first line, and then we customize 
it with the config dictionary you made before. Then,
we connect to the server with the connect() command,
and finally, we start the main loop that listens for
commands and executes them. But wait! We're not done 
yet! We still haven't added commands. Lets add a 'hi'
command: Whenever somebody says hi to the bot, we 
say hi back!

------------------------------------------------------
def hi(parseinfo):
	bot.privmsg(parseinfo["chan"],"Hi!")
------------------------------------------------------


Def declares a function. If you looked over the source,
you would see privmsg sends a message to a specific ch-
annel. The other way of interacting with the server thr-
ough this is with the sendraw command, which sends a 
raw message to the server. But enough of that - let's
make our command get parsed! To do that, we use the 
addcommand command. Lets modify our code.

------------------------------------------------------
bot = pythabot.Pythabot(config)
bot.addcommand("hi",hi,"all",1)
bot.connect()
bot.listen()
------------------------------------------------------

The addcommand command works like this:

bot.addcommand(text,function,permission,length)

Where text is what is needed to be spoken e.g. "hi",
function is the function to be executed e.g. hi,
permission is the permission e.g. all,
and length is how long the string needs to be.

Remember when we made the hi function earlier? This
is where it comes into play. The addcommand basically
added a trigger: Whenever anyone says "hi", the hi
function gets executed. It doesn't have to be "hi",
though - it works with "bye","die","lol" or anything
else. Lets go over permissions in more details.


Permissions
===========
	Permissions are what define user groups for
the bot. There are 3 user groups:

	+ Owner - This is only one person who can
control the bot to its fullest potential
	+ Admin - A group of people who can use
most of the bot's commands
	+ All - Everybody, from guests to bots to
ops.

You can make somebody by adding them to the admin
list. Here's code that shows that:

--------------------------------------------------------
def admin(parseinfo):
    bot.config["admins"].append(parseinfo["args"][1])
--------------------------------------------------------
...in the bot initialization section:
--------------------------------------------------------
bot.addcommand("admin",admin,"admins",2)
--------------------------------------------------------

Whenever an admin calls the admin command, the word after
admin will become an admin. For example:

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
	You've made your bot. You have customized every aspect
of it and made custom commands for it. Your commands harness
the power of parseinfo and you are generally satisfied with 
you bot. Not there yet? There's hope still! In this folder,
open example.py. It contains some example code that you
can build off of.


Happy bot building!

- Techboy6601



