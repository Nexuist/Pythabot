## Story Time!


Oh how far we've come.

This was my very first major software project, started around March 2012. I had just turned 13, and had gotten addicted to Internet Relay Chat. So, naturally, I wrote software for it.

In this project I learned about networking: TCP/IP, sockets, protocols, etc. It was actually a very good learning experience.

As I reflect back on this four years later, I'm glad I went ahead and worked on it, despite most people telling me to use an established framework such as Twisted. If I had done so, I would have been able to accomplish my goal of building a bot framework, but I would not have the skills and knowledge I got from doing it by hand.

So go ahead and look at this project, but remember: A 13 year old wrote it, so don't expect greatness. :P  


### Dependencies

* [Python 2.7](https://www.python.org/downloads/)

### Wiki

I set up a wiki for this project explaining the basic concepts employed by this framework. You can browse it [here](https://github.com/Nexuist/Pythabot/wiki).

### License
From the original documentation below:
```
Also keep in mind that Pythabot is completely open-source. Feel free to modify
it, but please give me (Nexuist) credit.
```

As it turns out, 13 year olds don't make good lawyers. Here's some better legalese:

```
MIT License

Copyright (c) 2012 Andi Andreas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Original Documentation

This was the original README written in 2012. It is still here for historical purposes.

---

#Pythabot v3.7
###IRC Framework for Bots

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

Commands
========
Here's an overview of how commands work:

1. Create the command function
2. Call the addCommand function
3. Initialize the bot

###Create the command function

```python
def hi(parseinfo):
	bot.privmsg(parseinfo["chan"],"Hi!")
```

Privmsg is a function declared in the bot framework: it makes the bot say something in a specific channel.
To find out which channel someone said  "hi" in, we use the "chan" variable included in [parseinfo](https://github.com/Techboy6601/Pythabot/wiki/parseinfo)

```python
bot = pythabot.Pythabot(config)
bot.addCommand("hi",hi,"all",1)
bot.connect()
bot.listen()
```

###Call the addCommand function and initialize the bot
addCommand is a function which adds a command to the bot's command list, which tells it to listen for the command
and enables it to call your command function (the one you made earlier).

addCommand takes the following arguments:

```python
bot.addCommand(text,function,permission,length)
```

For more information on addCommand, visit its [Wiki page](https://github.com/Techboy6601/Pythabot/wiki/addcommand)

Using addCommand basically adds a trigger: Whenever anyone says "hi", the hi
function gets executed.


Permissions
===========
Permissions are what define user groups for
the bot. There are 3 user groups:

	* Owner
	* Admin
	* All

Which group a user is in is decided by their hostmask. If their hostmask is equal to the hostmask defined in ownermask (in the config dictionary),
then they belong to the Owner group (note only one person can be in this group.)

Similarly, if a person's hostmask is included in the admins list (also in the config dictionary), they will have access to admin commands
(which can be created and assigned by you). This group can contain any amount of people.

All signifies what it's called - everyone is included. This includes the owner, admins, other bots, and anything else.

Next Steps
==========
With the ability to use Python, you can make your bot do anything!
This includes shutting off your computer, running shell commands,
sending mail, and anything else that is possible with Python.

Also keep in mind that Pythabot is completely open-source. Feel free to modify
it, but please give me (Nexuist) credit.


Happy bot building!
