# !usr/bin
# auther : amin abdedaiem
# date & time : march 31th 2021 11:30 AM
# subject : script to install all blackarch ripo without errors 


import os
from subprocess import call
import re
# os.system("ls -l")

# run a command in the terminal 
take_commands = os.system("sudo pacman -Sg | grep blackarch")

