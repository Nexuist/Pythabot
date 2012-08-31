#!/usr/bin/env python

import sys,socket,string, time


class Pythabot:
    #This will be executed when the class is created, so here we initialize all the important variables
    def __init__(self,config):
        print("Pythabot v3.6.1")
        print("Simple IRC framework")
        print("Made by Techboy6601")
        self.config = config
        self.buffer = ""
        self.debounce = False
        self.debounce2 = False
        self.commands = {}
        self.commandlist = []
        self.prefix = self.config["prefix"]
        self.sock = socket.socket() #Initialize socket.
        print("Ready to connect")
    def connect(self):
        #We have to make sure the address you give it is online at the time
        try:
            self.sock.connect((self.config["host"],self.config["port"]))
            print("Connected to %s" % self.config["host"])
            if (len(self.config["pass"]) != 0): #Check if password exists
                self.sendraw("PASS %s" % self.config["pass"]) #This sends the password to the IRC server using the PASS command; this must come before anything else
            else:
                print("Account identification bypassed.")
            self.sendraw("NICK %s" % self.config["nick"]) #This sends the nick to the IRC server using the NICK command
            self.sendraw("USER %s %s bla :%s" % (self.config["ident"],self.config["host"],self.config["realname"])) #This is the USER command. It sends your IDENT (client), HOST, (irc server domain), and REALNAME (can be anything you want)
            print("Identified as %s" % self.config["nick"])
        except socket.error:
            self.quit("Could not connect to port %s, on %s." % (self.config["port"],self.config["host"])) #Here's that % in action

    def addCommand(self,text,func,permission,arglength):
        #You use the addcommand function to add commands to the commandslist. You'll see what this is for later.
        self.commands[text] = {"func":func,"permission":permission,"arglength":arglength}
        self.commandlist.append(text)
    
    def initparse(self,line):
        #Here's an example value of the line variable: "':techboy6601!~IceChat77@unaffiliated/techboy6601','PRIVMSG','#botters-test',':yo','wuts','up'"
        senderline = line[0] #This selects the ":techboy6601!~IceChat77@unaffiliated/techboy6601" part of line
        chan = line[2] #This would be #botters-test
        msg = " ".join(line[3:]) #And this would select everything after and in ':yo': in this case, ':yo wuts up'
        msg = msg[1:] #This takes away that annoying colon, so you're left with 'yo wuts up'
        args = msg.split(" ") #Finally, this splits the message into arguments, so now 'yo wuts up' is turned into 'yo','wuts','up'
        firstarg = args[0] #This would then select the very first argument, in this case 'yo'
        exapoint = senderline.find("!")#Remember senderline? This finds the first ! in it and returns its position.
        tildepoint = senderline.find("~") + 1 #This finds the first ~, and adds one to its position - you will see why later
        atpoint = senderline.find("@") + 1 #Same thing as the tilde, except for the @ sign
        sender = senderline[1:exapoint] #This separates senderline into an easier-to-understand string; this would select the words between the first location (due to the pesky colon) and the location of the !
        #so now, sender would equal "techboy6601"
        ident = senderline[tildepoint:atpoint-1] #Same thing as sender, which returns 'IceChat77'
        mask = senderline[atpoint:] #And finally, this returns "unaffiliated/techboy6601', otherwise known as the hostmask

        parseinfo = {\
            "sender":sender,
            "ident":ident,
            "mask":mask,
            "chan":chan,
            "msg":msg,
            "firstarg":firstarg,
            "args":args
            }
        #This puts all the data we've collected into a less-messier dictionary and mails it off to the parse function
        self.parse(parseinfo)

    def parse(self,parseinfo):
        msg = parseinfo["firstarg"] #In our example, this is 'yo'
        prelen = len(self.prefix) #Yay! Multi-character prefixes!
        if msg[0:prelen] == self.prefix: #self.prefix is ^ (if you haven't changed it), so here we check if somebody is talking to the bot or not
            msg = msg[1:]
            if msg in self.commands: #This is empty now, but it won't be; it checks if what you said is in the commandslist
                if (self.commands[msg]["permission"] == "owner"): #Check the instruction manual for what permissions mean
                    if len(parseinfo["args"]) >= self.commands[msg]["arglength"]: #This makes sure that you gave the command enough arguments to work with
                         if parseinfo["mask"] == self.config["ownermask"]: #This is owner permission, so only the person with the mask = ownermask gets to execute it
                             self.commands[msg]["func"](parseinfo) #This is a hacky way to run a function: Check the instruction manual for better understanding. 
                         else:
                             self.privmsg(parseinfo["chan"],"Error: You are not the owner!") #Don't want to let them off without a warning!
                    else:
                        self.privmsg(parseinfo["chan"],"Error: Invalid parameters.") #Same thing as above, except this handles the length problem
                         
                if (self.commands[msg]["permission"] == "all"): #This is open to everyone and everything, but it has basically the same structure as the owner permission
                    if len(parseinfo["args"]) >= self.commands[msg]["arglength"]:
                        self.commands[msg]["func"](parseinfo)
                    else:
                        self.privmsg(parseinfo["chan"],"Error: Invalid parameters.")
                    
                if (self.commands[msg]["permission"] == "admins"): #Now, this is different. This command only works for admins. 
                    if len(parseinfo["args"]) >= self.commands[msg]["arglength"]: #Check for argument length
                        if parseinfo["mask"] in self.config["admins"] or parseinfo["mask"] in self.config["ownermask"]: #And now it checks if the sender (techboy6601) is in the admin list, which it isn't!
                            self.commands[msg]["func"](parseinfo)
                        else:
                            self.privmsg(parseinfo["chan"],"Error: You are not an admin!")
                    else:
                        self.privmsg(parseinfo["chan"],"Error: Invalid parameters.")

            else:
                self.privmsg(parseinfo["chan"],"Error: Unknown command") #If you started a command with ^, but it didn't match anything make sure to tell them that
        
    def listen(self):
        try: #Why is this here? To prevent dieing from netsplits :P
            while 1:
                self.buffer = self.buffer+self.sock.recv(1024) #Because sockets are so hacky to work with, we have to keep a buffer open so that everything gets sent
                print self.buffer
                if ("/MOTD" in self.buffer and self.debounce == False):  #Most servers send a /MOTD command after they've finished their intro
                    for chan in self.config["chans"]: #So that's our cue to start joining channels
                        self.sendraw("JOIN %s" % chan)
                        print("Joined %s" % chan)
                        self.debounce == True # This is set because some people may say "/MOTD" and trigger the channel joining
                temp=self.buffer
                temp = temp.split("\n") #Splits newlines from the buffer, and returns it in a list
                self.buffer=temp.pop( ) #This makes the buffer equal to the last line of the buffer. Why? Because sockets are hacky and sometimes you'll end up with half a sentence instead of a fully-received one.
                for line in temp:
                    line=string.rstrip(line)
                    line=line.split(" ")
                    if(line[0]=="PING"): #Make sure to respond to PINGs!
                        self.sendraw("PONG %s" % line[1])
                        print("PONG %s" % line[1])
                    if (line[1] == "PRIVMSG"): #If someone/something talks, start parsing it so the bot can figure out what to do
                        self.initparse(line)
        except socket.error:
            print("Socket error. Reconnecting...")
            self.connect()
                    
    #system commands
    def sendraw(self,msg):
        self.sock.send(msg + "\r\n") #This sends raw data through the socket to the server. It also takes the burden of appending \r\n to the end of everything off.
    def privmsg(self,to,msg):
        self.sock.send("PRIVMSG %s :%s\r\n" % (to,msg)) #And now, you don't have to type out raw PRIVMSG statements either!

    #Quits the server, closes the socket, and exits the program
    def quit(self,errmsg):
        print("Error: %s" % errmsg)
        self.sendraw("QUIT :%s" % self.config["quitmsg"])
        self.sock.close()
        sys.exit(1)
