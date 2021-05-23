# importing socket library
#In computer networking, a hostname (archaically nodename) is a label that is assigned to a device connected to a computer network and that 
#is used to identify the device in various forms of electronic communication, such as the World Wide Web. ... In the latter form, a hostname 
#is also called a domain name.
import socket

def get_hostname_IP():
    hostname = input("Please enter website address(URL):")
    try:
        print (f'Hostname: {hostname}')
        print (f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print (f'Invalid Hostname, error raised is {error}')

get_hostname_IP()

