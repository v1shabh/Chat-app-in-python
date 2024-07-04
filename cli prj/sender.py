import socket

s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP protocol 

target_ip="127.0.0.1"
target_port=2525


while True:
   message = input("plz eneter the message: ")
   message = message.encode("ascii")
   s.sendto(message,(target_ip,target_port))
   print("your msg has been send successfully send!")






   
  