import time
import os
import sys
import colorama

def sekilliprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)


time.sleep(4)

sekilliprint("Welcome to Install Termux All Packages!")

os.system("clear")

time.sleep(3)

print('''


 __      __________ __________    _____    _____________________________
/  \    /  \_____  \\______   \  /     \  /  _____/\______   \__    ___/
\   \/\/   //   |   \|       _/ /  \ /  \/   \  ___ |     ___/ |    |   
 \        //    |    \    |   \/    Y    \    \_\  \|    |     |    |   
  \__/\  / \_______  /____|_  /\____|__  /\______  /|____|     |____|   
       \/          \/       \/         \/        \/                     
''')

choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update -y && apt upgrade -y")
os.system ("pd sh debian")
os.system ("ollama list")
# wormgpt api key zfhudhivc-hiirdkmm4784;fiivmprs_ho64
os.system ("ollama pull tinyllama")
os.system ("ollama run tinyllama")


