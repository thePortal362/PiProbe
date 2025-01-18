import subprocess
import http.server
import socketserver
import socket
import re
import csv
import os
import time
import shutil
from datetime import datetime

active_wireless_networks = []

wifi_interface_choice = "wlan0"

def start_server():
    html_file = input("Enter the full path to the HTML file you want to serve: ").strip()
    port_selection = input("What Port do you want to use? (default=8000): ").strip()
    
    
    if not port_selection:
        port_selection = 8000
    else:
        port_selection = int(port_selection)
    
    if not os.path.isfile(html_file):
        print(f"Error: The file '{html_file}' does not exist.")
        return
    
    directory = os.path.dirname(html_file)
    file_name = os.path.basename(html_file)
    
   
    os.chdir(directory)
    
    
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/" or self.path == f"/{file_name}":
                self.path = f"/{file_name}"
                return super().do_GET()
            else:
                self.send_error(404, "File Not Found")
    
    
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    
    with socketserver.TCPServer(("", port_selection), CustomHandler) as httpd:
        os.system('clear')
        time.sleep(0.5)
        print(f"Serving file '{file_name}' on:")
        print(f"  Localhost: http://localhost:{port_selection}")
        print(f"  Network: http://{local_ip}:{port_selection}")
        print("")
        print("Press \033[31mCtrl+C\033[0m to stop the server.")
        print("")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

def check_if_installed(program_name):
    result = subprocess.run(['which', program_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def check_for_essid(essid, lst):
    check_status = True

if not 'SUDO_UID' in os.environ.keys():
    print("This Program needs Sudo to run properly!")
    print("If you don't have access to superuser rights try the rootless version:")
    print("python3 rootless.py")
    print("Note that some functions might not work properly")
    exit()

def cpu_temp():
    try:
        output = subprocess.check_output(['sensors']).decode()
        for line in output.splitlines():
            if "Core 0" in line:  
                return line.strip()
    except Exception as e:
        return f"Error reading temperature: {e}"

def get_wifi_networks():
    try:
        wifi = subprocess.run(['sudo', 'iwlist', wifi_interface_choice, 'scan'], capture_output=True, text=True)
        output = wifi.stdout

        networks = re.findall(r'ESSID:"(.*?)"', output)
        signal_strengths = re.findall(r'Signal level=(-?\d+)', output)

        if not networks:
            print("No WiFi Networks found")
            return

        print(f"{'SSID':<30}{'Signal Strength'}")
        print("=" * 50)
        for ssid, signal in zip(networks, signal_strengths):
            print(f"{ssid:<30}{signal} dBm")

    except Exception as e:
        print(f"Error scanning for Neworks: {e}")

def main():
    print("Scanning for WiFi Networks")
    print("--------------------------")
    print()
    get_wifi_networks()

while True:

    os.system('clear')
    print("--------------------------------------")
    print("-----------For Debian/Arch------------")
    print("""--------------------------------------
 ___    _    ___                                                       
|   |  |_|  |   |            |                                          
|___|   _   |___|  ___  ___  |___   __
|      | |  |     | |/ |   | |   | |__|
|      |_|  |     |_|  |___| |___| |__ """)
    print("--------------------------------------")
    print("---------PiProbe by thePortal---------")
    print("---github.com/thePortal362/PiProbe----")
    print("--------------------------------------")
    print("")
    print("Select Mode:")
    print("1. WiFi")
    print("2. Start HTTP Server")
    print("3. Tools")
    print("4. Other")
    print("5. Calculate Prim Numbers")
    print("6. Exit")
    mode_select = input()
    time.sleep(0.5)


    if mode_select == "1" :
        print("WiFi mode selected")
        time.sleep(0.5)
        os.system('clear')
        time.sleep(0.5)
        print("What do you want to do?")
        time.sleep(0.5)
        print("1. Scan for interfaces")
        print("2. Scan for WiFi networks")
        print("3. Fern WiFi Cracker")
        print("4. Connect to WiFi")
        print("5. MDK3 Wifi Deauth")
        print("6. Go back")
        wifi_select = input()

        if wifi_select == "2":
            print("Scanning for WiFi Networks...")
            time.sleep(1)
            os.system('clear')
            main()
            print("")
            print("Press \033[31me\033[0m to Exit")
            exit_ans = input()
            if exit_ans == "e":
                os.system('clear')
            else:
                time.sleep(3600)

        elif wifi_select == "1":
            os.system('clear')
            time.sleep(0.5)

            wlan_pattern = re.compile("^wlan[0-9]+")

            check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())

            if len(check_wifi_result) == 0:
                print("No WiFi Adapter found")
                exit()

            for index, item in enumerate(check_wifi_result):
                print(f"{item}")

            while True:
                wifi_interface_choice = input("Select an interface: ")
                try:
                    if check_wifi_result:
                        subprocess.run(['sudo', 'airmon-ng', 'start', wifi_interface_choice])
                        break
                except:
                    print("Please select a real interface.") 
            os.system('clear')                  
        
        elif wifi_select == "3":
            os.system('clear')
            print("Starting Fern WiFi Cracker")
            os.system('clear')
            if check_if_installed('fern-wifi-cracker'):
                print("Checking if installed...")
                time.sleep(0.5)
                print("is_installed \033[32m[ok]\033[0m")
                time.sleep(1.5)
            else:
                print("Checking if installed...")
                time.sleep(0.5)
                print("is_installed \033[31m[failed]\033[0m")
                time.sleep(0.5)
                print("Do you want to install it now? [1=Y/2=n]")
                install_ans = input()
                if install_ans == "1":
                    print("Debian[1] or Arch[2]?")
                    operating_sys = input()
                    if operating_sys == "1":
                        os.system('clear')
                        time.sleep(1)
                        print("Installing for Debian...")
                        time.sleep(0.5)
                        try:
                            subprocess.run(['sudo', 'apt', 'install', 'fern-wifi-cracker'], check=True)
                        except subprocess.CalledProcessError as e:
                            print(f"Error: {e}")
                            print("\033[31mfailed\033[0m to install")
                    elif operating_sys == "2":
                        os.system('clear')
                        time.sleep(1)
                        print("Installing for arch...")
                        time.sleep(0.5)
                        try:
                            subprocess.run(['sudo', 'pacman', '-Syu', 'fern-wifi-cracker'])
                        except subprocess.CalledProcessError as e:
                            print(f"Error: {e}")
                            print("\033[31mfailed\033[0m to install")
                elif install_ans == "2":
                    print("Not installing")
                    time.sleep(1)

                time.sleep(1)

            os.system('clear')
            time.sleep(0.5)
            try:
                subprocess.run(['sudo', 'fern-wifi-cracker'], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")

        elif wifi_select == "4":
            print("Connection Mode")
            time.sleep(0.5)
            os.system('clear')
            print("SSID:")
            connect_ssid = input()
            time.sleep(0.5)
            print("Password: (If none type nothing)")
            connect_pwd = input()
            os.system('clear')
            print("Trying to connect...")
            try:
                subprocess.run(['nmcli', 'dev', 'wifi', 'connect', connect_ssid, 'password', connect_pwd, '--ask'], check=True)
                os.system('clear')
                print("Connected!")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
            time.sleep(5.5)
            os.system('clear')

        elif wifi_select == "5":
            print("Deauth")
            time.sleep(0.5)
            os.system("clear")
            print("What IP addr do you want to attack? ")
            attack_ip = input()
            time.sleep(0.5)
            os.system('clear')
            try:
                subprocess.run(["sudo", "mdk3", wifi_interface_choice, "d", attack_ip])
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")

        elif wifi_select == "6":
            time.sleep(0.2)

    if mode_select == "2":
        os.system('clear')
        time.sleep(0.5)
        start_server()
        time.sleep(2.5)

    if mode_select == "3":
        os.system('clear')
        print("All Tools:")
        print("1. Bettercap")
        print("2. Ping Service")
        print("3. Go back")
        tool_select = input()

        if tool_select == "1":
            os.system('clear')
            if check_if_installed('bettercap'):
                print("Checking if installed...")
                time.sleep(0.5)
                print("is_installed \033[32m[ok]\033[0m")
                time.sleep(1)
            else:
                print("Checking if installed...")
                time.sleep(0.5)
                print("is_installed \033[31m[failed]\033[0m")
                time.sleep(0.5)
                print("Do you want to install bettercap? Y=1/n=2")
                install_ans = input()
                if install_ans == "1":
                    os.system('clear')
                    print("Debian[1] or Arch[2]?")
                    operating_sys = input()
                    if operating_sys == "1":
                        os.system('clear')
                        subprocess.run(['sudo', 'apt', 'install', 'bettercap'])
                    elif operating_sys == "2":
                        os.system('clear')
                        subprocess.run(['sudo', 'pacman', '-S', 'bettercap'])
            print("Starting Bettercap...")
            os.system('clear')
            try:
                subprocess.run(['bettercap'], check=True)
            except subprocess.CalledProcessError as e:
                time.sleep(3600)
                print(f"Error: {e}")
            time.sleep(3.5)
            os.system('clear')

        elif tool_select =="2":
            os.system('clear')
            print("Starting ping service...")
            time.sleep(0.5)
            os.system('clear')
            print("What Host do you want to ping?")
            ping_host = input()
            os.system('clear')
            time.sleep(0.5)
            print("How many times?")
            ping_cnt = input()
            os.system('clear')
            time.sleep(0.5)
            try:
                subprocess.run(['ping', ping_host, '-c', ping_cnt], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
            time.sleep(3.5)
            os.system('clear')

        elif tool_select == "3":
            time.sleep(0.2)

    if mode_select == "4":
        print("Other selected")
        time.sleep(0.5)
        os.system('clear')
        print("What do you want to do?")
        print("1. Apt update & upgrade")
        print("2. Install something with apt")
        print("3. Help")
        print("4. Credits")
        print("5. Shutdown or Reboot")
        print("6. Get CPU Temp")
        print("7. Go back")
        other_select = input()
        
        if other_select == "1":
            os.system('clear')
            print("Making sure you have the latest")
            time.sleep(1.5)
            os.system('clear')
            print("Please wait...")
            try:
                subprocess.run(['apt', 'update'], check=True)
                subprocess.run(['apt', 'upgrade', '-y'], check=True)
                os.system('clear')
                print("Success!")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
            time.sleep(2.5)
            os.system('clear')
        
        if other_select == "2":
            os.system('clear')
            print("What do you want to install?")
            install_pkg = input()
            os.system('clear')
            print("Installing " + install_pkg + "...")
            time.sleep(0.5)
            try:
                subprocess.run(['apt', 'install', install_pkg], check=True)
                os.system('clear')
                print("Success!")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
            time.sleep(2.5)
            os.system('clear')

        if other_select == "3":
            os.system('clear')
            print("E-Mail me on: theportalprogrammer@gmail.com")
            time.sleep(5)
            os.system('clear')

        if other_select == "4":
            os.system('clear')
            print("Script by thePortal")
            print("Thanks to David Bombal for some Code Snippets")
            time.sleep(5)
            os.system('clear')

        if other_select == "5":
            os.system('clear')
            print("What do you want to do?")
            print("1. Shutdown")
            print("2. Reboot")
            sutd_select = input()

            if sutd_select == "1":
                subprocess.run(['shutdown', '-h', 'now'])

            if sutd_select == "2":
                subprocess.run(['reboot'])    

        if other_select == "6":
            os.system('clear')
            print(cpu_temp)
            time.sleep(3)
            os.system('clear')


        if other_select == "7":
            time.sleep(0.2)

    if mode_select == "5":
        os.system('clear')
        def calculate_primes(limit):
            """
            Calculate all prime numbers up to a given limit using the Sieve of Eratosthenes.
    
            :param limit: int - The upper limit of numbers to check for primality.
            :return: list - A list of prime numbers up to the specified limit.
            """
            if limit < 2:
                return []

            
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False  

            
            for num in range(2, int(limit**0.5) + 1):
                if is_prime[num]:
                    
                    for multiple in range(num * num, limit + 1, num):
                        is_prime[multiple] = False

            
            primes = [num for num, prime in enumerate(is_prime) if prime]
            return primes


        
        if __name__ == "__main__":
            os.system('clear')
            upper_limit = int(input("Enter the upper limit to calculate prime numbers: "))
            primes = calculate_primes(upper_limit)
            print(f"Prime numbers up to {upper_limit}: {primes}")
        time.sleep(5)    
    
    if mode_select == "6":
        subprocess.run(['sudo', 'airmon-ng', 'stop', wifi_interface_choice + 'mon'])
        os.system('clear')
        break
