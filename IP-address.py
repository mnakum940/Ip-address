import socket as s

host = input("Enter URL:")
print(f'IP of {host} is {s.gethostbyname(host)}')

