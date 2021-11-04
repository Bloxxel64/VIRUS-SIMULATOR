import random
import time
import os
import sys

age = random.randint(1, 101)
birthmonth = random.randint(1, 13)
uid = input("enter userid: ")

print("hello", uid, "and welcome")
print()
print("To VIRUS SIMULATOR")
print()
informed = input("Have you 'played' before? ")

if informed == "no":
  print("PP")

if informed == "yes" or "y":
  print("okay, then we can begin.")
  