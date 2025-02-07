import time
import os
import sys
# import colorama

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
os.system ("termux-setup-storage")
os.system ("pkg install proot-distro -y")
os.system ("pd i debian")
os.system ("pd sh debian")
os.system ("apt update")
os.system ("apt upgrade")
os.system ("apt install curl")
os.system ("curl -fsSL https://ollama.com/install.sh | sh")
os.system ("ollama serve")
