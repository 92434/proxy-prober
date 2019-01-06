#Import dependencies
from pyfiglet import figlet_format
import os
from termcolor import cprint
from ScraperModules.socks4scrape import socks4scrape
from ScraperModules.httpscrape import httpscrape
from ScraperModules.socks5scrape import socks5scrape

#Create the clear console function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

#Create output directory
outputdir = r'.\OUTPUT'
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

#Opening creidts
cprint(figlet_format('Proxy Prober', font='big'), 'green', attrs=['bold'])
cprint(figlet_format(' v.3.2 \nBy HydraPhoenix', font='small'), 'red')

#User input options
while True:
    try:
        choice = int(input("\n[1] Scrape HTTP Proxies\n\n[2] Scrape SOCKS4 Proxies\n\n[3] Scrape SOCKS5 Proxies\n\n"))
        if choice not in (1, 2 ,3):
            print("\nPlease pick one of the choices above")
        else:
            break

    except ValueError:
        print("\nPlease pick one of the choices above")

if choice == 1:
    httpscrape()
elif choice == 2:
    socks4scrape()
elif choice == 3:
    socks5scrape()
    
input()