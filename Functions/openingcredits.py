# Import dependencies
from termcolor import cprint
from pyfiglet import figlet_format

def credits():
    cprint(figlet_format('Proxy Prober', font='big'), 'green', attrs=['bold'])
    cprint(figlet_format(' v.3.3 \nBy HydraPhoenix', font='small'), 'red')
    return