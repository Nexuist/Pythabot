#!/usr/bin/env python

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
    bot.privmsg(parseinfo["chan"],"Commands: " + " ".join(bot.commandlist))
    bot.privmsg(parseinfo["chan"],"Channels I'm in: " + " ".join(config["chans"]))
    bot.privmsg(parseinfo["chan"],"Admins: " + " ".join(bot.config["admins"]))

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

def mute(parseinfo):
    if bot.settings["mute"] == "off":
        bot.settings["mute"] = "on"
    else:
        bot.settings["mute"] = "off"
        bot.privmsg(parseinfo["chan"],"Mute off.")

def kickjoin(parseinfo):
    if bot.settings["kickjoin"] == "off":
        bot.settings["kickjoin"] = "on"
        bot.privmsg(parseinfo["chan"],"Kickjoin on.")
    else:
        bot.settings["kickjoin"] = "off"
        bot.privmsg(parseinfo["chan"],"Kickjoin off.")

def prefix(parseinfo):
    prefix = parseinfo["args"][1]
    prefix = prefix[0:1]
    bot.prefix = prefix
    bot.privmsg(parseinfo["chan"],"My prefix is now %s." % prefix)

def sendraw(parseinfo):
    bot.sendraw(" ".join(parseinfo["args"][1:]))

def startimefunc(parseinfo):
    bot.privmsg(parseinfo["chan"],"I have been on since: %s GMT" % startime)

config = {\
    "host":"irc.freenode.net",
    "port":6667,
    "nick":"techsbot",
    "ident":"Pythabot3",
    "realname":"Techboy6601",
    "pass":"",
    "chans":["#botters-test"],
    "admins":["techboy6601"],
    "ownermask":"unaffiliated/techboy6601",
    "prefix":"^",
    "quitmsg":"This is my quit message."
    }
bot = pythabot.Pythabot(config)
startime =  time.strftime("%a, %B %d %Y [%H:%M:%S]", time.gmtime())
bot.addcommand("hi",hi,"all",1)
bot.addcommand("botquit",quit,"owner",1)
bot.addcommand("mode",mode,"admins",3)
bot.addcommand("admin",admin,"owner",2)
bot.addcommand("deladmin",deladmin,"owner",2)
bot.addcommand("selfop",selfop,"all",1)
bot.addcommand("help",list,"all",1)
bot.addcommand("list",list,"all",1)
bot.addcommand("join",join,"admins",2)
bot.addcommand("part",part,"admins",2)
bot.addcommand("raw",raw,"all",1)
bot.addcommand("kick",kick,"admins",3)
bot.addcommand("mute",mute,"admins",1)
bot.addcommand("kickjoin",kickjoin,"admins",1)
bot.addcommand("prefix",prefix,"owner",2)
bot.addcommand("sendraw",sendraw,"owner",2)
bot.addcommand("start-time",startimefunc,"all",1)
bot.connect()
bot.listen()
