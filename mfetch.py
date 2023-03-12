import os

username = os.popen("echo $USER").read().strip()
hostname = os.popen("cat /etc/hostname").read().strip()
currentKernel = os.popen("uname -r").read().strip()
numberOfPackages = os.popen("pacman -Q | wc -l").read().strip()
totalRAM = os.popen("grep MemTotal /proc/meminfo | sed -r 's/MemTotal:        //'").read().strip()
currentShell = os.popen("echo $SHELL | grep -o '[a-Z0-9]*$'").read().strip()

print('''\033[1;35m
  __ __ ___ ___ _____ ____  _  
 |  V  | __| __|_   _/ _/ || | 
 | \\_/ | _|| _|  | || \\_| >< | 
 |_| |_|_| |___| |_| \__/_||_|
      \033[0m''')
print("\033[1;34muser: \033[m" + username)
print("\033[1;31mhostname: \033[m" + hostname)
print("\033[1;33mkernel: \033[m" + currentKernel)
print("\033[1;32mpkgs: \033[m" + numberOfPackages)
print("\033[1;36mmemory: \033[m" + totalRAM)
