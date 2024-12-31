import subprocess
import re
import csv
import os
import time
import shutil
from datetime import datetime

active_wireless_networks = []

def check_for_essid(essid, lst):
    check_status = True

if not 'SUDO_UID' in os.environ.keys():
    print("This Program needs Sudo to run properly!")
    exit()

def cpu_temp():
    try:
        output = subprocess.check_output(['sensors']).decode()
        for line in output.splitlines():
            if "Core 0" in line:  # Find a line that mentions Core temperature
                return line.strip()
    except Exception as e:
        return f"Error reading temperature: {e}"

for file_name in os.listdir():
    # We should only have one csv file as we delete them from the folder 
    #  every time we run the program.
    if ".csv" in file_name:
        print("There shouldn't be any .csv files in your directory. We found .csv files in your directory and will move them to the backup directory.")
        # We get the current working directory.
        directory = os.getcwd()
        try:
            # We make a new directory called /backup
            os.mkdir(directory + "/backup/")
        except:
            print("Backup folder exists.")
        # Create a timestamp
        timestamp = datetime.now()
        # We move any .csv files in the folder to the backup folder.
        shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)

while True:

    os.system('clear')
    print("--------------------------------------")
    print("---------For Ethical Use only---------")
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
    print("2. BLE")
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
            try:
                while True:
                    subprocess.call('clear', shell=True)
                    for file_name in os.listdir():
                        fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
                        if ".csv" in file_name:
                            with open(file_name) as csv_h:
                                csv_h.seek(0)
                                csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)
                                for row in csv_reader:
                                    if row["BSSID"] == "BSSID":
                                        pass
                                    elif row["BSSID"] == "Station MAC":
                                        break
                                    elif check_for_essid(row["ESSID"], active_wireless_networks):
                                        active_wireless_networks.append(row)
                    print("Press Ctrl+C to stop scan\n")
                    print("No |\tBSSID              |\tChannel|\tESSID                         |")
                    print("___|\t___________________|\t_______|\t______________________________|")
                    for index, item in enumerate(active_wireless_networks):
                        print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
                    time.sleep(1)
        
            except KeyboardInterrupt:
                print("\nReady to make choice")

            
            os.system('clear')

        elif wifi_select == "1":
            os.system('clear')
            time.sleep(0.5)

            wlan_pattern = re.compile("^wlan[0-9]+")

            check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())

            if len(check_wifi_result) == 0:
                print("No WiFi Adapter found")
                exit()

            for index, item in enumerate(check_wifi_result):
                print(f"{index} - {item}")

            while True:
                wifi_interface_choice = input("Select an interface: ")
                try:
                    if check_wifi_result[int(wifi_interface_choice)]:
                        subprocess.run(['sudo', 'airmon-ng', 'start', wifi_interface_choice])
                        break
                except:
                    print("Please select a real interface.") 
            os.system('clear')                  
        
        elif wifi_select == "3":
            os.system('clear')
            print("Starting Fern WiFi Cracker")
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
        print("Not avaible yet")
        time.sleep(2.5)
        os.system('clear')

    if mode_select == "3":
        os.system('clear')
        print("All Tools:")
        print("1. Bettercap")
        print("2. Ping Service")
        print("3. Go back")
        tool_select = input()

        if tool_select == "1":
            os.system('clear')
            print("Starting Bettercap...")
            os.system('clear')
            try:
                subprocess.run(['bettercap'], check=True)
            except subprocess.CalledProcessError as e:
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
            print("Updating and upgrading")
            time.sleep(0.5)
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

            # Create a boolean array "is_prime[0..limit]" and initialize all entries as True.
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers.

            # Use the sieve algorithm.
            for num in range(2, int(limit**0.5) + 1):
                if is_prime[num]:
                    # Mark all multiples of num as not prime.
                    for multiple in range(num * num, limit + 1, num):
                        is_prime[multiple] = False

            # Collect all prime numbers.
            primes = [num for num, prime in enumerate(is_prime) if prime]
            return primes


        # Example usage:
        if __name__ == "__main__":
            os.system('clear')
            upper_limit = int(input("Enter the upper limit to calculate prime numbers: "))
            primes = calculate_primes(upper_limit)
            print(f"Prime numbers up to {upper_limit}: {primes}")
        time.sleep(5)    
    
    if mode_select == "6":
        break
