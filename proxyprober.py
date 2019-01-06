#Import dependencies
import os
from ScraperModules.socks4scrape import socks4scrape
from ScraperModules.httpscrape import httpscrape
from ScraperModules.socks5scrape import socks5scrape
from Functions.openingcredits import openingcredits
from Functions.clear import clear
from ScraperModules import variables
from colorama import init

#Enable ANSI escape character sequence support for Windows
init()

#Clear console
clear()

#Create output directory
outputdir = r'.\OUTPUT'
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

#Opening creidts
openingcredits()

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