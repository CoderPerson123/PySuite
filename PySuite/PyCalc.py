# PyCalc
# Created by Nathan R (Mosrod) https://github.com/Mosrod

# Imports
from time import sleep
import sys

# Variables
run = 1

# Definitions

# Add
def add():
  x = input("Num1: ")
  y = input("Num2: ")
  z = x+y
  print(z)
  
# Subtract
def sub():
  x = input("Num1: ")
  y = input("Num2: ")
  z = x-y
  print(z)

# Multiply
def mul():
  x = input("Num1: ")
  y = input("Num2: ")
  z = x+y
  print(z)
  
# Divide
def div():
  x = input("Num1: ")
  y = input("Num2: ")
  z = x/y
  print(z)  
  
# Code
text = "Welcome to PyCalc"
for character in text:
  sys.stdout.write(character)
  sleep(0.1)
print("\n")
text = "Created by Nathan R (Mosrod)"
for character in text:
  sys.stdout.write(character)
  sleep(0.05)
print("\n")

while run == 1:
