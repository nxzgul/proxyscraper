### IMPORTS ###
import colorama
from sys import exit
from os import system
import requests


### GLOBALS ###
colorama.init()
clear = "clear"
version = "1.00"
maincolor = colorama.Fore.LIGHTCYAN_EX
seccolor = colorama.Fore.WHITE
reset = colorama.Fore.RESET

timeout = 3000
filepath = "scrapedproxies.txt"
socks5apis = [
f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout={str(timeout)}&country=all&ssl=all&anonymity=all",
]
socks4apis = [
f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout={str(timeout)}&country=all&ssl=all&anonymity=all",
]
httpapis = [
f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout={str(timeout)}&country=all&ssl=all&anonymity=all",
]

### SCRAPER ###
def scraper(type):
    proxies = []
    if type == "socks5":
        apis = socks5apis
    elif type == "socks4":
        apis = socks4apis
    elif type == "http":
        apis = httpapis
    print(maincolor + "Scraping", type.upper(), "...")
    for api in apis:
        try:
            r = requests.get(api)
            count = 0
            for proxy in r.iter_lines():
                proxies.append(proxy)
                count += 1
            print(colorama.Fore.GREEN + f"Successfully scraped {str(count)} Proxies")
        except:
            print(colorama.Fore.RED + "Scraped 0 Proxies")
    print("Scraped" , str(len(proxies)), "in total")
    for proxy in proxies:
        with open(filepath,"a+") as f:
            if proxy != "":
                f.write(proxy.decode("utf-8") + "\n")
    choice = input(maincolor + "Exit the Program (Y/n) ")
    if choice.lower() == "n":
        pass
    else:
        exit()

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
