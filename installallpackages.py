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

█████╗  ███╗   ██╗ ██████╗  ██████╗ ██╗  ██╗
██╔══██╗████╗  ██║██╔═══██╗██╔═══██╗╚██╗██╔╝
███████║██╔██╗ ██║██║   ██║██║   ██║ ╚███╔╝ 
██╔══██║██║╚██╗██║██║   ██║██║   ██║ ██╔██╗ 
██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
''')

choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice == 'n' : sys.exit()
if choice == 'y' : os.system ("apt update -y && apt upgrade -y")
os.system ("termux-setup-storage")
os.system ("apt install python -y")
os.system ("apt install python2 -y")
os.system ("apt install wget -y")
os.system ("apt install clang -y")
os.system ("apt update")
os.system ("apt upgrade")
os.system ("curl -fsSL https://ollama.com/install.sh | sh")
os.system ("ollama serve")
os.system ("ls")