import os
import time
import subprocess
from termcolor import colored

def banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(colored("""
        ██████╗  █████╗ ██╗      ███████╗███████╗███████╗ ██████╗ ██████╗ ███████╗
        ██╔══██╗██╔══██╗██║      ██╔════╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
        ██████╔╝███████║██║      ███████╗███████╗█████╗  ██║   ██║██████╔╝███████╗
        ██╔═══╝ ██╔══██║██║      ╚════██║╚════██║██╔══╝  ██║   ██║██╔═══╝ ╚════██║
        ██║     ██║  ██║███████╗███████║███████║███████╗╚██████╔╝██║     ███████║
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚══════╝
    """, 'green'))
    print(colored("AI BruteForce - 2025 Edition\n", 'cyan'))

def menu():
    print(colored("Main Menu", 'yellow'))
    print(colored("[1] Install Tools (Hashcat, John the Ripper, etc.)", 'cyan'))
    print(colored("[2] AI-Powered Brute-Force Attack", 'cyan'))
    print(colored("[3] AI-Powered Dictionary Attack", 'cyan'))
    print(colored("[4] Exit", 'red'))

def install_tools():
    print(colored("\n[Installing Tools...]", 'yellow'))
    if os.name == 'posix': 
        distro = subprocess.check_output('uname -a', shell=True).decode()
        if 'Android' in distro:
            print(colored("\nDetected: Termux (Android)\n", 'green'))
            os.system('pkg update && pkg install hashcat john -y')
        elif 'Ubuntu' in distro or 'Debian' in distro:
            print(colored("\nDetected: Ubuntu/Debian\n", 'green'))
            os.system('sudo apt update && sudo apt install hashcat john -y')
        elif 'Kali' in distro:
            print(colored("\nDetected: Kali Linux\n", 'green'))
            os.system('sudo apt update && sudo apt install hashcat john -y')
        else:
            print(colored("Unsupported Linux Distro", 'red'))
    else:
        print(colored("Unsupported OS!", 'red'))
    print(colored("Installation Complete!\n", 'green'))

def ai_brute_force():
    print(colored("\n[AI-Powered Brute-Force Attack]\n", 'green'))
    # Placeholder for brute-force logic

def ai_dictionary_attack():
    print(colored("\n[AI-Powered Dictionary Attack]\n", 'green'))
    # Placeholder for dictionary attack logic

def main():
    while True:
        banner()
        menu()
        choice = input(colored("\nEnter your choice: ", 'yellow'))

        if choice == '1':
            install_tools()
        elif choice == '2':
            ai_brute_force()
        elif choice == '3':
            ai_dictionary_attack()
        elif choice == '4':
            print(colored("\nExiting... Thank you for using AI BruteForce!\n", 'red'))
            time.sleep(1)
            break
        else:
            print(colored("\nInvalid choice! Please select a valid option.\n", 'red'))
        input(colored("\nPress Enter to continue...", 'yellow'))

if __name__ == "__main__":
    main()
