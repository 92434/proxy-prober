# Import dependencies
import requests
import re
from Functions.clear import clear
from Functions.openingcredits import openingcredits
import variables

#Create the socks4scrape function
def socks4scrape():

    #Clear console
    clear()

    #Opening credits
    openingcredits()

    #Clear contents of the output file
    file = open('OUTPUT/socks4proxies.txt', 'w')
    file.write("")
    file.close()
    
    for urlno, url in enumerate (variables.socks4urls):
        print("Scraping SOCKS4 source " + str(urlno) + "...\n")
        data = requests.get(url, headers=variables.headers)
        proxiesdata = str(data.text)

        #Look for regex matches in the html body of the websites
        matches = re.finditer(variables.regex, proxiesdata)

        #List the proxy matches
        for matchnumber, match in enumerate(matches, start=1):
            matchnumber = 1
            #Save the proxies in ip:port format
            proxies = "{ip}:{port}".format(ip = match.group(matchnumber), port = match.group(matchnumber + 1))
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
