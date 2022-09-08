import time, socket, sys

print("Welcome to Chat Room")
print("Initialising....")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
print(host)
ip = socket.gethostbyname(host)
print(ip)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")")
name = input(str("Enter your name: "))

s.listen(2)
print("Waiting for incoming connections...")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())

while True:
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":", message)