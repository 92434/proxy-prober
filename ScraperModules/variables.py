#Import dependencies


regex = r"((?:\d{1,3}\.?){4})\D+(\d+)"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
httpurls = ["https://free-proxy-list.net", "https://free-proxy-list.net/anonymous-proxy.html", "https://www.us-proxy.org/", "https://www.sslproxies.org/", "https://www.xroxy.com/free-proxy-lists/?port=&type=All_http&ssl=&country=&latency=&reliability=7500", "https://www.proxy-list.download/api/v1/get?type=http", "https://www.proxy-list.download/api/v1/get?type=https"]
socks4urls = ["https://www.socks-proxy.net/", "https://www.xroxy.com/free-proxy-lists/?port=&type=Socks4&ssl=&country=&latency=&reliability=7500", "https://www.my-proxy.com/free-socks-4-proxy.html", "https://www.proxy-list.download/api/v1/get?type=socks4"]
socks5urls = ["https://free-socks.in/", "https://www.xroxy.com/free-proxy-lists/?port=&type=Socks5&ssl=&country=&latency=&reliability=7500", "https://www.my-proxy.com/free-socks-5-proxy.html", "https://www.proxy-list.download/api/v1/get?type=socks5"]