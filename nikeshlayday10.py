#import socket
'''import socket
hostname = socket.gethostname()
ip = socket.gethostbyname("google.com")
print("hostname:",hostname)
print("ip:",ip)'''
from socket import socket
from urllib import response

#requests
'''import requests
response = requests.get("https://Livewiresalem.com")
print(response.status_code)
print(response.text)'''

#import the socket libary
'''import socket
s = socket.socket()
print("socket successfully created")
port = 9999
host = socket.gethostname()
s.bind((host,port))
s.listen(3)
print("socket is listening")
while True:
    c, addr = s.accept()
    print("got connection from",addr)
    c.send(b"thank you for connecting")
    c.close()'''

#client
'''import socket
s = socket.socket()
host = socket.gethostname()
port = 9999
s.connect((host,port))
print(s.recv(1024).decode())
s.close()'''

#tkinter
'''import tkinter as tk
root = tk.Tk()
root.title("hello")
root.geometry("1500x400")
label = tk.Label(root,text="hello")
label.pack()
root.mainloop()'''

#button
import tkinter as tk
def hello():
    print("hello")
root = tk.Tk()
button = tk.Button(root,text="click",command=hello)
button.pack()
root.mainloop()
