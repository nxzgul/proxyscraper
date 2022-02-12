### IMPORTS ###
import colorama
from sys import exit
from os import system
import requests


### GLOBALS ###
colorama.init()
clear = "clear"
version = "1.00"
maincolor = colorama.Fore.CYAN
seccolor = colorama.Fore.WHITE
reset = colorama.Fore.RESET

timeout = 3000
socks5apis = [f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout={str(timeout)}&country=all&ssl=all&anonymity=all"]
socks4apis = [f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout={str(timeout)}&country=all&ssl=all&anonymity=all"]
httpapis = [f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout={str(timeout)}&country=all&ssl=all&anonymity=all"]

### SCRAPER ###
def scraper(type):
    proxies = []
    if type == "socks5":
        apis = socks5apis
    elif type == "socks4":
        apis = socks4apis
    elif type == "http":
        apis = httpapis
    print("Scraping", type, "...")
    for api in apis:
        try:
            r = requests.get(api)
            with open("scrapedproxies.txt","a+") as f:
                f.write(r.text)
            print(colorama.Fore.GREEN + "Successfully scraped Proxies")
        except:
            print(colorama.Fore.RED + "Error: API Offline")
    input(reset + "Press any Key to Exit ... ")

def socks5scrape():
    scraper("socks5")

def socks4scrape():
    scraper("socks4")

def httpscrape():
    scraper("http")

### UI ###
def custominput():
    return input(maincolor + "==> " + seccolor)

def banner():
    print(f"""{maincolor}
       ███▄    █  ▄▄▄      ▒███████▒  ▄████  █    ██  ██▓        
       ██ ▀█   █ ▒████▄    ▒ ▒ ▒ ▄▀░ ██▒ ▀█▒ ██  ▓██▒▓██▒        
      ▓██  ▀█ ██▒▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██░▄▄▄░▓██  ▒██░▒██░        
      ▓██▒  ▐▌██▒░██▄▄▄▄██   ▄▀▒   ░░▓█  ██▓▓▓█  ░██░▒██░        
      ▒██░   ▓██░ ▓█   ▓██▒▒███████▒░▒▓███▀▒▒▒█████▓ ░██████▒    
      ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░▒▒ ▓░▒░▒ ░▒   ▒ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░    
      ░ ░░   ░ ▒░  ▒   ▒▒ ░░░▒ ▒ ░ ▒  ░   ░ ░░▒░ ░ ░ ░ ░ ▒  ░    
         ░   ░ ░   ░   ▒   ░ ░ ░ ░ ░░ ░   ░  ░░░ ░ ░   ░ ░       
               ░       ░  ░  ░ ░          ░    ░         ░  ░    
          Github : {seccolor}nxzgul{maincolor}    ░   {seccolor}Proxyscraper v{str(version)}{maincolor}   
    """)

def mainmenu():
    print(f"""{maincolor}╔═══════════════════════════════════════════════════════════════╗
║              [{seccolor}0{maincolor}] : Exit the Program                           ║
║              [{seccolor}1{maincolor}] : Scrape Socks5 Proxies                      ║ 
║              [{seccolor}2{maincolor}] : Scrape Socks4 Proxies                      ║
║              [{seccolor}3{maincolor}] : Scrape HTTP   Proxies                      ║
╚═══════════════════════════════════════════════════════════════╝""")

choices1 = {"0":exit,"1":socks5scrape,"2":socks4scrape,"3":httpscrape}

### PROGRAM ###
def main():
    while True:
        system(clear)
        banner()
        mainmenu()
        try:
            choices1[custominput()]()
        except KeyError:
            pass # Choice not available

if __name__ == "__main__":
    main()
