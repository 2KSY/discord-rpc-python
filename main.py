import os 
import time
os.system("clear")

#CUSTOMIZE THIS PART

TOKENHERE = "ur token here if your retarded"
APPID = discord app id (int)

#DONT EDIT BELOW

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.WARNING}DISCORD RPC{bcolors.ENDC}")
print(f"{bcolors.WARNING}made by pxizone#0070{bcolors.ENDC}")
print(f"{bcolors.WARNING}Version 5.2{bcolors.ENDC}")
time.sleep(1.5)
print(f"{bcolors.UNDERLINE}                           {bcolors.ENDC}")
print("")
print(f"{bcolors.OKBLUE}Importing required modules{bcolors.ENDC}")
print(f"{bcolors.UNDERLINE}                           {bcolors.ENDC}")
print("")
time.sleep(2.0)
print ("\033[A                             \033[A")
print ("\033[A                             \033[A")
print ("\033[A                             \033[A")
print ("\033[A                             \033[A")
print(f"{bcolors.OKBLUE}Import Complete{bcolors.ENDC}")
print("")

# importing required packages
import datetime
import discord
import asyncio
from discord.ext import commands
import threading
# Customize Here

presentDate = datetime.datetime.now() 
unix_timestamp = datetime.datetime.timestamp(presentDate)*1000

# DO NOT EDIT THIS PART

entercmd = 'help'
prefix = 'x' # edit the bot prefix for the command
client = discord.Client()
name1 = input("Enter the app name: ")
print("")
detail1 = input("App Details: ")
print("")
state1 = input("State of the app: ")
print("")
print(f"{bcolors.WARNING}NEW{bcolors.ENDC} Elapsed Time")
elapsed1 = input("[type n to turn off]: ")

imagekey1 = "imagekey1"

# do not modify / edit the rest of this if you have little to no python / discord.py knowledge
bot = commands.Bot(command_prefix=prefix, self_bot=True)


hitjack = bot.change_presence(activity=discord.Activity(application_id=APPID, name=name1, type=discord.ActivityType.playing, state=state1, details=detail1, assets={'large_image_key' : imagekey1, 'large_text' : 'image'}, timestamps={'start' : unix_timestamp}))
hitjack1 = bot.change_presence(activity=discord.Activity(application_id=APPID, name=name1, type=discord.ActivityType.playing, state=state1, details=detail1, assets={'large_image_key' : imagekey1, 'large_text' : 'image'}))

@bot.event 
async def on_ready():
    print(f"{bcolors.UNDERLINE}                           {bcolors.ENDC}")
    print("")
    print(f"Logged in as {bcolors.OKGREEN}{bot.user.name}! {bcolors.ENDC}")
    print(f"{bcolors.FAIL}Do not share your token")
    print(f"with anyone else!{bcolors.ENDC}")
    time.sleep(1.5)
    print("")
    if elapsed1 == "n" :
    	await hitjack1
    else :
    	await hitjack
    print(f"{bcolors.OKBLUE}Custom Status applied{bcolors.ENDC}")
    print(f"{bcolors.UNDERLINE}                           {bcolors.ENDC}")
    print("")
    
    #Hi I'm still working in this part, so be sure to follow 2KSY on github
#    testing()
    
#user_input = "not available"
    
#def testing():
#    user_input = input()
 #   if user_input.lower() == "end":
  #  	print("script will end")
#    elif user_input.lower() == "reset":
#        print(" script is fine")
 #   else :
 #       print("not sure")

     
async def on_set():
    if elapsed1 == "n" :
    	await hitjack1
    else :
    	await hitjack
    await asyncio.sleep(60)
    client.loop.create_task(on_set())

@bot.command()
async def stop(ctx): # stops the streaming status and closes down
    if bot.user.id == ctx.message.author.id: # makes it so only you are able to shut down the bot
        print("bot shutdown requested")
        await bot.close()
        time.sleep(3)
       
bot.run(TOKENHERE, bot = False) # enter your token where it says TOKEN
