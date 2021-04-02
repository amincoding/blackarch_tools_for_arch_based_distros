# !usr/bin
# auther : amin abdedaiem
# date & time : march 31th 2021 11:30 AM
# subject : script to install all blackarch ripo without errors 

import os
from subprocess import call
import time

if os.system("sudo pacman -Sg | grep blackarch > /dev/null 2>&1") != 0:
  while os.system("sudo curl -O https://blackarch.org/strap.sh"):
    time.sleep()
  os.system("sudo chmod +x strap.sh")
  time.sleep(0.5)
  os.system("sudo ./strap.sh")
if os.system("sudo pacman -Sg | grep blackarch > /dev/null 2>&1") == 0:
  # saving the otutput of the silent execution of the file script to a file {output.txt}
  first_run = os.system("python3 script.py > output.txt")

  time.sleep(0.5)

  second_run = os.system("python3 blackarch-install-script.py")

