### IMPORTS ###
import colorama
from sys import exit
from os import system
from time import sleep
import requests
import json
from discord_webhook import DiscordWebhook


### GLOBALS ###
colorama.init()
clear = "clear"
version = "1.00"
maincolor = colorama.Fore.LIGHTCYAN_EX
seccolor = colorama.Fore.WHITE
reset = colorama.Fore.RESET

timeout = 0
safetofile = True
filepath = ""
webhook = True
webhookurl = ""

socks5apis = [
f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout={str(timeout)}&country=all&ssl=all&anonymity=all",
f"https://www.proxyscan.io/api/proxy?format=txt&limit=20&type=socks5&ping={str(timeout)}",
"https://www.proxy-list.download/api/v1/get?type=socks5",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt"
]
socks4apis = [
f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout={str(timeout)}&country=all&ssl=all&anonymity=all",
f"https://www.proxyscan.io/api/proxy?format=txt&limit=20&type=socks4&ping={str(timeout)}",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
"https://www.proxy-list.download/api/v1/get?type=socks4",
"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt"
]
httpapis = [
f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout={str(timeout)}&country=all&ssl=all&anonymity=all",
"https://www.proxy-list.download/api/v1/get?type=http",
f"https://www.proxyscan.io/api/proxy?format=txt&limit=20&type=http&ping={str(timeout)}",
f"https://www.proxyscan.io/api/proxy?format=txt&limit=20&type=https&ping={str(timeout)}",
"https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
"http://pubproxy.com/api/proxy?format=txt&limit=5",
"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt",
"https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt"
]

### CONFIG LOADER ###
def loadconfig():
    try:
        with open("config.json","r") as f:
            config = json.load(f)
            global timeout 
            global filepath
            global webhook
            global webhookurl
            timeout = config["timeout"]
            filepath = config["filepath"]
            webhook = config["webhook"]
            webhookurl = config["webhookurl"]
        print(colorama.Fore.GREEN + "Successfully loaded config")
    except:
        print(colorama.Fore.RED + "Error: Config not available or corrupt")
        timeout = 300
        filepath = "scrapedproxies.txt"
        webhook = 0
        webhookurl = ""
    sleep(0.5)

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
            if count != 0:
                print(colorama.Fore.GREEN + f"Successfully scraped {str(count)} Proxies")
            else:
                print(colorama.Fore.RED + "Scraped 0 Proxies")
        except:
            print(colorama.Fore.RED + "Scraped 0 Proxies")
    count = len(proxies)
    print(maincolor + "Scraped" , str(count), "in total")
    proxies = set(proxies)
    print(maincolor + f"Deleted {str(count - len(proxies))} duplicates")
    if safetofile:
        for proxy in proxies:
            with open(filepath,"a+") as f:
                if proxy != "":
                    f.write(proxy.decode("utf-8") + "\n")
    if webhook:
        messages = []
        message = ""
        count
        for proxy in proxies:
            if proxy != "":
                message += proxy.decode("utf-8") + "\n"
                count += 1
            if count >= 100:
                messages.append(message)
                message = ""
                count = 0
        for msg in messages:
            if msg != "" or " ":            
                hook = DiscordWebhook(url=webhookurl,content=msg, rate_limit_retry=True)
                r = hook.execute()
                sleep(0.5)
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
        choice = input(maincolor + "Load config (Y/n) ")
        if not choice.lower() == "n":
            loadconfig()
        system(clear)
        banner()
        mainmenu()
        try:
            choices1[custominput()]()
        except KeyError:
            pass # Choice not available

if __name__ == "__main__":
    main()
