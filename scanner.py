import requests
import pyfiglet
from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
            _ = system('clear')

clear()
ascii_banner = pyfiglet.figlet_format('DIRScanner')
print(ascii_banner)
print("Ver 1.0")

sleep(2)

target = input('Target : ')


def req(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
            pass

    



with open("data/dir.txt","r") as wordlist_file:
    for line in wordlist_file:
        word=line.strip()
        test=target+"/"+word
        response = req(test)
        if response:
            print(test + " >> \033[92m 200 Ok \033[0m ")

        else:
                print(test + " >> \033[91m 404 Not Found \033[0m ")
                pass