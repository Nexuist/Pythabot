#!/usr/bin/env python

#This bot helps keep OP in channels on servers without access to services.
#If your IRC server has access to ChanServ (/msg chanserv help to find out)
#then you should use that instead.


import pythabot

def op(parseinfo):
	bot.sendraw("MODE %s +o %s" % (parseinfo["chan"], parseinfo["firstarg"]))


config = {\
    "host":"",
    "port":6667,
    "nick":"",
    "ident":"",
    "realname":"PythabotV3.6",
    "pass":"",
    "chans":[""],
    "admins":[""], # add the hostmasks of the people who should be able to op here
    "ownermask":"",
    "prefix":"^",
    "quitmsg":""
    }
bot = pythabot.Pythabot(config)
bot.addCommand("op",op,"admins",1)
bot.connect()
bot.listen()
