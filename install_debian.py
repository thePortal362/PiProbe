import subprocess
import time
import os

print("Installing Requirements")
subprocess.run(['sudo', 'apt', 'install', 'hping3'])
subprocess.run(['sudo', 'apt', 'install', 'nmap'])
subprocess.run(['sudo', 'apt', 'install', 'mdk3'])
