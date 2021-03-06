#!/usr/bin/env python

#These commands were created to help with channel administration.
#It includes mode change, self OP, raw message, channel joins,
#parts, kicks, a prefix changer, and even a start timer!


import pythabot,time

def hi(parseinfo):
    bot.privmsg(parseinfo["chan"],"Hi, %s." % parseinfo["sender"])
    
def quit(parseinfo):
    bot.quit("Quit")

def mode(parseinfo):
    bot.sendraw("MODE %s %s %s" % (parseinfo["chan"],parseinfo["args"][1]," ".join(parseinfo["args"][2:])))

def selfop(parseinfo):
    bot.privmsg("chanserv","op %s %s" % (parseinfo["chan"],bot.config["nick"]))
    
def list(parseinfo):
    bot.privmsg(parseinfo["chan"],"Commands: " + ", ".join(bot.commandlist))
    bot.privmsg(parseinfo["chan"],"Channels I'm in: " + ", ".join(config["chans"]))
    bot.privmsg(parseinfo["chan"],"Admins: " + ", ".join(bot.config["admins"]))

def admin(parseinfo):
    bot.config["admins"].append(parseinfo["args"][1])
    bot.privmsg(parseinfo["chan"],"Added %s to admin list." % parseinfo["args"][1])

def deladmin(parseinfo):
    bot.config["admins"].remove(parseinfo["args"][1])
    bot.privmsg(parseinfo["chan"],"Removed %s from admin list." % parseinfo["args"][1])

def join(parseinfo):
    bot.config["chans"].append(parseinfo["args"][1])
    bot.sendraw("JOIN %s" % parseinfo["args"][1])
    bot.privmsg(parseinfo["chan"],"Joined %s" % parseinfo["args"][1])
    
def part(parseinfo):
    bot.config["chans"].remove(parseinfo["args"][1])
    bot.sendraw("PART %s" % parseinfo["args"][1])
    bot.privmsg(parseinfo["chan"],"Left %s" % parseinfo["args"][1])

def raw(parseinfo):
    bot.privmsg(parseinfo["chan"],str(parseinfo))
    
def kick(parseinfo):
    bot.sendraw("KICK %s %s %s" % (parseinfo["chan"],parseinfo["args"][1]," ".join(parseinfo["args"][2:])))

def prefix(parseinfo):
    prefix = parseinfo["args"][1]
    bot.prefix = prefix
    bot.privmsg(parseinfo["chan"],"My prefix is now %s." % prefix)

def sendraw(parseinfo):
    bot.sendraw(" ".join(parseinfo["args"][1:]))

def startimefunc(parseinfo):
    bot.privmsg(parseinfo["chan"],"I have been on since: %s GMT" % startime)

config = {\
    "host":"",
    "port":6667,
    "nick":"",
    "ident":"",
    "realname":"PythabotV3.7",
    "pass":"",
    "chans":[""],
    "admins":[""],
    "ownermask":"",
    "prefix":"^",
    "quitmsg":""
    }
bot = pythabot.Pythabot(config)
startime =  time.strftime("%a, %B %d %Y [%H:%M:%S]", time.gmtime())
bot.addCommand("hi",hi,"all",1)
bot.addCommand("botquit",quit,"owner",1)
bot.addCommand("mode",mode,"admins",3)
bot.addCommand("admin",admin,"owner",2)
bot.addCommand("deladmin",deladmin,"owner",2)
bot.addCommand("selfop",selfop,"all",1)
bot.addCommand("list",list,"all",1)
bot.addCommand("join",join,"admins",2)
bot.addCommand("part",part,"admins",2)
bot.addCommand("raw",raw,"all",1)
bot.addCommand("kick",kick,"admins",3)
bot.addCommand("prefix",prefix,"owner",2)
bot.addCommand("sendraw",sendraw,"owner",2)
bot.addCommand("start-time",startimefunc,"all",1)
bot.connect()
bot.listen()
