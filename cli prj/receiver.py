import socket
import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP protocol

ip_address = "127.0.0.1"
port_no = 2525
print(datetime.datetime.now())

complete_address = (ip_address, port_no)

s.bind(complete_address)

print("Hey, I am listening......")

while True:
    messages = s.recvfrom(100)
    message = messages[0].decode()
    addr = messages[1]
    sender_ip = addr[0]
    sender_port = addr[0]
    current_time = datetime.datetime.now()

    print(f"Message: {message}")
    print(f"IP Address: {sender_ip}")
    print(f"Port Number: {sender_port}")
    print(f"Datetime: {current_time}")
    print("-----------------------------------------------------------")

    with open("demoo.txt", "a") as file:
        file.write(f"Message: {message} \n")
        file.write(f"IP Address: {sender_ip}\n")
        file.write(f"Port Number: {sender_port}\n")
        file.write(f"Datetime: {current_time}\n")
       




















'''import socket
import datetime
s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP protocol 
#ip_address = "192.168.39.221"
ip_address = "127.0.0.1"
port_no=2525
print(datetime.datetime.now())

complete_address = (ip_address,port_no)


s.bind(complete_address)

print("Hey i am listening......")

while True:
    
    messages =s.recvfrom(100)
    print(messages)
    print(datetime.datetime.now())'''
    