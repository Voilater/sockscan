import socket
from datetime import datetime
from pyfiglet import Figlet
from clint.textui import colored



banner = Figlet(font='slant')
print(colored.red(banner.renderText("Sock Scan")))


HOST = "127.0.0.1"

t1 = datetime.now()
print(colored.green(t1))

try:
    # will scan ports between 1 to 65,535
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = s.connect_ex((HOST,port))
        if result == 0:
            print(f"port are open {port}")

        s.close()

except KeyboardInterrupt:
		print("\n bye ")

