#import necessary behaviors
import time
import sys
import os

#import other parts of the game


print("Select option...")
print("")
print("1: text speed")
print("2: year")
print("3: multiplayer settings placeholder.")
print("")
setting = input("Setting: ")

if setting == "1":
  time.sleep(textspeed)
  print("Choose speed.")
  print("")
  print("1: Fast")
  print("2: Normal")
  print("3: Slow")
  print("")
  textspeed = input("Speed: ")
  time.sleep(textspeed)
  os.system('python main.py')