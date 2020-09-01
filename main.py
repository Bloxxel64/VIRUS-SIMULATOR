
#import necessary behaviors
import time
import sys
import os

#presettings
textspeed = 2

#title "screen"
print("Loading...")
print("")

time.sleep(textspeed)

print("Welcome to VIRUS SIMULATOR V.1.0")
print("")

time.sleep(textspeed)

#game setup code
print("Select Gamemode...")
print("")

print("1: Singleplayer")
print("2: Multiplayer")
print("3: Settings")
print("4: Never mind, i quit.")
print("")

gamemode = input("Gamemode: ")

if gamemode == "1":
  time.sleep(textspeed)
  print("Choose gametype...")
  print("")
  print("1: Quick Game, Jump Right into the Action.")
  print("2: Custom. Change EVERY aspect of the game.")
  print("")
  gametype=input("Gametype: ")
  if gametype == "1":
    time.sleep(textspeed)
    os.system('python quickgame.py')

elif gamemode == "2":
  time.sleep(textspeed)
  print("multiplayer coming soon.")
  print("goodbye. :)")
  print("")
  sys.exit

elif gamemode == "3":
  time.sleep(textspeed)
  os.system('python settings.py')

elif gamemode == "4":
  print("Bye Bye")
  sys.exit

