# Import dependencies
import requests
import re
import os
from termcolor import cprint
from pyfiglet import figlet_format

#Create the socks4scrape function
def socks4scrape():

    #Create the clear console function
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    cls()

    #Opening credits
    cprint(figlet_format('Proxy Prober', font='big'), 'green', attrs=['bold'])
    cprint(figlet_format(' v.3.2 \nBy HydraPhoenix', font='small'), 'red')

    #Clear contents of the output file
    file = open('OUTPUT/socks4proxies.txt', 'w')
    file.write("")
    file.close()

    #Variables
    regex = r"((?:\d{1,3}\.?){4})\D+(\d+)"
    socks4urls = ["https://www.socks-proxy.net/", "https://www.xroxy.com/free-proxy-lists/?port=&type=Socks4&ssl=&country=&latency=&reliability=7500", "https://www.my-proxy.com/free-socks-4-proxy.html", "https://www.proxy-list.download/api/v1/get?type=socks4"]
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    
    #Send the HTTP requests
    for socks4url in socks4urls:
        print("Scraping SOCKS4 source " + str(socks4url) + "...\n")
        data = requests.get(socks4urls[socks4url], headers=headers)
        proxiesdata = str(data.text)

        #Look for regex matches in the html body of the websites
        matches = re.finditer(regex, proxiesdata)

        #List the proxy matches
        for match in enumerate(matches, start=1):

            #Save the proxies in ip:port format
            proxies = "{ip}:{port}".format(ip = match.group(1), port = match.group(2))
            file = open('OUTPUT/socks4proxies.txt', 'a')
            file.write("\n" + proxies)
            file.close()
    #Verify that all lines are real proxies
    print("\nVerifying that all lines are proxies...\n")
    textfile = open('OUTPUT/socks4proxies.txt', 'r')
    vf = textfile.read()
    textfile.close()
    matches = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b:\d{2,5}', vf)
    verify = open('OUTPUT/socks4proxies.txt', 'w')
    verify.writelines("\n".join(matches))

    #Remove duplicate proxies
    print("\nRemoving duplicate proxies...\n")
    uniquelines = set(open('OUTPUT/socks4proxies.txt').readlines())
    rm = open('OUTPUT/socks4proxies.txt', 'w')
    rm.writelines(set(uniquelines))
    rm.close()

    #Count number of proxies scraped
    with open('OUTPUT/socks4proxies.txt') as f:
        number = sum(1 for _ in f)
    print("\nFinished scraping! " + (str(number)) + " SOCKS4 proxies have been saved to OUTPUT/socks4proxies.txt.")

    #Exit the function
    return
