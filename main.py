# this is a python console script for RATTMURDOCK users  
# written by : NinjaCat811

#** imports :

import os
import sys
import random
import getpass
from paramiko import SSHClient
# ** Variables : 

help_menu = """
Arguments : 
            XXX.ratt = RattMurdock target's device configuration file

Example    :
            python3 main.py example.ratt

"""
qoutes = [
    "There are other ways to see.",
    "I didn’t ask for that name.",
    "Listen, I need you to know why I’m hurting you … I’m doing this ’cause I enjoy it.",
    "How do you know the angel and the devil inside me aren’t the same thing?",
    "You don’t get to destroy who I am.",
    "No, it's not easy, but it's a choice, and it's a choice I remake every day.",
    "I am what I do in the dark now, I bleed only for myself",
    "I'd rather die as the devil than live as matt murdock",
    "You Hit Them And They Get Back Up, I Hit Them And They Stay Down",
    "There are no heroes, no villains. Just people with different agendas.",
    "I am daredevil"

]
qoute = random.choice(qoutes)
banner = f'''
 ██▀███   ▄▄▄      ▄▄▄█████▓▄▄▄█████▓ ███▄ ▄███▓ █    ██  ██▀███  ▓█████▄  ▒█████   ▄████▄   ██ ▄█▀
▓██ ▒ ██▒▒████▄    ▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒▀█▀ ██▒ ██  ▓██▒▓██ ▒ ██▒▒██▀ ██▌▒██▒  ██▒▒██▀ ▀█   ██▄█▒ 
▓██ ░▄█ ▒▒██  ▀█▄  ▒ ▓██░ ▒░▒ ▓██░ ▒░▓██    ▓██░▓██  ▒██░▓██ ░▄█ ▒░██   █▌▒██░  ██▒▒▓█    ▄ ▓███▄░ 
▒██▀▀█▄  ░██▄▄▄▄██ ░ ▓██▓ ░ ░ ▓██▓ ░ ▒██    ▒██ ▓▓█  ░██░▒██▀▀█▄  ░▓█▄   ▌▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ 
░██▓ ▒██▒ ▓█   ▓██▒  ▒██▒ ░   ▒██▒ ░ ▒██▒   ░██▒▒▒█████▓ ░██▓ ▒██▒░▒████▓ ░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░  ▒ ░░     ▒ ░░   ░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ░▒ ░ ▒░  ▒   ▒▒ ░    ░        ░    ░  ░      ░░░▒░ ░ ░   ░▒ ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░
  ░░   ░   ░   ▒     ░        ░      ░      ░    ░░░ ░ ░   ░░   ░  ░ ░  ░ ░ ░ ░ ▒  ░        ░ ░░ ░ 
   ░           ░  ░                         ░      ░        ░        ░        ░ ░  ░ ░      ░  ░   
                                                                   ░               ░               
[.] {qoute}
[.] Created by :  NinjaCat811

'''

username = getpass.getuser()
header = f"{username}@RattMurdock"

options_menu ="""
    [*] Select A Number To Use Payload [*]

        Payloads :

        [0] Remote Console
            

"""

#** functions :
def parser():
    pass

def read_config(config_file):
    configuration = {}
    read_lines= open(config_file,"r").readlines()
    configuration["ipAddress"] =  read_lines[0].strip()
    configuration["userName"] =  read_lines[1].strip()
    configuration["password"] =  read_lines[2].strip()
    configuration["wordDirectory"] =  read_lines[3].strip()
    return configuration

def exit():
    sys.exit()

def cli(arguments):
    if arguments:
        # print("Options : ")


        try:
            configuration = read_config(sys.argv[1])

        except FileNotFoundError:
            print("[!] File does not exist")

            exit()

        print(options_menu)
        config_file = input(f"{header} $ ") 

        ipv4 = configuration.get("ipAddress")
        password= configuration.get("password")
        username = configuration.get("userName")

        if config_file == "0":  
            connect(password,username,ipv4)



        ipv4 = configuration.get("ipAddress")
        password= configuration.get("password")
        username = configuration.get("userName")

        if config_file == "0":  
            connect(password,username,ipv4)

    else:
        print(help_menu)

def os_detection():
    if os.name == "nt":
        return "w"
    
    if os.name == "posix":
        return "l"

# connect to target
def connect(password,username,ipv4):
    command = f"sshpass -p {password} ssh {username}@{ipv4} 'powershell'"
    os.system(command)
        


def main():
    print(banner)

    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        argument_exist =False
    else:
        argument_exist =True

    cli(argument_exist)



if __name__ == '__main__':
    main()


