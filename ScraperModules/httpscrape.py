# Import dependencies
import requests
import re
import os
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

#Create the httpscrape function
def httpscrape():

    #Create the clear console function
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    cls()

    #Opening credits
    cprint(figlet_format('Proxy Prober', font='big'), 'green', attrs=['bold'])
    cprint(figlet_format(' v.3.2 By HydraPhoenix', font='small'), 'red')

    #Clear contents of the output file
    file = open('OUTPUT/httpproxies.txt', 'w')
    file.write("")
    file.close()

    #Variables
    regex = r"((?:\d{1,3}\.?){4})\D+(\d+)"
    httpurls = ["https://free-proxy-list.net", "https://free-proxy-list.net/anonymous-proxy.html", "https://www.us-proxy.org/", "https://www.sslproxies.org/", "https://www.xroxy.com/free-proxy-lists/?port=&type=All_http&ssl=&country=&latency=&reliability=7500", "https://www.proxy-list.download/api/v1/get?type=http", "https://www.proxy-list.download/api/v1/get?type=https"]
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    
    #Send the HTTP requests
    for httpurl in range(len(httpurls)):
        print("Scraping HTTP source " + str(httpurl) + "...\n")
        data = requests.get(httpurls[httpurl], headers=headers)
        proxiesdata = str(data.text)

        #Look for regex matches in the html body of the websites
        matches = re.finditer(regex, proxiesdata)

        #List the proxy matches
        for matchNum, match in enumerate(matches, start=1):

            #Save the proxies in ip:port format
            proxies = "{ip}:{port}".format(ip = match.group(1), port = match.group(2))
            file = open('OUTPUT/httpproxies.txt', 'a')
            file.write("\n" + proxies)
            file.close()
    
    #Verify that all lines are real proxies
    print("\nVerifying that all lines are proxies...\n")
    textfile = open('OUTPUT/httpproxies.txt', 'r')
    vf = textfile.read()
    textfile.close()
    matches = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b:\d{2,5}', vf)
    verify = open('OUTPUT/httpproxies.txt', 'w')
    verify.writelines("\n".join(matches))

    #Remove duplicate proxies
    print("\nRemoving duplicate proxies...\n")
    uniquelines = set(open('OUTPUT/httpproxies.txt').readlines())
    rm = open('OUTPUT/httpproxies.txt', 'w')
    rm.writelines(set(uniquelines))
    rm.close()

    #Count number of proxies scraped
    with open('OUTPUT/httpproxies.txt') as f:
        number = sum(1 for _ in f)
    print("\nFinished scraping! " + (str(number)) + " HTTP proxies have been saved to OUTPUT/httpproxies.txt.")

    #Exit the function
    return
