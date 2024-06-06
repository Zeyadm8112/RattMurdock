# this is a python console script for RATTMURDOCK users  
# written by : NinjaCat811

#** imports :

import os
import sys
import random
import getpass

# ** Variables : 

help_menu = """
Arguments : 
    - t <ipadress> = run RattMurdock on target ip address
    - f <config file> = run RattMurdock by config file
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
    [*] Select A Number To Use Payload [8]

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

def cli(arguments):
    if arguments:
        print(read_config("config.ratt"))
        print("Options : ")
        print(options_menu)

        option = input(f"{header} $ ") 

    else:
        print(help_menu)

def os_detection():
    if os.name == "nt":
        return "w"
    
    if os.name == "posix":
        return "l"

# connect to target
# ! STILL WORKING ON
def connect(argument):
    if sys.argv[1] == "-t":
        ipv4 = sys.argv[2]
    if sys.argv[1] == "-f":
        


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


