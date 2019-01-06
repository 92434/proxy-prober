# Import dependencies
import requests
import re
from Functions.clear import clear
from Functions.openingcredits import openingcredits

#Create the socks5scrape function
def socks5scrape():

    #Clear console
    clear()

    #Opening credits
    openingcredits()

    #Clear contents of the output file
    file = open('OUTPUT/socks5proxies.txt', 'w')
    file.write("")
    file.close()

    #Variables
    regex = r"((?:\d{1,3}\.?){4})\D+(\d+)"
    urls = ["https://free-socks.in/", "https://www.xroxy.com/free-proxy-lists/?port=&type=Socks5&ssl=&country=&latency=&reliability=7500", "https://www.my-proxy.com/free-socks-5-proxy.html", "https://www.proxy-list.download/api/v1/get?type=socks5"]
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    #Send the HTTP requests
    for urlno, url in enumerate (urls):
        print("Scraping SOCKS5 source " + str(urlno) + "...\n")
        data = requests.get(url, headers=headers)
        proxiesdata = str(data.text)

        #Look for regex matches in the html body of the websites
        matches = re.finditer(regex, proxiesdata)

        #List the proxy matches
        for matchnumber, match in enumerate(matches, start=1):
            matchnumber = 1
            #Save the proxies in ip:port format
            proxies = "{ip}:{port}".format(ip = match.group(matchnumber), port = match.group(matchnumber + 1))
            saveproxies = "\n" + proxies
            file = open('OUTPUT/socks5proxies.txt', 'a')
            file.write(saveproxies)
            file.close()
    #Verify that all lines are real proxies
    print("\nVerifying that all lines are proxies...\n")
    textfile = open('OUTPUT/socks5proxies.txt', 'r')
    vf = textfile.read()
    textfile.close()
    matches = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b:\d{2,5}', vf)
    verify = open('OUTPUT/socks5proxies.txt', 'w')
    verify.writelines("\n".join(matches))

    #Remove duplicate proxies
    print("\nRemoving duplicate proxies...\n")
    uniquelines = set(open('OUTPUT/socks5proxies.txt').readlines())
    rm = open('OUTPUT/socks5proxies.txt', 'w')
    rm.writelines(set(uniquelines))
    rm.close()

    #Count number of proxies scraped
    with open('OUTPUT/socks5proxies.txt') as f:
        number = sum(1 for _ in f)
    print("\nFinished scraping! " + (str(number)) + " SOCKS5 proxies have been saved to OUTPUT/socks5proxies.txt.")

    #Exit the function
    return
