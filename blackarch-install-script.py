# !usr/bin
# auther : amin abdedaiem
# date & time : march 31th 2021 11:30 AM
# subject : script to install all blackarch ripo without errors 

# work note : the yes part of the script is not
# working at all , try fix it next time dude *wink* ;)

import os
from os import sys
from subprocess import call
import time
import re

# load the file 
file = open("output.txt","r")

# iterat through every singel command then store them in a list
choices = []
for f in file:
    choices.append(f)

# display all the categorys available

print("categorys : ")
for i in range(len(choices)):
  print(f"{choices[i]}",end='')
    

# asking the user to choose his category

category_choice = input("choose your category : blackarch-")

os.system("clear")

print(f"your category of choise were blackarch{category_choice}")

# prompt the error message if any , otherwise print ENJOY!

print("do you want to install a whole category ? : ")
test_of_what_to_install = input("[yes][no] : ")
os.system("clear")

if test_of_what_to_install == "yes":
  # os.system("sudo pacman -S blackarch" + category_choice)
  os.system("sudo pacman -Sg blackarch" + category_choice + "| grep blackarch > output.txt")
  time.sleep(0.1)
  file = open("output.txt","r")
  lenght = len("blacarch" + category_choice)
  cat = []
  for f in file:
    cat.append(f[lenght+2:])
  for x in range(len(cat)):      
    p = os.popen(f"sudo pacman -S {cat[x]}","w")
    p.write("y\n")
    p.close()
  print("the intallation have been seccessful")
else:
  os.system("sudo pacman -Sg blackarch" + category_choice + "| grep blackarch")
  time.sleep(0.1)
  choice = input(f"blackarch{category_choice} ")
  new_choice = choice.split()
  os.system("clear")
  for j in range(len(new_choice)):
    # installing 
    p = os.popen(f"sudo pacman -S {new_choice[j]}","w")
    p.write("y\n")
    p.close()
    time.sleep(0.1)
    os.system("clear")
  print("the intallation have been seccessful")