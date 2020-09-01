#import necessary behaviors
import time
import sys
import os


#title "screen"
print("Loading...")
print("")

time.sleep(3)

print("Welcome to VIRUS SIMULATOR V.1.0")
print("")

#game setup code
print("Select Gamemode...")
print("")

print("1: Singleplayer")
print("2: Multiplayer")
print("")

gamemode=input("Gamemode: ")

if gamemode == "1":
  print("Choose gametype")
  print("")
  print("1: Quick Game, Jump Right into the Action.")
  print("2: Custom. Change EVERY aspect of the game.")
  print("")
  gametype=input("Gametype: ")
  if gametype == "1":
    os.system('python quickgame.py')

elif gamemode == "2":