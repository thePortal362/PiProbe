import subprocess
import time
import os

print("Installing Requirements")
subprocess.run(['sudo', 'pacman', '-S', 'hping3'])
subprocess.run(['sudo', 'pacman', '-S', 'nmap'])
subprocess.run(['sudo', 'pacman', '-S', 'mdk3'])
